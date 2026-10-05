#!/usr/bin/env python3
r"""
ledger.py -- WHAT IS ESTABLISHED, WHAT IS OWED, AND WHICH SIDE OWES IT.

    python3 ledger.py             the reading
    python3 ledger.py --selftest  every row asked of its owner; stdlib only
    python3 ledger.py --md        write LEDGER.md
    python3 ledger.py --check     LEDGER.md against a fresh ask; exit 1 on drift

Run under python3 (3.11).  STDLIB ONLY, plus the seated peers it asks.

===============================================================================
0.  WHY THIS EXISTS, AND WHAT IT IS NOT
===============================================================================

M ruled the order of work: CONSOLIDATE first, keep TESTING beside it, and only
then build the positive theory -- "we'll be working it like balancing an
equation with the theory and math on one side, and the device engineering and
materials on the other side".  This file is the first half of that instruction
and it is built in the shape of the second.

    IT ESTABLISHES NOTHING.  Not one row here is derived, measured or proved by
    this file.  Every row is ASKED of the instrument that owns it, at run time,
    and a row whose owner disagrees is a failure rather than a surprise.  That
    is `state.py`'s discipline applied to the warp work, which had no equivalent:
    `state.py` answers "what is the index right now", and nothing answered "what
    is the warp result right now".

    IT IS NOT A SUMMARY EITHER.  A summary can be read and believed.  This can
    be RUN, and `--check` fails when a peer moves underneath it.  The distinction
    is the whole point: this project has twice shipped a figure that was true
    when written and false when read -- `achievable.py`'s "sixty-five orders",
    `bounds.py`'s "Casimir saturates Ford-Roman" -- and both were prose quoting a
    number no instrument was asked for.

===============================================================================
1.  THE FIVE STATUSES, AND WHY THERE ARE FIVE RATHER THAN TWO
===============================================================================

M's standing rule is "Nothing less than computed or measured".  That rules out
ASSERTION as a status; it does not collapse the rest into one, because a
THEOREM and a SURVEY fail in different ways and a reader who cannot tell them
apart cannot tell what would change the answer.

  THEOREM    proved, with stated hypotheses, and the hypotheses are named.  It
             fails only if a hypothesis fails.
  MEASURED   a number produced by a computation someone can re-run.  It fails if
             the computation is wrong or its inputs move.
  SURVEY     true of everything looked at, and nothing proves the look was
             exhaustive.  It fails silently, when something unlooked-at turns up.
             DOCKET 55's verdict is this and says so.
  OPEN       named, not answered, and the thing that would answer it is named.
  WITHDRAWN  this project asserted it and then refuted it.  KEPT, never deleted:
             a withdrawn figure that leaves no trace is how a corpus forgets it
             was ever wrong.

THE DISTINCTION THAT MATTERS MOST HERE IS THEOREM AGAINST SURVEY, and it is
DOCKET 55's own finding about itself: four limbs, each proved inside its own
hypotheses, whose CONJUNCTION is a survey because nothing proves those
hypotheses exhaust the matter models.  Calling that conjunction a theorem would
be `achievable.py`'s error committed one level up.

===============================================================================
2.  THE TWO SIDES
===============================================================================

LEFT, THE DEMAND.  What the theory requires of any device that does this, with
the status of each requirement.  This side is settled by mathematics and moves
only when a proof moves.

RIGHT, THE SUPPLY.  What physics and materials actually deliver, with a ceiling
on each.  This side moves when a measurement improves or a mechanism is found.

THE BALANCE is the difference, in orders of magnitude, and the honest reading of
it is NOT always "how far short we are".  Two rows on this ledger are short by a
finite, quotable number.  One is short by a number that no engineering can move
because the ceiling is a-INDEPENDENT.  And one is not short at all -- DOCKET 56's
reconstruction route has a PRICE, and until DOCKET 65 it was the only row here
that did; DOCKET 65's remainders S11-S13 are priced too (section 6).

    A ROW WHERE THE DEMAND IS REFUSED RATHER THAN EXPENSIVE IS MARKED REFUSED
    AND CARRIES NO GAP.  A gap implies a ladder.  Where the sign inverts before
    the magnitude is reached, there is no ladder and quoting a gap would invent
    one.  DOCKET 54's Boyer inversion and DOCKET 53's plate mass are both of this
    kind and neither gets a number in the gap column.

===============================================================================
3.  WHAT THIS FILE REFUSES
===============================================================================

    IT DOES NOT RANK THE OPEN QUESTIONS.  How many are open is whatever
    statuses() counts -- this sentence first said "Three are open" and went
    stale the day O4-O7 arrived, which is the fault this file exists to catch,
    so no count is typed here.  Which is most promising is a judgement and
    judgements are M's.
    IT DOES NOT TOTAL THE GAPS.  Orders of magnitude on different quantities do
    not add, and a single headline number would be the most quotable false thing
    in the repository.
    IT DOES NOT CARRY THE INDEX WORK.  `state.py` owns that and this file does
    not duplicate a row of it.
    IT REPAIRS NOTHING AND EDITS NO PEER.

===============================================================================
4.  DOCKETS 62 AND 63, AS M RULED THEM
===============================================================================

DOCKET 62 CLOSED NOTHING.  O2, O3, O5, O6 and O7 stay OPEN and are NARROWED,
each now ASKED of the instrument that seated its narrowing (fewsterteo.py,
latticectc.py, throatmass.py, branelink.py), and each owner is asked whether it
closed -- an open row whose owner says CLOSED is a selftest failure.  The one
new row its narrowings produced is the flat-bulk lattice theorem, D21, a
THEOREM with its hypotheses named; its RECOMMENDED new rows are decided below,
one by one, under the principle for opening a row.  REFUSED by the ruling
and therefore NOT on this board: closing any of the five; the
curvature-tightened persistence figures; the void 9/64 adjustment; an R-1 row (it is O7 renamed); a separate NEC-everywhere row (it is
O3 with a clause); the Caldwell & Langlois withdrawal (it has no referent).
The selftest asserts each refusal.  The wording each narrowing replaced is
KEPT in SUPERSEDED_WORDING, because a row rewritten in place leaves no trace
otherwise.

DOCKET 63 adds D15-D20 (the Higgs at the endpoint), S6-S8 (all REFUSED, no
gap) and W9-W13, owners as the ruling named them.  W9 is excite.W9 and
W10-W13 are address.WITHDRAWN: the withdrawn rows are ASKED too, not retyped.

THE PRINCIPLE FOR OPENING A ROW, STATED ONCE AND APPLIED TO EVERY CANDIDATE:

    A QUESTION THE TREE ALREADY HAS AN INSTRUMENT FOR GETS A ROW NOW -- the
    board must not lag the tree.  A QUESTION WITH NO INSTRUMENT IS OPENED BY
    THE DOCKET THAT BUILDS ITS INSTRUMENT, because a row this file cannot ask
    is a row it cannot defend.

    AND A ROW IS FOR A QUESTION THAT CAN MOVE A REQUIREMENT OR A PRICE ON THE
    BOARD.  An unsettled question internal to an already-REFUSED row, which
    gates nothing, is recorded where that row's owner records it and gets no
    row of its own -- one row per question would over-represent it.  This is
    the criterion that keeps DOCKET 63 section E's thirteen items off the
    board (see the census re-pin below); it is part of the principle, not an
    exception to it.

Applied, candidate by candidate (the owner was READ before each decision):
  D22  stress-tensor fluctuations -- fluctuation.py.  OPENED.
  D23  the first trip / amortisation -- transit.py (TRAVERSAL_IS_REMOVED).
       OPENED; S5's note now carries the amortisation reading.
  D24  formation -- create.py (NUCLEATION_STATUS).  OPENED.
  D25  the destination stock gate -- stockgate.py (GATE), auditing stock.py.
       OPENED.
  S9   the Drive folder's device specification as a supply -- warpfolder.py
       (FLASH_IS_A_RECONSTRUCTION_MECHANISM).  SEATED, REFUSED.
  linearised stability -- OPENED by DOCKET 64 as D26 (linstab.py).  At
       DOCKETS 62/63 it was NOT OPENED because no instrument asked it:
       stability.py asked only the CLASSICAL radial stability of
       concentric.py's shell, and nothing evaluated Anderson-Molina-Paris-
       Mottola's criterion on anything.  That deferral is what the principle's
       second half is for, and DOCKET 64 built the instrument.
       WAITS_FOR_ITS_INSTRUMENT is now empty, and LEDGER.md prints "none"
       rather than dropping the section.
  the FINITE Higgs share of atomic mass -- massform.py.  NOT A ROW, ON M's
       RULING M-D65-2 ('Fold into S10 (Recommended)').  The question is
       internal to the REFUSED row S10, it gates nothing ("nothing in DOCKET
       65 moves on it") and nothing computes it, so by the principle's clause
       on questions internal to an already-REFUSED row that gate nothing it is
       recorded where its owner records it: as the OPEN item
       "S10 (open)" inside S10's note, a candidate question for a future
       docket.  DOCKET 65's seating first opened it as its own row, O8; M was
       asked which it should be and ruled the fold, and O8 is not seated.

===============================================================================
5.  DOCKET 64, AS M RULED IT
===============================================================================

M ruled that all DOCKET 64 calculations run and be seated.  Five instruments
were seated first -- noise.py, hpscentre.py, qeihps.py, linstab.py and
formation.py -- and every row below is ASKED of them.  This file reads their
CORRECTED attributes, which are in places weaker than the ruling's section C
wording, because the ruling never saw the full verifier verdicts for three of
the lines; where the two differ the weaker, better-supported statement is the
one printed here:

  D22  OPEN -> SURVEY, owner noise.CORRIDOR_APPLICATION.  C1 is a THEOREM in
       the flat model H1-H6 only; on the corridor H2 fails and the curved
       decision is O2's.  The Einstein-Langevin surrogate figure is printed
       from noise.EL_VACUUM_LOG10_NEG_LN_P, never typed.
  D24  stays OPEN, owner formation.NUCLEATION_PRICEABLE_FROM_SOURCE, whose
       value is NOT DETERMINED: the neck is a recipe with free functions and
       its price has not been computed.  "Cannot be priced from the source"
       was withdrawn by formation.py's verification and is not printed.
  D25  stays OPEN and UNCHANGED, owner stockgate.GATE.  formation.py evaluates
       no conjunct anew and re-prices none; stockgate's figures are not
       re-printed a second time.  The survey names a CONDENSED body (Proxima b);
       what is open is "primitive" and "accessible".
  D26  NEW, OPEN, owner linstab.SEMICLASSICAL_EVALUABLE_ON_DEMAND, text
       linstab.D26_CLAIM with the IFF narrowed to GMMPS's reported mode and
       "recorded or shown" in place of a proof.
  O5   stays OPEN, re-owned to hpscentre.O5_CLOSED; the throat-geodesic
       verdict is qeihps.VERDICT_THROAT_GEODESIC, "NOT A TEST".
  O2   stays OPEN; its answer now names D22's curved distribution question.

Not opened, each because it is the SAME question as an existing row (a
second row for one question is the over-representation the principle
forbids): the curved smeared variance (O2's); Kontou's QEI on HPS (O5's);
formation (D24's third part).  The phase1 D4 restatement was a requirement
question for M, not a row.  M RULED: restate it.  phase1.py now states D4 as
T^{0i} = 0 in each configuration and zero net momentum across a passage, and
RULED_BY_M records the ruling (M-D64-1).

DOCKET 64's lines withdrew claims their own reports had made before seating.
Each is kept on its owner (noise.WITHDRAWN, hpscentre.WITHDRAWN,
linstab.WITHDRAWN, qeihps.VERDICT_THROAT_GEODESIC_WITHDRAWN, formation.py's
[W1]-[W7]).  None was ever on this board, so none is a W row here; the board
wording DOCKET 64 replaced is kept in SUPERSEDED_WORDING.

===============================================================================
6.  DOCKET 65, AS M RULED IT
===============================================================================

DOCKET 65 tested M's mechanism (M-S1A-P1) in massform.py, and M ruled its rows
"Seat as proposed".  Every one is ASKED of massform.PROPOSED_ROWS at run time
-- text, status and owner -- and none is retyped here:

  D27, D28, D29  DEMAND, each a THEOREM on hypotheses its own row names
                 (M's consideration computed; the pair floor; the field has no
                 energy to give about v).
  S10            SUPPLY, M's mechanism as a supply of payload mass.  Its status
                 IS massform.MECHANISM_VERDICT[0], REFUSED reading by reading;
                 gap None, since no ladder is quoted for a refusal.
  S11, S12, S13  SUPPLY, OPEN: the anomaly route, the pair route and the
                 held-seat release route -- priced remainders, not refusals.
                 Their names are massform.SURVIVES's.
  S10 (open)     NOT A ROW: the FINITE Higgs share of atomic mass, an OPEN
                 item carried inside S10's note -- massform's item, asked, its
                 status massform.FINITE_HIGGS_SHARE_STATUS.  No DOCKET 65
                 verdict rests on it.  The seating first opened it as the row
                 O8; M ruled M-D65-2, 'Fold into S10 (Recommended)', and it is
                 folded back (section 4).
  S5             note appended: reconstruction from destination stock survives
                 M's mechanism (massform.RECONSTRUCTION_SURVIVES).

Not opened: massform.NOT_OPENED (asked), each internal to S10 or S13 or gating
nothing (the selftest asks each item: it names S10 or S13, says 'no verdict',
or is the H-FLAV-only sub-count, whose owner says it carries no verdict).

A SUPPLY row has one note, so S10-S13 carry the proposed claim followed by
what would move it, both asked; S10's note then carries the item S10 (open),
its text and what would move it, asked too.  massform.py asks THIS file for D23 (the
held-seat route needs a prior arrival) and for M's words, and it does so only
at CALL time, never while it is being imported: this file asks massform for
its rows during its own import, and two modules that each need the other at
import find each other empty.

M's QET ruling is on RULED_BY_M as M-D65-1: Quantum Energy Teleportation is not
a docket of its own; it is FOLDED INTO DOCKET 66.  Its literature was CITED, not
READ, when M ruled -- nothing in this tree had read those papers; DOCKET 66 has
since READ them (qet.py; section 8), and the first sentence is kept as history.  M's ruling on the finite
Higgs share is M-D65-2: folded into S10's note, not a row.  M's ruling on
DOCKET 67 is M-D65-3: the audit of the external results the board's refusals
rest on is OPENED, to run after DOCKET 65 is seated and before DOCKET 66 (NOT
YET RUN; specthm's DOCKETS_OPENED records it); no row here.  M's ruling on
the paper's caveat (b) is M-D65-4: qualified on P-UNIFORM, a named premise --
a paper edit on M's ruling under M's rule for the paper (M_PAPER_RULE_WORDS,
M's words verbatim from the session, witnessed by the lead; the tree holds no
copy to check them against); the paper's other marked edit on M's ruling is
DOCKET 63's, at the marker paper_d63_marker() READs back from paper/CLAIMS.md
(PAPER_D63_MARKER_LINE) -- so it stood when M ruled M-D65-4; CORRECTED
(DOCKET 67 follow-ups): the paper has since carried DOCKET 67's markers,
'(Corrected on M's "Repair all", DOCKET 67: ...)', which name M's ruling by
M's words and which paper_docket_markers() READs as naming one -- the
paper's edits are not counted here, the markers are named and the reader
counts; CORRECTED (DOCKET 67 close): the closing rulings' markers carry M's
words for those rulings, not "Repair all", so the census READs the general
head (PAPER_D67_MARKER_HEAD_RE) and paper_d67_words() lists the words READ.  M's ruling on the ruling id in the
paper's clause is M-D65-5: added (M_D65_5_ANSWER); the markers this file names
each name a ruling, and the paper's DOCKET markers are asked of the paper by
paper_docket_markers() and printed in M-D65-5's cell, a census the reader
counts; paper_caveat_b_faults() READs the clause back.  Nothing from
DOCKET 65 is pending M.

===============================================================================
7.  DOCKET 68, WAVE 1, AS M RULED IT
===============================================================================

DOCKET 68 asked M's question -- information without transit -- and M ruled
the order of what follows it: "1 then 2 then 3 then 4" (M-D68-10); step 1 is
this seating.  Its instruments sit in docket68/ and are the owners here:
combine.py (the seven hypotheses in combination, z3), settle.py, frame.py,
measure.py (Q-1) and signed.py (Q-1s); geometry.py's grades reach this file
only through combine.py.  NOTHING IS RETYPED.  Every D68 verdict below is
asked of combine.Screen at run time, for the variants D68_VARIANTS names.

  O9   OPEN, NEW: THE TWO CLASSICAL BITS, AND WHAT ELSE STANDS.  Its cell is
       the obstruction table, ASKED: member-attributed removals first (O-BITS
       REMOVED-IF by W2 x F1 on two supports, or by clause 2b's D-CTC with
       O-LOOP reintroduced); then the NOT-BOUND-IF entries under H-IT as an
       information layer (not removals); then the OPEN pathways and
       NOT-BOUND-IF the other readings give, none a removal (KR, W1 x F1,
       KR x F1, ITJ, ITE, RQ, and ITB+RQ, where R-QUANTUM undoes ITB's
       non-binding -- ADDED by the DOCKET 68 residuals: O9 first asked only
       the board, W2, F1, W2 x F1, F2b, ITB, ITB+RI and SHAPE); the
       geometry's corridor O-LOOP, credited to no hypothesis, with F1's
       alternative member support beside it; O-SEAT OPEN via S5/D25 under
       H-SEAT-S5 (M: "S5 counts (Recommended)"), LEFT given H-SEAT-ROUTES;
       O-MAKE in its distribution form OPEN via N_VAC.  Q-1 and Q-1s are
       carried in the same cell as the computed measures R-INDEX uses (Re H,
       Im H = pi N, M = ln sum|p|).  The separable claim (X = c Re H + b N
       over every continuous separable functional) is signed.py's section
       (4b), under H-SEPARABLE, H-FINSIGNED and H-CONT-G: its algebraic steps
       z3-checked (asked of signed.z3_obligations), its analytic steps DERIVED
       by hand and READ as cited; signed.separable_nullspace is corroboration,
       not proof; uniqueness OPEN for non-separable functionals.  CORRECTED
       (DOCKET 68 residuals): first attributed to the null space and under
       H-SEPARABLE alone.  Q-1 and Q-1s get no row of their own, here or in
       index3.py: a measure counts and moves no requirement or price
       (measure.GRADES['Q-1'] LEAVES-ALL, asked), so a row would
       over-represent it -- section 4's principle.  (index3.py's row for them
       was REMOVED by the residuals: its Z = +1 had no numeric requirement
       stated by an owner, and at Z = 0 it sits on the null cell.)
  O9's closing is ASKED, not flagged: no docket68 owner pins an O9_CLOSED,
       so OPEN_ROW_READINGS holds what would close it -- O-BITS REMOVED with
       no named premise (combine.counts(<variant>, ('REMOVED',))) in any asked
       variant -- and the selftest asks it in place of a flag.
  S5, S10, S13, D23, D25  each carries a DOCKET 68 NOTE, asked, and NO status
       change: no owner's computed status moved (S5 and D25 OPEN, S10 and S13
       as massform states them, D23 OPEN).  O-SEAT touches S5 (the route),
       D25 (the gate), S13 (it forms no baryons, C3, under H-C3), S10 (its
       row) and D23 (S5's channel, and N_VAC, the pair supply wave 2 reads).
  RULED_BY_M  M-D68-1..13 (M-RULINGS-2026-10-03.md, items 1-13; item 11, M's
       novelty gate on the paper, recorded 2026-10-04 and ADDED by the
       residuals; items 12 and 13, M's rulings on the paper -- correct
       CLAIMS.md 4647-4648, scope H62d -- whose applied text is the paper's
       marked line, READ back by paper_d68_marker() from M's words in the
       marker head, never typed), the charter's rulings M-D68-C1, C2, C3, C5 and C8
       (open after D67; the 12-vector; deterministic drift; consider both 1
       and 2; negative probabilities and Q-1s), and M-D68-C12 (record the
       ER = EPR source in emtension.py: ruled 2026-10-02, before DOCKET 68
       opened, and applied that day; M-RULINGS-2026-10-03.md item 14 holds
       the question and M's answer verbatim), each with M's words
       verbatim, held once in D68_M_WORDS and checked by the selftest
       against the tree's own copy (M-RULINGS-2026-10-03.md or CHARTER.md),
       the question as the tree records it, the option taken and what was
       applied.  Where M replied to a route put to M, only M's reply is held
       and the route is printed as the question, the charter's words
       (D68_ROUTES, checked the same way).  Where the tree holds M's answer
       only as the charter's carrying (the 12-vector, deterministic drift),
       the cell says so: no paraphrase is printed as M's words.
  CARRIED, NOT RULED  M-D68-C4 (test in combination, M's instruction),
       C6 (H-ZERO, M's proposal), C7 (H-NULL, M's statement), C9 (H-IT, M's
       instruction to assume it), C10 (H-FRAME, with M's question on
       flatness, which prompted the FRW finding) and C11 (H-INFO and its
       request, Q-1): M's words verbatim (D68_CARRIED_WORDS, checked), each
       carried by the charter as a hypothesis or a standing instruction, in
       D68_CARRIED and its own LEDGER.md section -- NOT on RULED_BY_M and
       not counted as rulings.  MOVED by the residuals: C4, C6 and C7 were
       first seated on RULED_BY_M under a 'RULED BY M' prefix their own text
       contradicted; C9-C11 ADDED.  M's hypotheses (H-IT, H-SETTLE, H-FRAME,
       H-12, H-INFO, H-ZERO, H-NULL) are carried AS HYPOTHESES, in
       combine.py, never as results; a ruling to carry one applies the
       carrying, not the claim.
  QUOTATIONS  Every quotation in a DOCKET 68 cell is the tree's words or
       declared otherwise (d68_quote_faults): a double-quoted span must be a
       held text (M's words, a route, M's thesis, the question, or an inline
       quotation in D68_INLINE_QUOTES), and every quoted span here and in
       index3.py's DOCKET 68 rows must occur verbatim in CHARTER.md or
       M-RULINGS-2026-10-03.md.  ADDED by the residuals: the D23 note first
       printed M's words emended.
  PENDING  none.  M-D68-P1 -- whether to record emtension.py's
       ENTANGLED_BRIDGE_IS_TRAVERSABLE = False against Maldacena-Susskind
       arXiv:1306.0533v2 -- was first recorded as pending because CHARTER.md
       reads 'asked of M and unanswered'.  That was stale: M had answered,
       "Record it (Recommended)", before DOCKET 68 opened, and it was applied
       the same day (emtension.py's ER_EPR_SOURCE, ER_EPR_SOURCE_STATUS,
       ER_EPR_FOOTNOTE_1 and their selftest checks).  CONVERTED to the ruling
       M-D68-C12 (not C9, which is the charter's carried H-IT instruction),
       its owner values asked of emtension and its first text kept as history
       (D68_P1_AS_FIRST_RECORDED).  The flag's value never moved.

NAMED LIMITATIONS OF THIS SEATING.
  H-LEDGER-ASKS-REPRESENTATIVES: the board asks the variants D68_VARIANTS
    names, at combine's 1 ly, N = 7 and 1 AU, N = 7 cells.  The census over
    every variant (at most one member-attributed removal per account, always
    O-BITS; O-SEAT and O-MAKE-DIST removed by no member anywhere) is
    combine.py's full screen (B-combine.md section 3), which this file does
    not re-run; it is cited there and not printed here as asked.
  WHAT IS CHECKED: every number and support index3.py's DOCKET 68 rows type
    is checked against its owner (d68_index3_faults); their qualitative
    claims (at most one member removal in any consistent account; O-SEAT
    and O-MAKE-DIST removed by no member; the D-CTC route's pairs at most 1;
    N_CORR's clash with N_QTOPO) are cited from their owners, not checked.
  H-LEDGER-DEPS: the docket68 owners bring z3-solver (pip, not vendored),
    numpy and scipy into this file's import, which until DOCKET 68 needed
    only the stdlib and its stdlib peers.  Without them the import fails;
    nothing is skipped silently.
  The paper (paper/CLAIMS.md) was NOT edited by DOCKET 68's seating.  The
    non-edit is M's rule for the paper (M_PAPER_RULE_WORDS: a finding must
    change existing paper text), not M-D68-9, whose 'Wait' concerns the
    separate Q-1s paper session; what DOCKET 68 bears on in the paper is
    reported for M, and applied only on M's ruling.  ADDED: on items 12 and
    13 (M-D68-12, M-D68-13) the lead corrected CLAIMS.md 4647-4648 and scoped
    H62d, each under the head '(Corrected on M's "<M's words>", DOCKET 68:'
    (PAPER_D68_MARKER_HEAD_RE, read as DOCKET 67's are); the census
    (paper_docket_markers) READs them like the others.  One DOCKET 67 correction the DOCKET 67 pass missed --
    H62e's opening sentence, which predates the midpoint-source correction
    D23 carries -- is made under M's DOCKET 67 ruling "Repair all", with the
    paper's DOCKET 67 marker; it is DOCKET 67's, and the paper-marker census
    (paper_docket_markers) READs it like the others.

===============================================================================
7b.  DOCKET 68, WAVE 2, AS SEATED
===============================================================================

M's order (M-D68-10) put D68 wave 2 second: the Weinberg-family limits read
at source, vacuum entanglement as pair supply, the S5 seat route.  Wave 2
ran, was verified both ways (W2V-0 against overstatement, W2V-1 against
understatement; no grade moved either way) and its fixes landed (W2-fix).
This is its seating, in wave 1's form; section 7 is wave 1's record and is
kept as written.  The owners are settle.py (W2A-limits), vacuum.py
(W2B-vacuum), seat.py (W2C-seat) and combine.py (W2-combine); every value is
ASKED of them at run time, and wave 1's words, where wave 2 replaced them,
are kept in the same cell and re-derived as AS-OF CONTROLS.

  O9   still OPEN; no grade moved.  Its cell now reports support 1 of W2 x F1
       (N_EPS) on the READ (abstract) limits, cell by cell, from
       settle.window_read: EXCLUDED given W_W2R at 1 AU, N = 7 and at 1 AU,
       N = 1e3 (whose reading A also needs H-SAME-EPS -- one READ limit alone
       opens it); ADMISSIBLE given W_W2R -- not excluded, not found -- at the
       other seven.  combine's exact-rational window is checked against
       settle's at its four screened cells, and combine's support-1 route
       alone is asked at 1 AU.  The 1 AU headline does not move: support 2
       (N_W2ANC, UNEVALUATED) carries it.  O-MAKE-DIST is vacuum.py's grade --
       LEFT-IF its nine hypotheses, OPEN outside them via N_NLDIST, N_W2WEAK
       and N_VACNP, none computed -- as combine screens it, with the named
       reading H-VAC-LEFTIF beside it.  O-SEAT stays OPEN via N_S5;
       seat.grade_o_seat agrees, and the gate's binder is measured in no
       Proxima-system star or body in the sources read.  Wave 1's 1 AU and
       O-MAKE-DIST words are re-derived from combine's history encodings
       (wave6-WREAD, wave6-NVAC) and settle.window_given.  O9's answer names
       what wave 2 left open and keeps wave 1's answer after it.
  D23, D25, S5  their notes carry vacuum.py's (D23) and seat.py's (D25, S5)
       asked values; D23 keeps wave 1's words after them.  No status moved.
  RULED_BY_M  + M-D68-15 and M-D68-16 (items 15-16, the retrieval route).
       Item 15 (corpus instruments) is SUPERSEDED by item 16 (the session's
       web-retrieval connectors, Firecrawl beside alphaXiv, open content only,
       route recorded) and kept as history; what 16 applied is the routes the
       owners record, asked (d68_w2_routes).  M-D68-10's cell says wave 2 ran
       and keeps wave 1's NOT YET RUN after it.
  index3.py  no row added and no cell moved: wave 2 moved no grade a row
       reads.  D68-ONE-MEMBER-REMOVAL-AND-IT-IS-CONDITIONAL's support-1
       sentence is re-typed on the READ windows (its wave-1 text kept as
       index3.D68_TEXT_AS_WAVE1); the O-SEAT row gains seat.py's binder; the
       needles (d68_index3_needles) ask the new values.

NAMED LIMITATIONS OF THIS SEATING (wave 2), beside section 7's.
  H-LEDGER-ASKS-REPRESENTATIVES grows: vacuum.compact_boundary (about 44 s;
    the family-specific window bound) and combine's full screen and selftest
    (about 40 minutes) are their owners' runs, cited and not re-run here.  The
    window-free floor, the harvested pair's figures, the windows and seat.py's
    grade are cheap and asked.
  H-NO-VACUUM-ROW: whether the vacuum route's computed floor and pair figures
    earn an index3 row of their own (a requirement stated in numbers could
    read Z = +1) is NOT decided here.  They are carried on O9 and the D23
    note, and the question is reported for M.
  RECORDED, NOT REPAIRED: seat.py's binder figure (on stock.HUMAN) and
    stockgate's D25 figure (on the 'as-composed 59' payload) differ in the
    fifth figure; element and four-figure value agree, so D25's note names
    the element and leaves the figure to the row's claim (printed once).
  Not edited by this seating: paper/CLAIMS.md (M's rule for the paper) and
    the wave-2 owners themselves.

===============================================================================
8.  DOCKET 66, WAVE 1, AS SEATED
===============================================================================

M's order (M-D68-10, "1 then 2 then 3 then 4") put DOCKET 66 fourth: seating
at topological defects, with Quantum Energy Teleportation folded in (M-D65-1).
Its charter (docket66/CHARTER.md) carries three of M's hypotheses, AS
HYPOTHESES and never as results: H-DEFECT-SEAT (M-S1A-P3 (ii)), H-THROAT-BITS
(M-S1A-P3 (i) with M's clarification) and H-QET-EXOTIC (M-D65-1).  Wave 1 ran
(A1 defects.py, A2 throatbits.py, A3 qet.py, B combine66.py), was verified
three ways (V66-0 against M, V66-1 for M, V66-2 reproduce) and its fixes landed
(D66-fix, every verifier problem applied or answered, each owner keeping D66
wave 1's words as history).  This is its seating, in DOCKET 68's form.  Every
value is ASKED of the docket66/ owners at run time: combine66.D66Screen for
every verdict (inside combine66.vocabulary, which extends combine.py's
vocabulary in process only and restores it on exit -- checked); defects.py,
throatbits.py and qet.py for every figure; B-combine66.md READ for every
figure of combine66's own runs, which this file does not repeat.

  O9   still OPEN; no grade moved.  Its cell now carries a DOCKET 66 part
       after DOCKET 68's (D66_O9_PART; DOCKET 68's cell, o9_claim(), is kept
       exactly): member-attributed first -- no D66 literal is load-bearing in
       any removal or non-binding (combine66.d66_attributed, on the variants
       asked; B-combine66.md READ for the full screen); the only member
       removal stays D68's O-BITS by W2 x F1; R-LIT (the question's
       parenthetical read as arrival alone) inconsistent alone and, with W2,
       inside a support only by entailing W2.  Then what the D66 readings ADD:
       OPEN pathways, none a removal -- on O-SEAT N_DEFB (its READ direction
       wash-out), on O-HOLD N_NEGT, N_PINCH, N_GJWPAY and N_QETHAD, on
       O-MAKE-TOPO N_WNCC under M's ruling M-S1A-P3 applied; the interference
       (a D66 throat beside ITB undoes ITB's non-bindings); the defeasibility
       (only through a held string-supported throat, FKZ); the seat condition
       M-S1A-P3 (i) per reading (VIOLATED in none).  O9's answer gains what
       would answer the D66 pathways (D66_O9_ANSWER).  O9's closing is asked
       over DOCKET 68's and DOCKET 66's variants (o9_removed_outright).
  S5, S13  each carries a DOCKET 66 NOTE after its DOCKET 68 note, asked, NO
       status change: S5 the O-SEAT pathways a defect seat or QET adds (N_DEFB
       beside N_S5; QET no supply of substance; the defect seats pass
       M-S1A-P3 (i)); S13 the defect-core link (A1's answer item 7; the ground
       of TEMPLATE's refusal moves from P-UNIFORM to topology, the grade does
       not, and O-SEAT does not move).
  RULED_BY_M  no new ruling at this seating: M had ruled nothing in DOCKET 66
       (as first written; M has since ruled items 26-28 of the rulings file,
       seated as M-D68-26..28 -- section 8b).  M-S1A-P3's
       unblocks cell said "DOCKET 66 opens"; it now says what ran
       (d66_p3_ran), the first wording kept before it, and the cell must EQUAL
       that (p3_unblocks_faults).  M-D65-1's ruling cell said "QET is to be
       tested inside DOCKET 66 (NOT YET RUN)"; it is now M_D65_1_RULING_T
       filled from the constants and what DOCKET 66 ran (d66_m_d65_1_ran: the
       literature READ by qet.py, item by item from its own sources; the
       parenthetical INEXACT; R-QET and R-LIT as qet.grades reads them), the
       first wording kept inside it as FIRST APPLIED, and m_d65_1_faults
       requires EQUALITY, refuses NOT YET RUN outside the history, and refuses
       any source printed as READ that qet.py does not head an entry with.
       [2026-10-05: M-D65-3's unblocks cell still said "DOCKET 67, NOT YET
       RUN", though DOCKET 67 closed on 2026-10-03.  It now keeps that wording
       and follows it with what ran, READ from docket67-raw/CLOSE.md (d67_ran:
       its head and section headings, nothing typed), and must EQUAL that
       (m_d65_3_unblocks_faults).]
       Its unblocks cell likewise; its `why` keeps the question as it stood.
       M-D68-10's cell says step (4) ran (and step (3)'s comments are written,
       kept as drafts), keeping the wave-2 seat's and wave 1's NOT YET RUN.
  THE TURN QUESTION, FOR M (as this seating carried it; RULED since -- M:
       "Any crossing", M-D68-27, section 8b; the paragraph is kept as
       written): spec.py's 'TURN' -- a conjugate point
       (H-TURN-CONJUGATE) or any crossing (H-TURN-CROSSING)?  A1's question
       for M since D66 wave 1, still M's to rule after D66-fix, which leaves it
       deciding the straight string alone; its values asked of defects.py
       (d66_turn_question).  Carried in O9's DOCKET 66 answer and NOT on
       PENDING_RULINGS: specthm.py's selftest pins ledger.pending_rulings()
       empty, and specthm.py is not edited by this seating (no class verdict
       moved) -- seating it as pending needs specthm's PENDING FOR M updated
       first; reported.
  QUOTATIONS  docket66/CHARTER.md says every quotation of M in it is taken
       from this file: d66_charter_quote_faults checks each of its quoted spans
       verbatim against the constant that holds it, and d66_quote_faults
       requires every quotation in a DOCKET 66 cell here to be M's words held
       or docket66/'s own words.
  RECORDED FOR THE D68 BOARD, NOT REPAIRED (as this seating first wrote it;
       REPAIRED since on M's ruling, M-D68-28, section 8b): read as a board
       ruling reaching D68's own throats (combine66's reading singok-board),
       M-S1A-P3 moves combine.py's O-MAKE-TOPO from LEFT to OPEN via N_WNCC
       where a throat is merely possible -- in combine66's census 174
       variants, 20 of them context-only (B-combine66.md; the contexts, READ
       from docket68/B-combine.md section 0: the board alone, RQ, ITJ, SHAPE
       and W2 x F1, alone and combined, and ITB with RQ).  This board asks
       two of the 20, the board alone and RQ; the other 18 are READ, not
       asked.  CORRECTED (R-seat, from D66-repro's FIX-SEAT-RESULT result.v):
       first written '(the board alone, RQ; 20 context-only variants in
       combine66's census)', which read as if the 20 were those two.
       combine66 cannot change D68 rows (its conservative-extension rule) and
       combine.py was not edited by this seating: O9 printed both, and the
       re-grade was for M and the D68 owners.  CORRECTED (D66-RULINGS
       verifier, 2026-10-05; the paragraph above is kept as first written):
       'where a throat is merely possible' is wrong for combine.py.  In those
       20 context variants a geometric throat is FORCED by the board --
       B-THROAT: Not(THROAT) == NONGEO, and NONGEO needs ITB's premise -- so
       read 'a throat forced by the board (no D66 throat literal present)'.

NAMED LIMITATIONS OF THIS SEATING (DOCKET 66), beside sections 7's and 7b's.
  H-LEDGER-ASKS-REPRESENTATIVES grows: combine66's full screen (3,528 + 1,764
    variants, about 16 minutes with its selftest) and its --conservative-full run
    (8,192 compared, about 29 minutes), and the A-instruments' selftests, are
    their owners' runs, READ from B-combine66.md or cited, never re-run here.
    The board asks D66_VARIANTS (24 at 1 ly) and D66_VARIANTS_AU (2 at 1 AU)
    and five readings; the census (0 load-bearing D66 literals in 2,492 and
    1,332 consistent variants) is READ.
  H-QET-SPEC-PLACEHOLDER: qet.grades needs specthm's class verdicts (about
    45 s of z3) only for its seat-class sentence; this file reads its
    own-content verdicts and per-obstruction heads, passes a placeholder, and
    the selftest re-asks with a second placeholder and requires those fields
    unchanged.  throatbits.grades (which needs them throughout) is not asked;
    its figures are (capacity_table_base, mmp_scales).
  H-NO-D66-ROW (a named reading, not a fact): index3.py gains no row.  Read
    this way, DOCKET 66's answer is (0, 0, 0) in the house reading -- it
    removes nothing (Y = 0, asked: no D66 literal load-bearing in any removal
    or non-binding) and identifies no warp energy (X = 0); Z = 0 is the
    reading itself, which counts as "its own" only a requirement on a route
    the docket shows, and a null cell is not a finding.  Its owners DO state
    requirements in numbers -- A2's throat at the A/4 ceiling (r_fit and
    M_sat, IF {H-CAP-AT-THROAT, H-NECK-DOGMA, H-COUNT-IS-ENTROPY}; no encoding
    at that density constructed or READ), A3's QET injection bound, MMP's N_f
    -- each a price of an OPEN or LEFT route.  They are kept on O9 and S5's
    note by M's precedent for the vacuum route (M-RULINGS-2026-10-03.md item
    18, "No, keep on O9 (Recommended)") -- a precedent, not a ruling on DOCKET
    66 -- and whether any earns a row (which could read Z = +1) is put to M;
    no cell moves unless M rules.  d66_index3_faults checks that no index3.py
    row cites docket66/.  CORRECTED (R-seat, from D66-repro's FIX-SEAT-RESULT
    result.v): first written 'states no requirement in numbers of its own
    (Z = 0)' as a fact, followed by the requirements its owners state in
    numbers -- two sentences that contradicted each other.
  H-LEDGER-DEPS grows: docket66/'s owners need z3, numpy and scipy, and use
    sympy at call time.  Without them the import fails; nothing is skipped
    silently.
  Not edited by this seating: paper/CLAIMS.md (M's rule for the paper:
    what DOCKET 66 bears on there is reported for M), specthm.py (no class
    verdict moved: A1's gauge monopole joins S-1, already NONEMPTY), the
    docket66/ owners, docket68/combine.py.

===============================================================================
8b.  M'S DOCKET 66 RULINGS (M-RULINGS-2026-10-03.md items 26-28), AS SEATED
===============================================================================

M ruled three DOCKET 66 questions on 2026-10-04; the rulings file holds them
verbatim (items 26-28).  The paper's correction was applied by the lead
(paper/CLAIMS.md, under a DOCKET 66 head); items 27 and 28 by R-apply, in
docket66/defects.py and spec.py's PART 2 note (27) and docket68/combine.py
(28).  This is their seating, in DOCKET 68's form; every value is ASKED of its
owner at run time.

  RULED_BY_M  + M-D68-26, M-D68-27, M-D68-28, appended to D68_RULED (the ids
       follow the item number, as M-D68-12..16 do; specthm places D68_RULED's
       rows, so no specthm edit is needed to place them).  M's words held in
       D68_M_WORDS and checked against the rulings file;
       the question and the file's own 'applied' sentence held in
       D66_RULING_QUESTIONS and D66_RULING_CARRIED (the file's words, NOT
       M's) and checked the same way (D68_INLINE_QUOTES).
       M-D68-26 ("Correct it (Recommended)"): what was applied is the paper's
       marked line, READ back by paper_d66_marker() from M's words in its
       DOCKET 66 head (PAPER_D66_MARKER_HEAD_RE, read as DOCKET 67's and 68's
       are), never typed; the paper's figures are compared with defects.py's
       (gott_gamma_needed at the Planck bounds) and its first wording with
       item 26's, number by number.  No board status moves.
       M-D68-27 ("Any crossing"): H-TURN-CROSSING adopted, H-TURN-CONJUGATE
       kept as the alternative on record (defects.TURN_RULING, asked); the
       straight string TURNs at a computed range (defects.string_turn).  The
       question O9's DOCKET 66 answer carried for M since D66 wave 1 is kept
       there and in the row as FIRST RECORDED (d66_turn_question, history).
       No specthm class verdict moves: its seat classes are defined by the
       literals wl and ball (specthm_seat_class_literals, READ from source:
       specthm imports this file), so specthm.py is not edited.
       M-D68-28 ("Re-grade D68 (Recommended)"): combine.py's O-MAKE-TOPO reads
       OPEN via N_WNCC where a geometric throat is possible -- asked on the
       board alone, RQ, ITJ, ITB and ITB with RQ -- never removed; D68 wave
       2's LEFT kept as combine's history mutation d68w2-topo, asked; the
       census over every variant READ from docket68/B-combine.md section 0
       (D68_TOPO_CENSUS), combine66's side READ from B-combine66.md
       (D66_TOPO_READ).  STATED EXACTLY (D66-RULINGS verifier, 2026-10-05;
       'where a geometric throat is possible' kept as first written): the
       3,840 / 960 verdict moves (LEFT -> OPEN via N_WNCC) are exactly the
       variants where Geroch/Tipler bind -- the predicate is NEITHER ITE NOR
       ITB-WITHOUT-RQ (3,840 + 1,920 at 1 ly with the board alone, 960 + 192
       at 1 AU, no exception).  ITE variants also hold a forced geometric
       throat but read NOT-BOUND-IF {ITE; N_MS17}, and ITB-without-RQ
       variants NOT-BOUND-IF {ITB; N_QTOPO}; in both the removal moves OPEN
       via N_ILFREE -> OPEN via N_ILFREE, N_WNCC, a via-list move.  Of the
       five variants this board asks, ITB is such a via-list move; the board
       alone, RQ, ITJ and ITB with RQ are verdict moves.
  O9   still OPEN; no grade moved.  DOCKET 68's answer gains the re-graded
       O-MAKE-TOPO and the adopted TURN reading (asked); DOCKET 66's part
       says the D68 board is re-graded, with section 8's 'RECORDED FOR THE
       D68 BOARD, NOT REPAIRED' kept after it as FIRST SAID (its combine.py
       verdicts re-asked of d68w2-topo); DOCKET 66's answer says the TURN
       reading is ruled, the question kept after it.
  THE PAPER-MARKER CENSUS  paper_docket_markers() READs the DOCKET 66 token at
       the corrected line as naming M's ruling (M's quoted words before the
       token); the selftest ties that to PAPER_D66_MARKER_HEAD_RE, as for
       DOCKET 67 and 68, with a control that strips M's words in a private
       copy of the paper.
  QUOTATIONS  CORRECTED (R-seat, from D66-repro's FIX-SEAT-RESULT result.v):
       'with M's throat-compression mechanism' is the ledger's wording in the
       M-S1A-P3 cell; the charter now attributes it to the ledger
       (d66_charter_attribution_faults READs that), d66_charter_quote_faults
       still checks it verbatim, and d66_quote_faults no longer accepts it as
       M's words (D66_CHARTER_LEDGER_WORDS).  First held among M's
       quotations, labelled '(the ledger's words)'.
  index3.py  no row added and no cell moved; the comment above
       FINDINGS_AS_OF_DOCKET67_CLOSE states H-NO-D66-ROW as a reading (its
       first wording kept), as section 8 now does.
  Not edited by this seating: paper/CLAIMS.md (the lead applied item 26),
    specthm.py (no class verdict moved), the docket66/ and docket68/ owners.

===============================================================================
8c.  DOCKET 68 WAVE 3 AND STEP 1b, AS SEATED (M-RULINGS items 21-25, 29-36)
===============================================================================

M chose the corridor after Step 1b's first pass (item 34, "Corridor (D68
wave 3)"); wave 3 ran in docket68/wave3/ (corridor.py, criteria12.py,
seatrank.py, aperture.py; WAVE3.md) and Step 1b went on by necessity in
step1b/ (balance.py, compensate.py, openterms.py, bsupply.py, placement.py;
BALANCE.md).  Both were verified adversarially in both directions and
corrected, and M ruled the seating (item 36, "Seat both (Recommended)").  This
is that seating, in DOCKET 68's form; every value is ASKED of its owner at run
time (W3S1B_ASKED, about a second).

  THE OWNERS  loaded after M_NEUTRON_KG is defined, by _w3s1b_load():
       openterms.py imports this file, so when this file is __main__ it is
       lent to that import under its own name for the duration (no second
       load); wave 3's corridor.py shares its name with this directory's
       corridor.py, so it is loaded by path as 'w3corridor' and never
       registered as 'corridor'; sys.path is restored after the load.  The
       selftest checks all three.  Each owner's own copy of M's words is
       checked against the words held here (w3s1b_owner_words).
  RULED_BY_M  + M-D68-22, 24, 29, 30, 33, 34 and 36, appended to D68_RULED (the
       ids follow the item number).  Items 22 and 24 are M's answers of
       2026-10-04 on the corridor, held in the rulings file since then and
       first seated here, when wave 3 did their work: 22 carries the corridor
       as the A-B coupling (corridor.py); 24 is H-12Q (criteria12.py), with
       the sentence M added held as M-D68-24b and printed with the question.
       Items 29, 30 and 33 define Step 1b (balance.py); 34 opened wave 3; 36
       is this seating.
  D68_FILE_CARRIED  items 21, 23 and 25 (M's statements on speed and
       position, the twelve trajectories, and the ranking of seats, carried
       as tested readings and as H-SEATRANK), 31 (M's instruction on
       compensation, H-COMPENSATION), 32 (M's answer with "I suspect", carried
       as the hypothesis H-RETIRE-A, never a result) and 35 (M's question on
       the corridor's size, answered by aperture.py).  NOT on RULED_BY_M and
       not counted as rulings; kept apart from D68_CARRIED because the
       carrier is the rulings file, not the charter, and printed in their own
       LEDGER.md section.
  W3S1B_OPEN  thirteen items, seven from Step 1b and six from wave 3, as the
       owners' records state them, each with what would answer it.  Named,
       not ranked.
  O9 and the board  no status moves.  Wave 3's grade for O-BITS (REMOVED-IF
       one of H-DIRECT-COUPLING, H-LONG-RANGE with alpha < d, or unbounded J,
       with J > pi c/2L and H-STATE-AS-BITS, each speed-free route clashing
       with H-LOCALITY) is the owner's PROPOSAL and is not screened by
       combine.py, which this seating does not edit; it is printed in
       M-D68-22's cell as PROPOSED.  W3B, W3C, the corridor's size and
       Step 1b move no obstruction grade.

NAMED LIMITATIONS OF THIS SEATING (wave 3 and Step 1b).
  H-NO-W3S1B-ROW: no index3 row is added.  Nothing seated here moves a
    requirement or a grade a row reads, which is wave 2's precedent (section
    7b); whether Step 1b's equation or the corridor's size earns a row of its
    own is NOT decided here and is reported for M.
  H-LEDGER-ASKS-REPRESENTATIVES grows: the owners' selftests (balance 17,
    compensate 15, openterms 11, bsupply 8, placement 9, corridor 17,
    criteria12 14, seatrank 14, aperture 9) are their own runs, cited and not
    re-run here; the values the cells print are asked.
  The owners bring numpy (corridor, seatrank, criteria12), as wave 1's did
    (H-LEDGER-DEPS).
  Not edited by this seating: paper/CLAIMS.md (M's rule for the paper),
    docket68/combine.py (the O-BITS grade stays proposed), index3.py,
    specthm.py, and the wave-3 and Step 1b owners.

===============================================================================
8d.  STEP 1c, AS SEATED (M-RULINGS items 37-39)
===============================================================================

M ruled the order 1a, 1b, 1c (specthm.py section 0).  Step 1c -- the device --
ran in step1c/: demand.py (what each subsystem must deliver, read off the
balanced equation), supply.py (present supply READ at source, item 37: "All
three (Recommended)"), coupling.py (the wave-3 coupling as the link, item 38:
"Take the coupling route"), nonlocal.py and coherence.py (item 39: "3, then 2.
Then 1 last please" -- the non-local branch as M's hypothesis, then
H-COHERENCE, then this seating).  Each was verified adversarially in both
directions and corrected; first-written claims are kept in each file's
HISTORY and in step1c/DEVICE.md.  Every value is ASKED of its owner at run
time (S1C_ASKED).

  THE OWNERS  step1c's demand.py, supply.py and coupling.py share their names
       with modules in this directory, so all five are loaded BY PATH under
       private names (_s1c_load), never by the bare name, with the same lending
       and setting-aside as section 8c's load.  The selftest checks the bare
       names still answer to this directory's modules.
  RULED_BY_M  + M-D68-37, 38, 39, appended to D68_RULED.
  S1C_OPEN  eight items, each with what would answer it.  Named, not ranked.
  O9 and the board  no status moves.  WITHDRAWN on verification and kept as
       history in the owners: 'J <= pi c/2L' as a locality ceiling (locality
       bounds time, not J); 'a century is not excluded' for an instantaneous
       coupling; the formal 1/R^3 carry as the best direct coupling (the far
       field is (kL)^2 larger); 'H-MIDPOINT-SOURCE minimises the hold' (2x/c, 0
       at Alice).  Wave 3's proposed O-BITS grade is unchanged: its J > pi c/2L
       is the before-light condition of the instantaneous coupling it names.
       H-NONLOCAL-COUPLING is M's hypothesis, carried, neither shown nor
       dismissed.

NAMED LIMITATIONS OF THIS SEATING (Step 1c).
  H-NO-S1C-ROW: no index3 row is added; nothing seated here moves a
    requirement or a grade a row reads (wave 2's precedent, section 7b).
  The supply figures were read by this session's readers; the ones the gaps
    rest on were re-read by the lead (Sturm, the DSOC release, Barredo,
    Vienna's geometry, Saeedi).  The rest carry the reader's or the
    verifier's route.
  Not edited by this seating: paper/CLAIMS.md, docket68/combine.py,
    index3.py, specthm.py, and the step1c, wave-3 and Step 1b owners.

===============================================================================
8e.  DOCKET 68 WAVE 4 AND ITS CLOSE (M-RULINGS item 40), AS SEATED
===============================================================================

M chose a wave 4 first, then the close and the Q-1s gate (item 40, "2 then 1
please").  Wave 4 priced what Step 1c left OPEN: the transmitted power at the
floor quantum (docket68/wave4/linkbudget.py, S1C-O8) and a fault-tolerant
memory on measured surface-code figures (docket68/wave4/ftmemory.py,
H-FT-MEMORY); both were verified in both directions and corrected
(docket68/wave4/WAVE4.md).  DOCKET 68's close record is docket68/CLOSE.md:
its answer is NOT FOUND, NOT EXCLUDED -- O9 stays OPEN -- and its section
headings are READ by d68_close_sections(), never typed.

  THE OWNERS  loaded BY PATH as 'w4_<name>' (_w4_load), with section 8d's
       lending and setting-aside; every 's1c_*' key they add is removed after.
  RULED_BY_M  + M-D68-40.
  W4_OPEN  six items, each with what would answer it.
  The board  no status moves; O9 stays OPEN.  H-NO-W4-ROW: no index3 row.
  The paper  not edited.  The Q-1s prior-art gate (M-D68-11's condition,
       M-D68-C8b's instruction) runs next; no paper session starts before M
       sees its result.

===============================================================================
8f.  THE Q-1s GATE, AND H-CMB-CORRIDOR READING 1 (M-RULINGS items 41-45), AS
     SEATED
===============================================================================

After DOCKET 68's close M asked whether the universe's background radiation
could construct the corridor (item 41, carried as H-CMB-CORRIDOR and
H-CMB-UNIVERSAL), and ordered the Q-1s gate first, then the CMB as the frame
(item 42, "3, then 1").  The gate (docket68/Q1s-PRIORART.md, its section
headings READ by q1s_gate_sections()) found not every item of the brief
published; M ruled no paper (item 43).  M's instruction that the physics of
the frame is what matters (item 44) is carried.  Reading 1
(docket68/cmb/cmbframe.py, CMB.md), verified once in both directions and
corrected, takes the background's rest frame as H-FRAME's frame; M ruled it
seated, then the medium reading (item 45).

  THE OWNER  loaded BY PATH as 'cmb_cmbframe' (_cmb_load), with section 8d's
       lending and setting-aside; every 's1c_*' and 'cmb_frame' key it adds is
       removed after.
  RULED_BY_M  + M-D68-42, 43 and 45.  D68_FILE_CARRIED + M-D68-41 (a question
       carrying two hypotheses) and M-D68-44 (an instruction).
  CMB_OPEN  four items, each with what would answer it.
  The board  no status moves; O9 stays OPEN.  H-NO-CMB-ROW: no index3 row.
  The paper  not edited; no Q-1s paper is written (M-D68-43).

===============================================================================
8g.  H-CMB-CORRIDOR READINGS 2 AND 3, AND THE LOCAL CLOCKS (M-RULINGS items
     46-54), AS SEATED
===============================================================================

During reading 2 M asked what a contracting universe would do (item 46,
carried as H-CONTRACT) and ordered its status READ, then folded into the
medium reading (item 47, "2, then 1").  M then carried the coupled medium as
the unobserved ground state (item 48, H-UNOBSERVED-MEDIUM), two kinds of
observer (item 49, H-TWO-OBSERVERS, with "1": READ, then model), conscious
selection (item 50, H-CONSCIOUS-SELECTS), many perspectives (item 51,
H-MANY-PERSPECTIVES, with "3": READ, then model) and a local clock (item 52,
H-LOCAL-CLOCK; item 53, "READ, then model").  Reading 2
(docket68/cmb/medium.py, MEDIUM.md), the observation model
(docket68/cmb/unobserved.py, UNOBSERVED.md, rebuilt twice against two
verifications) and the local clocks (docket68/cmb/localclock.py,
LOCALCLOCK.md, verified once) are seated on M's "3, then 2, then 1 please"
(item 54), after M-SUPPORT's dynamics (support.py) and reading (b)'s pricing
(bias.py) were built and verified -- those two are NOT seated here.

  THE OWNERS  loaded BY PATH as 'cmb_medium', 'cmb_unobserved' and
       'cmb_localclock' (_cmb2_load), with section 8d's lending; every module
       key the load adds is removed after, and any it would displace is
       restored.
  RULED_BY_M  + M-D68-47, 49, 51, 53 and 54.  D68_FILE_CARRIED + M-D68-46 (a
       question carrying a hypothesis), 48, 50 and 52 (statements carrying
       hypotheses).
  CMB2_OPEN  six items, each with what would answer it.
  The board  no status moves; O9 stays OPEN.  H-NO-CMB-ROW: no index3 row.
  The paper  not edited.

===============================================================================
8h.  M-SUPPORT'S DYNAMICS AND READING (b)'S PRICE (M-RULINGS item 55), AS
     SEATED
===============================================================================

Item 54's steps 3 and 2 built docket68/cmb/support.py (SUPPORT.md: on
H-SUPPORT-IS-RECORDS, the clock's support as matter's Thomson records of the
light) and docket68/cmb/bias.py (BIAS.md: H-CONSCIOUS-SELECTS reading (b) at
the READ intention-bias sizes), each verified once and corrected.  M ruled
both seated (item 55, "Seat both").

  THE OWNERS  loaded BY PATH as 'cmb_support' and 'cmb_bias' (_cmb3_load),
       with the same lending and key restoration as _cmb2_load.
  RULED_BY_M  + M-D68-55.
  CMB3_OPEN  five items, each with what would answer it; CMB2-O2 and CMB2-O4
       now point at the seated owners.
  The board  no status moves; O9 stays OPEN.  H-NO-CMB-ROW: no index3 row.
  The paper  not edited.
"""

import contextlib
import io
import math
import os
import re
import sys
import textwrap

import achievable
import address
import bounds
import branelink
import candidates
import certify
import create
import driven
import drivensource
import endpoint
import excite
import fewsterteo
import fluctuation
import foliation
import formation
import higgs
import hpscentre
import latticectc
import linstab
import massform          # DOCKET 65; it asks THIS file only at call time
import noise
import nonstatic
import overturn
import phase1
import qeihps
import stockgate
import throatmass
import tolman
import transit
import warpfolder

# DOCKET 68's owners sit in docket68/ and import their own peers; they are
# imported here with their printing swallowed, AFTER every peer above, so the
# paths they add cannot shadow one (no docket68/ or tools/ module shares a
# name with a module here -- checked when this was seated).  They bring z3,
# numpy and scipy (H-LEDGER-DEPS, docstring section 7).
D68_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docket68")
if D68_DIR not in sys.path:
    sys.path.append(D68_DIR)
with contextlib.redirect_stdout(io.StringIO()):
    import combine           # DOCKET 68: the seven hypotheses in combination
    import frame             # DOCKET 68: H-FRAME (A2)
    import measure           # DOCKET 68: Q-1 (A3)
    import settle            # DOCKET 68: H-SETTLE (A1)
    import signed            # DOCKET 68: Q-1s
    # DOCKET 68 wave 2 (docstring section 7b): the vacuum route (W2B) and the
    # S5 seat route (W2C).  Both insert docket68/ at the FRONT of sys.path;
    # no docket68/ module shares a name with a module here or in tools/
    # (re-checked when wave 2 was seated), so nothing is shadowed.
    import seat              # DOCKET 68 wave 2: W2C-seat
    import vacuum            # DOCKET 68 wave 2: W2B-vacuum

# DOCKET 66's owners sit in docket66/ (docstring section 8), imported AFTER
# docket68/'s because combine66.py runs docket68/combine.py's engine; no
# docket66/ module (combine66, defects, qet, throatbits) shares a name with a
# module here, in docket68/ or in tools/ (checked when this was seated).  They
# import THIS file only at call time (their M-S1A-P3 / M-D65-1 reads), never
# while it is being imported, so nothing below calls those functions.
D66_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docket66")
if D66_DIR not in sys.path:
    sys.path.append(D66_DIR)
with contextlib.redirect_stdout(io.StringIO()):
    import combine66         # DOCKET 66: the three hypotheses in combination (B)
    import defects           # DOCKET 66: H-DEFECT-SEAT (A1)
    import qet               # DOCKET 66: H-QET-EXOTIC (A3)
    import throatbits        # DOCKET 66: H-THROAT-BITS (A2)

#: LEDGER.md sits beside this file, and is found there from ANY working
#: directory.  It was first resolved against the cwd, so --check run from the
#: repository root reported a tracked file missing.
HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER_MD = os.path.join(HERE, "LEDGER.md")

THEOREM, MEASURED, SURVEY, OPEN, WITHDRAWN, REFUSED = (
    "THEOREM", "MEASURED", "SURVEY", "OPEN", "WITHDRAWN", "REFUSED")

#: A THEOREM whose SCOPE was stated wider than it was proved.  The theorem
#: stands; what was wrong was the class it was applied to.  DOCKET 61 needed
#: this and the five statuses had nowhere to put it: WITHDRAWN says the claim
#: fell, and it did not.
NARROWED = "THEOREM-NARROWED"

STATUSES = (THEOREM, NARROWED, MEASURED, SURVEY, OPEN, WITHDRAWN, REFUSED)

# CONSTANTS ASKED, NEVER RETYPED.  Each is read from the module that owns it so
# that a peer moving underneath this file is a --check failure rather than a
# stale sentence.
C_LIGHT = foliation.C_LIGHT                  # m/s,  exact by definition
G_NEWTON = foliation.G_NEWTON                # m^3 kg^-1 s^-2, CODATA 2018
M_SUN = foliation.M_SUN                      # kg,   IAU nominal
PROXIMA_LY = foliation.PROXIMA_LY            # ly,   Gaia DR3 parallax
#   CORRECTED (DOCKET 67): epoch J2016.0, barycentric, raw parallax (no
#   zero-point), formal sigma +-0.00028 ly -- so about 4 significant figures;
#   by 2026.74 Proxima's approach puts it at 4.24566 ly (DOCKET 67, computed).
LAMBDA = overturn.LAMBDA                     # the method equation's coefficient
LY_M = 9.4607304725808e15                    # m per light year, exact (IAU)


def casimir_sheet_ratio(spacing_m, site_mass_kg):
    """S2's note and B4's supply: the continuum bound |E_Cas|/(M c^2) <=
    pi^2 hbar/(1440 d m c), gap = site spacing d, site mass m -- DOCKET 67's
    recovered construction (H-CONTINUUM, H-GAP-GE-SPACING, H-PASSIVE,
    H-PLANAR-INFINITE, H-T0).  hbar and c asked of address.py."""
    return math.pi ** 2 * address.HBAR / (1440.0 * spacing_m * site_mass_kg * address.C)


#: CORRECTED (DOCKET 67 follow-ups, residue pass; M: "address/correct/repair all
#: figures").  The nuclear-density entry was TYPED 7.43e-4: the bound at n0 =
#: 0.1375 fm^-3 (the tree's recalled 2.3e17 kg/m^3) with site mass m_n.  The
#: tree's one nuclear density is now address.RHO_NUCLEAR (n0 = 0.16 fm^-3 x m_p,
#: DERIVED-FROM-ORDER), so the entry is COMPUTED from it, site mass m_p as
#: address takes m_N: 7.83e-4.  Still below 1 -- the refusal does not move.
M_PROTON_KG = address.M_P_MEV * 1.0e-3 * address.GEV_IN_J / address.C ** 2
NUCLEAR_SHEET_RATIO = casimir_sheet_ratio(
    (M_PROTON_KG / address.RHO_NUCLEAR) ** (1.0 / 3.0), M_PROTON_KG)
NUCLEAR_SHEET_RATIO_TEXT = ("%.2e" % NUCLEAR_SHEET_RATIO).replace("e-0", "e-")
#: as first written; still checked as a RECORD (n0 = 0.1375 fm^-3, site mass m_n)
NUCLEAR_SHEET_RATIO_AS_FIRST_WRITTEN = 7.43e-4
N0_RECALLED_PER_M3 = 0.1375e45
M_NEUTRON_KG = 1.67492749804e-27             # CODATA 2018; used by the RECORD only

#: kg of negative enclosed Misner-Sharp mass per metre of contraction.
#: DERIVED here from two asked constants and nothing else; the figure the tree
#: quotes is 1.348948e26 and the selftest checks this against it.
EXCHANGE_RATE = C_LIGHT ** 2 / (G_NEWTON * LAMBDA)

PROXIMA_M = PROXIMA_LY * LY_M


def required_negative_mass(delta_d_m):
    """kg of negative enclosed mass to contract proper distance by delta_d_m.

    The method equation read the one way it is ever used here.  ASKED, not
    derived: LAMBDA is overturn.py's and the exchange rate is the two constants
    above.  Nothing in this function is this file's own physics.
    """
    return EXCHANGE_RATE * delta_d_m


# ---------------------------------------------------------------------------
# LEFT SIDE -- THE DEMAND.  (row id, claim, status, owner, what would move it)
#
# `owner` names a module and an attribute wherever the claim is pinned as one,
# so `ask()` can fetch it.  Where the owner is a paper rather than a module the
# attribute is None and the row is CITED in its note instead -- those rows are
# counted separately and the selftest says how many there are, because a row
# this file cannot ask is a row this file cannot defend.
# ---------------------------------------------------------------------------

DEMAND = [
    ("D1",
     "Contraction at r requires negative enclosed Misner-Sharp mass, "
     "ansatz-free, in any STATIC spherically symmetric spacetime -- in GR, "
     "wherever the areal radius is a radial coordinate (not where dr = 0 on "
     "the slice, as at a throat); reading m as the enclosed energy of matter "
     "also needs Lambda = 0 (CORRECTED, DOCKET 67: these were unstated)",
     THEOREM, ("certify", "THEOREM_SCOPE"),
     "a failure of staticity or sphericity -- and D2 removes the first"),

    ("D2",
     "Gamma > 1 in EVERY foliation <=> m < 0.  The RANGE THEOREM: over all "
     "foliations Gamma takes exactly [sqrt(1-2m/R), infinity), so the LOCAL "
     "criterion is gauge and staticity is DELETED rather than weakened",
     THEOREM, ("foliation", "IDENTITY_DISPUTED"),
     "nothing in 4D spherical symmetry; 16 z3 obligations, all unsat"),

    ("D3",
     "The local criterion alone is NOT a scalar, so 'contraction' read off one "
     "slice is a statement about the foliation and not about the spacetime",
     THEOREM, ("driven", "CONTRACTION_IS_A_SCALAR"),
     "nothing; it is the content of D2 read from the other side"),

    ("D4",
     "certify.py's COROLLARY -- and therefore negative enclosed ENERGY -- needs "
     "a REGULAR CENTRE, m(0) = 0.  Reissner-Nordstrom is a counterexample "
     "inside the file's own stated scope, and the integration constant a "
     "regular centre kills IS the central mass",
     THEOREM, ("drivensource", "CERTIFY_COROLLARY"),
     "nothing; it is a hypothesis that was always in force and was unwritten"),

    ("D5",
     "Superluminal travel requires negative energies, with NO staticity, NO "
     "symmetry and NO sphericity, pointwise on the path travelled.  "
     "'Superluminal' is Olum's Condition 1 -- the path reaches B earlier "
     "than every NEIGHBOURING path in the same spacetime, with no reference "
     "geometry -- and the theorem also assumes the generic condition on the "
     "path and Einstein's equations in a classical smooth 4-D geometry; its "
     "proof gives NEC violation on the path, stronger than the stated WEC "
     "(CORRECTED, DOCKET 67: Condition 1 and the generic condition were "
     "dropped).  A 'lead' against a reference geometry is not Condition 1",
     THEOREM, None,
     "nothing read this pass; Olum PRL 81 3567, CITED"),

    ("D6",
     "There are NO purely spatially averaged quantum inequalities over bounded "
     "regions in 4D Minkowski.  The ball integral at an INSTANT is unbounded "
     "below, so THE MAGNITUDE AXIS CARRIES NO NO-GO.  CORRECTED (DOCKET 67): "
     "proved for the massless minimally coupled free scalar, against bounds "
     "UNIFORM over states, as the UV cutoff Lambda -> infinity (the divergence "
     "is logarithmic in Lambda), at leading order in an asymptotic "
     "derivation.  One field suffices to refute a universal, matter-"
     "independent spatial bound, which is the use made here; a field-"
     "specific or state-dependent spatial bound is not addressed",
     THEOREM, None,
     "nothing; Ford, Helfer & Roman PRD 66 124012, CITED, read in full"),

    ("D7",
     "A corridor must HOLD for at least one light-crossing or it transmits "
     "nothing, and the duration QEI rho >= -C/tau^4 refuses exactly that.  The "
     "bound is STATE-INDEPENDENT over Hadamard states, so no branch of any "
     "decomposition escapes it",
     THEOREM, ("bounds", "DURATION_ROUTE_Z"),
     "a matter model outside its hypotheses -- see O1, which is exactly that"),

    ("D8",
     "The pointwise T^r_r test RESTATES certify.py on a strictly SMALLER class "
     "and does not supersede it: it needs tracelessness and a test-field "
     "background where certify.py needs neither",
     THEOREM, ("tolman", "RESTATES_CERTIFY_ON_SMALLER_CLASS"),
     "nothing; the containment is proper and machine-checked"),

    ("D9",
     "A SOURCED background satisfying the pointwise test's hypotheses forces "
     "Minkowski, so the test has content only as a test-field statement.  "
     "'Minkowski' is for Lambda = 0 (CORRECTED, DOCKET 67): with Lambda != 0 "
     "and T read as matter, the regular static solution with T^matter = 0 is "
     "de Sitter, and the test-field reading stands",
     THEOREM, ("tolman", "SUPERSEDES_CERTIFY"),
     "nothing; THEOREM X, two independent machine checks"),

    ("D10",
     "Sustaining contraction does NOT force rho < 0.  Witnesses hold it for all "
     "time with rho = 0 exactly and with rho > 0 exactly, NEC satisfied and not "
     "saturated.  What kills the driven route is kinematics, not an energy "
     "condition",
     THEOREM, ("nonstatic", "SUSTAINING_FORCES_NEGATIVE_RHO"),
     "nothing; it is why D7 and not an energy condition is the obstruction"),

    ("D11",
     "The exchange rate: kg of negative enclosed mass per metre of contraction, "
     "from the method equation's own coefficient",
     MEASURED, ("overturn", "LAMBDA"),
     "a re-ruling of LAMBDA, which is a corpus question and not a physics one"),

    ("D12",
     "NO-IN-PRACTICE on the geometric route: four limbs, each proved inside its "
     "own hypotheses.  THE CONJUNCTION IS A SURVEY AND NOT A THEOREM, because "
     "limb one quantifies over ONE field and nothing proves the four hypotheses "
     "exhaust the matter models",
     SURVEY, None,
     "a matter model outside all four sets of hypotheses would break it "
     "without refuting any single limb"),

    ("D13",
     "Classical information travels at <= c IN THE METRIC ITS CARRIER "
     "PROPAGATES IN, and the no-communication theorem closes the entangled "
     "variant -- for linear, completely positive dynamics, non-selective "
     "local operations, commuting local subsystems and no closed causal loops "
     "(CORRECTED, DOCKET 67: these hypotheses were unnamed; outside the first "
     "a nonlinear local map signals).  For a BRANE-CONFINED carrier that metric is the induced metric "
     "and the reconstruction route is EMIGRATION WITHOUT SPEED.  THE ROW IS "
     "NOT A STATEMENT ABOUT A BULK CARRIER: on a brane moving through a "
     "compact extra dimension, bulk null geodesics join brane points the "
     "induced metric calls spacelike, and GKLP's field commutator on M4 x S1 "
     "is non-zero across them",
     NARROWED, None,
     "nothing further -- limb 2 was always intact and limb 1 is now stated "
     "over the class it was proved for.  It is why S5 is a price rather than "
     "a shortcut FOR A BRANE-CONFINED CARRIER, which is the only case it "
     "covers"),

    ("D14",
     "A static spherically symmetric device has NO PARAMETER IN WHICH A "
     "DESTINATION CAN BE WRITTEN: the solution data is (Phi, m) as functions "
     "of r alone, no entry of either is a function of direction, and the "
     "contraction it certifies is identical in every direction.  Addressing "
     "is not un-answered on the priced object, it is UNDEFINED on it",
     THEOREM, ("certify", "THEOREM_SCOPE"),
     "nothing; dL/dtheta = dL/dphi = 0 is machine-checked.  What it costs is "
     "O4: the whole demand side prices an object that cannot have a "
     "destination.  SCOPE FLAGGED BY DOCKET 62: O4 closed on a CYLINDRICAL "
     "object, which has an axis, and an axis supplies a direction and two "
     "ends, not a 3-D destination -- so on the axial object undefinedness "
     "narrows from 'no parameter at all' to 'a one-bit parameter', and what a "
     "full 3-D address requires of a metric is written down nowhere.  The "
     "theorem stands on its own class; the board's use of it moved.  The "
     "Higgs does not supply the missing parameter (S6)"),

    # ----- DOCKET 63: the Higgs at the endpoint.  Owners exactly as ruled. ----
    ("D15",
     "A static displacement of any vacuum with V''(v) = m^2 > 0 returns to v "
     "at asymptotic rate EXACTLY m -- every Mexican hat, any dimension d, "
     "nonlinearly, for any source sign, size or shape, outside its support.  "
     "Proved by an elementary Riccati argument (ruling F1), not by the unread "
     "Levinson/Hartman theorem.  For the Higgs the rate is hbar/(m_h c) = "
     "%.6e m at the READ m_h" % excite.LAMBDA_H_READ_M,
     THEOREM, ("excite", "TAIL_RATE_IS_MASS"),
     "a failure of one of its hypotheses: %s"
     % "; ".join(excite.TAIL_RATE_HYPOTHESES)),

    ("D16",
     "The displacement is ULTRALOCAL: delta phi = -J/m_h^2 locally and "
     "INT G d^3r = 1/m^2, so a displaced vev exists only where its source is "
     "and no arrangement of sources beats the local density",
     THEOREM, ("excite", "DISPLACEMENT_IS_ULTRALOCAL"),
     "a failure of its hypotheses -- linear regime, static, source scale L "
     "large against lambda_h; the error is (lambda_h/L)^2"),

    ("D17",
     "Role 3 at the endpoint -- the Higgs as a source of NEC violation -- is "
     "closed for ANY CLASSICAL minimally coupled scalar with a CANONICAL "
     "two-derivative kinetic term, any potential, any mass: "
     "T_kk = (k.d phi)^2 >= 0.  (CORRECTED, DOCKET 67: as first written, "
     "'a source of negative energy' and 'ANY minimally coupled scalar'; "
     "rho = V_min < 0 at the vev is allowed, and the SM Higgs is classical "
     "and canonical here.)  The obstruction is not the Higgs mass; it "
     "would be just as closed at m_h = 0",
     THEOREM, ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC"),
     "a non-minimal coupling -- which is S4 and O1, both refused; outside the "
     "row's class, quantum states (NEC violation at first order in hbar, "
     "R4/R6's) and non-canonical kinetic terms (P(X), Galileons)"),

    ("D18",
     "m_e -> m_e(1 + eps), alpha fixed and nuclei clamped, is an EXACT "
     "dilation of the Schrodinger and Dirac-Coulomb problems, so a displaced "
     "endpoint does not bind wrong through a_0: the object is its own ruler",
     THEOREM, ("excite", "ELECTRON_MASS_IS_A_RULER"),
     "alpha not held fixed (H1) or finite nuclear size -- the residual "
     "channels, O(eps) through m_p/m_e, which S7 prices"),

    ("D19",
     "A displacement along T1, T2, T3 or Y leaves H+H, every mass and every "
     "derivative-free gauge-invariant local observable unchanged: the flat "
     "directions are INERT",
     THEOREM, ("excite", "FLAT_DIRECTIONS_ARE_INERT"),
     "nothing gauge-invariant, local and derivative-free; a radial "
     "displacement is the control that moves H+H"),

    ("D20",
     "Holding eps costs source 4 rho_EW eps(2-eps)(1-eps)^2 plus field "
     "rho_EW eps^2(2-eps)^2.  At the clock-comparison ORDER eps = %.0e that "
     "is %.6e kg/m^3 of Higgs-derived density, and %.2g (H1) to %.2g (H2) "
     "kg/m^3 of stable matter.  m_h is READ (%.2f, captures/PDG-2026.tsv); "
     "G_F is %s (PDG 2024 Table 1.1, 1.1663788(6)e-5 GeV^-2, identical to "
     "the typed digits), and the figure inherits G_F's status.  CORRECTED "
     "(DOCKET 67 follow-ups): this read 'G_F is NAMED-NOT-READ'; DOCKET 67 "
     "READ it, and no value moved.  The printed digits are "
     "arithmetic, not physical precision: the figure is tree level (MS-bar "
     "NNLO lambda/LO = 0.9757 moves it -2.4%%), eps's '+1' coefficient "
     "carries O(1e-3), and the value assumes SM self-couplings (it scales "
     "with the depth, (3 - kappa_lambda)/2, kappa_lambda bounded to "
     "(-1.2, 7.5)) and kappa_e = 1 (it scales as 1/kappa_e, |kappa_e| < 260); "
     "the H1 stable-matter figure carries the one-loop 2/9 (7.8e+11 with "
     "N3LO's 0.23839), all computed by DOCKET 67"
     % (excite.EPS_AT_FIXTURE, excite.HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18,
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H1"],
        excite.HOLD_STABLE_KG_M3_AT_EPS_1E18["H2"], higgs.M_HIGGS,
        higgs.STATUS_D67["G_FERMI"]),
     MEASURED, ("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18"),
     "a cheaper stable neutral source (DOCKET 63 E1, unsettled), the "
     "Yukawa-running correction to the 2/9 source fraction (E10, unsettled), "
     "a later G_F or m_h differing from the READ values carried (CORRECTED, "
     "DOCKET 67 follow-ups: this read 'a READ G_F or m_h'; both are READ), "
     "or the H1/H2 choice, which no Standard Model instrument can "
     "make and this file does not"),

    # ----- DOCKET 62: the O3 narrowing, seated as its own THEOREM. ----------
    ("D21",
     "THE FLAT-BULK LATTICE THEOREM: %s.  At rank 1 with a spatial circle the "
     "condition is vacuous, so GKLP's 'no' is FORCED rather than contingent; "
     "at rank 2 the chronology-respecting case is exactly the spacelike span "
     "(a degenerate span is the boundary, causal but not stably causal, and a "
     "rational one holds a null lattice vector; rank >= 3 needs the signature "
     "of the full Gram matrix -- CORRECTED, DOCKET 67), and the "
     "separating witness e1, e2 has norms %s, %s and a %s sum (%s).  "
     "DOCKET 57's 'two independent routes' -- %s"
     % (latticectc.LATTICE_THEOREM,
        latticectc.WITNESS_NORMS[0], latticectc.WITNESS_NORMS[1],
        latticectc.WITNESS_SPAN, latticectc.WITNESS_NORMS[2],
        latticectc.DOCKET57_TWO_ROUTES),
     THEOREM, ("latticectc", "LATTICE_THEOREM"),
     "a failure of a hypothesis -- %s.  The codimension-one CTC does NOT move "
     "it: %s" % ("; ".join(latticectc.HYPOTHESES),
                 latticectc.CODIM1_CTC_REFUSAL)),

    # ----- the board catching up with the tree: fluctuation.py.  DOCKET 64:
    # noise.py prices the smeared fluctuation in flat space and the row moves
    # OPEN -> SURVEY; the wording it replaces is D22_DOCKET62 (kept). -------
    ("D22",
     "THE SMEARED FLUCTUATION DOES NOT RESTATE THE DEMAND, IN FLAT SPACE.  "
     "fluctuation.py's pointwise T1 stands (Delta' >= 1/2, Delta >= 1/3 for "
     "every zero-mean Gaussian (Hadamard) state of the MASSLESS minimal "
     "scalar, z3; with a mass term the floor is Delta' >= 2/5 -- CORRECTED, "
     "DOCKET 67: the field model was unnamed in this clause), and it is "
     "sign-blind at either floor, so it cannot be the demand.  For the free minimal scalar in Minkowski (noise.py, "
     "flat model %s), Fewster's sampled energy density is bounded below AS "
     "AN OPERATOR by -C/tau^4 (C1_FLAT_THEOREM = %s).  The demanded density "
     "is therefore the mean of no state and, under H6 (the quantum spectral "
     "measure), the outcome of no measurement.  Vacuum SD_0 = %.6f C/tau^4 "
     "at every tau.  T1 fails under smearing (T1_SURVIVES_SMEARING = %s): "
     "thermal Delta'_f < 1/2 for tau > %.6f beta.  Under the Gaussian "
     "Einstein-Langevin surrogate -- a different reading of 'distribution', "
     "not H6 -- the probability is not zero: with the VACUUM's noise kernel "
     "at b = 1 m it is exp(-10^%.3f), below exp(-10^%d); a state with a "
     "larger noise kernel is not computed (EL_SURROGATE_NONVACUUM_COMPUTED "
     "= %s).  ON THE CORRIDOR THIS IS A %s: H2 fails, (b/l_G)^2 = %.0f, "
     "and the curved decision is %s's"
     % (", ".join(sorted(noise.HYPOTHESES)), noise.C1_FLAT_THEOREM,
        noise.SD0_OVER_C, noise.T1_SURVIVES_SMEARING,
        noise.TAU_STAR_OVER_BETA, noise.EL_VACUUM_LOG10_NEG_LN_P,
        int(math.floor(noise.EL_VACUUM_LOG10_NEG_LN_P)),
        noise.EL_SURROGATE_NONVACUUM_COMPUTED, noise.CORRIDOR_APPLICATION,
        noise.B_OVER_LG_SQUARED, noise.CURVED_PART_CARRIED_BY),
     SURVEY, ("noise", "CORRIDOR_APPLICATION"),
     "%s's absolute QEI evaluated on the corridor: by FFR 1004.0179 note "
     "[18] it decides the distribution question there, with no variance at "
     "all, IF the evaluated bound Q_corr is below the demanded magnitude "
     "and holds on the whole domain of a self-adjoint realisation of the "
     "corridor's sampled operator (a curved H3); a bound above it decides "
     "nothing.  The TIME-smeared curved variance itself, were it wanted, "
     "needs no NEW renormalisation (Hu & Verdaguer 3.2, READ, gives the "
     "counterterm cancellation and separated-point finiteness; the pull-back "
     "to the worldline is Fewster 1208.5399 sec. 3.3, NAMED; "
     "CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION = %s; CORRECTED, DOCKET "
     "67: 'decides' was unconditional and H&V carried the whole claim), and its "
     "finiteness is %s.  Or a failure of H3 (%s: %s) -- a "
     "self-adjoint extension other than Friedrichs need not keep the bound"
     % (noise.CURVED_PART_CARRIED_BY,
        noise.CURVED_VARIANCE_NEEDS_QUARTIC_RENORMALISATION,
        noise.CURVED_VARIANCE_FINITENESS, noise.HYPOTHESES["H3"][0],
        noise.HYPOTHESES["H3"][1])),

    # ----- the principle applied (docstring section 4): each of these has an
    # instrument in the tree, so each gets its row now.  DOCKET 62's
    # recommended NEW rows. ------------------------------------------------
    ("D23",
     "THE FIRST TRIP.  transit.py: a channel spanning D required something to "
     "cross D at <= c beforehand -- THE CORRIDOR MUST BE TRAVERSED IN ORDER TO "
     "EXIST.  CORRECTED (DOCKET 67): that holds for initially SEPARABLE "
     "systems with every resource starting at ONE END, which is S5's case; "
     "the theorem itself needs only a common causal past (a midpoint source "
     "spans D at D/(2c)), and the vacuum is already entangled across "
     "spacelike regions (harvested, small: no near-maximal Bell pair across "
     "a macroscopic D is shown).  Its advantage over light is ZERO BY CONSTRUCTION, not by "
     "measurement: transit.py models the channel's arrival as the classical "
     "message at c, because reading the shared state carries nothing alone "
     "(READING_CARRIES_NOTHING_ALONE = %s -- the no-communication theorem), "
     "so advantage_over_light(D) = D/c - D/c at every distance it lists "
     "(%s: %s).  Applied to S5 with no entanglement in it: the "
     "fabricator, the stock survey and the receiver all had to reach the "
     "destination at <= c.  So S5 is an AMORTISATION SCHEME, not a transport "
     "route, with a minimum setup of the light time, %.4g years at Proxima "
     "(the span in light years, foliation.py).  "
     "Whether that setup amortises is OPEN"
     % (transit.READING_CARRIES_NOTHING_ALONE,
        ", ".join(n for n, _d in transit.DISTANCES),
        ", ".join(sorted(set("%.3f" % transit.advantage_over_light(d)
                             for _n, d in transit.DISTANCES))), PROXIMA_LY),
     OPEN, ("transit", "TRAVERSAL_IS_REMOVED"),
     "S5 priced per reconstruction -- DOCKET 56's owed instrument -- set "
     "against the first trip, giving the number of later reconstructions at "
     "which the route beats sending the payload itself at <= c.  Nothing "
     "removes the first trip: transit.py moves the traversal earlier, it does "
     "not delete it"),

    ("D24",
     "FORMATION.  D1-D14 each price a CONFIGURATION, and none prices getting "
     "to it.  create.py: bringing a throat into existence is TOPOLOGY CHANGE, "
     "and, FOR CAUSALLY COMPACT INTERPOLATING SPACETIMES, Geroch and Borde "
     "force causality violation for it kinematically -- '%s'; Borde: '%s' -- "
     "so exotic matter cannot help (EXOTIC_MATTER_HELPS_CREATION = %s).  "
     "Dropping causal compactness is one of Borde's three escapes, and none "
     "stays inside Lorentzian GR without a pathology "
     "(any_escape_stays_in_lorentzian_gr() = %s).  Enlarging an existing throat is a metric "
     "change those theorems say nothing about "
     "(create.theorems_apply_to_enlargement() = %s), but its premise is "
     "unpriced: %s"
     % (create.BORDE, create.BORDE_SINGULARITY,
        create.EXOTIC_MATTER_HELPS_CREATION,
        create.any_escape_stays_in_lorentzian_gr(),
        create.theorems_apply_to_enlargement(), create.ROUTE_COST)
     # DOCKET 67 appends (M ruled "Repair all"); nothing above is replaced.
     + ".  CORRECTED (DOCKET 67): the kinematic theorems also assume a "
     "TIME-ORIENTED spacetime with a smooth Lorentz metric NON-DEGENERATE "
     "everywhere on the interpolating region; 'exotic matter cannot help' is "
     "exact for that forced CTC only -- Borde IX.B names large "
     "energy-condition violation as the way past Theorem 3's DYNAMICAL "
     "obstruction, and 2505.02210 builds a nucleation with CTCs violating "
     "every standard energy condition; Borde lists FOUR routes, and his IX.C, "
     "degenerate metrics, he places inside the Lorentzian framework, so 'none "
     "stays inside Lorentzian GR without a pathology' holds only if a "
     "degenerate point counts as a pathology or as leaving GR.  The "
     "theorems' silence on enlargement holds for a non-degenerate metric "
     "family on a FIXED spatial manifold with the throat radius > 0 (a "
     "product interpolation).  'Unpriced' is accurate at the tree's 1193 km "
     "target; published null results (from search snippets, NOT READ) bound "
     "the abundance of Ellis throats of 10 pc to 10 kpc and of ~1 cm"
     # DOCKET 64 appends; nothing above is replaced.
     + ".  THE PASSAGE IS PRICED (formation.py, DOCKET 64; F1 THEOREM under: "
     "%s).  Across a sphere the Kodama energy the passage carries is "
     "-m_1(R), the object's own enclosed negative mass, by any route at any "
     "speed; the extra outgoing radial null deficit is -(W_1 - 1)/(2 pi R) "
     "per passage, duration-independent (F2, THEOREM, adding: %s).  "
     "T^{0r} != 0 in the Eulerian (fixed-R) frame at some instant wherever m_1 != 0, with zero net momentum "
     "by symmetry (PHASE1_D4_POINTWISE_DURING_PASSAGE = %s) -- NOT PROPULSION "
     "under phase1.py's D4 as RESTATED ON M'S RULING (RULED_BY_M, M-D64-1).  "
     "Nucleation READ (%s): the neck is "
     "a recipe with free smooth functions (%s); its price has not been "
     "computed (NUCLEATION_PRICED = %s), and whether it is priceable from the "
     "source is %s"
     % ("; ".join(formation.F1_THEOREM),
        "; ".join(h for h in formation.F2_THEOREM
                  if h not in formation.F1_THEOREM),
        formation.PHASE1_D4_POINTWISE_DURING_PASSAGE,
        formation.NUCLEATION_SOURCE,
        ", ".join(formation.NUCLEATION_FREE_FUNCTIONS),
        formation.NUCLEATION_PRICED,
        formation.NUCLEATION_PRICEABLE_FROM_SOURCE),
     OPEN, ("formation", "NUCLEATION_PRICEABLE_FROM_SOURCE"),
     "the nucleation construction COMPUTED -- the neck recipe written out "
     "and integrated (%s, %s in create.py), over the whole cobordism W and "
     "not the neck alone (its energy-condition violations sit in the Morse "
     "spacetime's type-IV band and the CP^2 pocket), classically only (the "
     "source excludes QFT on its Cauchy horizon) -- CORRECTED, DOCKET 67; or an observed throat, priced by "
     "F1 as m_final(R) - m_initial(R) (the find-and-enlarge route: %s); the "
     "surface layer at R_s priced, since every formation.py figure lies on "
     "one side of it; or a passage with U != 0, which is outside F1.  The "
     "wording this replaces is kept (SUPERSEDED_WORDING, DOCKET 64)"
     % (create.NUCLEATION_LITERATURE, create.NUCLEATION_STATUS,
        create.ROUTE_COST)),

    ("D25",
     "THE DESTINATION STOCK GATE.  stock.py derives it and stockgate.py "
     "audits it: %s  The assemblable set is a principal ideal, down-set and "
     "join-closed (stockgate's z3 discharges).  A reference adult (ICRP) "
     "against a CI chondrite binds on %s at %.4g kg of feedstock per kg; the "
     "same payload against a stellar photosphere binds on %s at %.4g kg per "
     "kg.  A "
     "manufactured payload binds on a refractory rarity instead.  S5 cannot "
     "close in either direction while this gate is unchecked at its "
     "destination.  CORRECTED (DOCKET 67): the payload is ICRP 23's 70 kg "
     "reference MALE (1975; ICRP says it is amended by ICRP 89), and of its "
     "59 values 21 are ICRP 23 Table 110's -- all 11 bulk masses, which "
     "decide the CI binder -- 14 differ and 24, lithium among them, are not "
     "in that table (Emsley's); the CI "
     "table is not Lodders 2003's Table 3 (P 1040 against 920 +- 100 ppm); "
     "the 'stellar photosphere' is the present-day Sun (Asplund 2009) with "
     "meteoritic values for some elements.  THE BINDER IDENTITIES ARE "
     "DATA-DEPENDENT and are printed without uncertainty: at the photosphere "
     "Li runs 9%% behind P, inside photospheric Li's sigma (P(Li binds) = "
     "0.36 under A09; AAG21's Li makes Li bind), and CI N at its moved value "
     "(1965 ppm, LBP25) makes N bind at 13.07.  The magnitudes hold across "
     "these data: 8.3-13.1 (CI), 1.6e3-2.2e3 (photosphere) kg per kg"
     % ((stockgate.GATE,)
        + stockgate.binding_under("as-composed 59", "CI chondrite")
        + stockgate.binding_under("as-composed 59", "stellar photosphere"))
     # DOCKET 64 appends; the figures above are stockgate's and are NOT
     # re-printed below (formation.py's [W1]: over-representation).
     + ".  DOCKET 64 (formation.py): %s (DOCKET 67: MacGregor 2018 finds "
     "no NEED to posit the 1-4 au belt -- evidence removed by the source = "
     "%s (READ) -- and its first-12 image falls %.2f sigma below star + a "
     "%.0f uJy belt (on formation's H_unres and H_peak), under the %.0f "
     "sigma that would exclude it (H_3sig), so excluded by the source = %s "
     "(computed, formation.belt_excluded), and a belt below %.0f uJy is not "
     "spoken against even at %.0f sigma; that is not a "
     "withdrawal.  CORRECTED, DOCKET 67 follow-ups: this read 'about 2 sigma "
     "against it, and a belt below ~130 uJy is not excluded').  The "
     "aperture search covered "
     "'aperture' and its synonyms; %d files hit (%s among them) and none "
     "gives the arrival aperture a value (formation.APERTURE_SEARCH).  "
     "Survey: condensed body found = %s (%s); "
     "confirmed reservoir = %s; primitive measured = %s; accessible "
     "measured = %s; the data constrain bodies = %s"
     % (formation.D25_VERDICT,
        formation.SURVEY_BELT_1_4AU_EVIDENCE_REMOVED_BY_SOURCE,
        formation.belt_sigma_low(formation.BELT_PHOTOSPHERE_UJY
                                 + formation.BELT_ANGLADA_UJY),
        formation.BELT_ANGLADA_UJY, formation.BELT_DETECT_SIGMA,
        formation.SURVEY_BELT_1_4AU_EXCLUDED_BY_SOURCE,
        formation.belt_unexcluded_floor_ujy(), formation.BELT_PEAK_SIGMA,
        len(set(formation.APERTURE_HITS)
            | set(formation.APERTURE_SYNONYM_HITS)),
        " and ".join(sorted(
            f for f in ("ledger.py", "stockgate.py")
            if f in formation.APERTURE_HITS)) or "neither this file nor "
        "stockgate.py",
        formation.SURVEY_CONDENSED_BODY_FOUND,
        formation.SURVEY_CONDENSED_BODY,
        formation.SURVEY_CONFIRMED_RESERVOIR,
        formation.SURVEY_PRIMITIVE_MEASURED,
        formation.SURVEY_ACCESSIBLE_MEASURED,
        formation.SURVEY_CONSTRAINS_BODIES),
     OPEN, ("stockgate", "GATE"),
     "the destination's arrival aperture surveyed for a condensed, "
     "primitive body holding M(p,s) x m_payload of accessible mass -- a "
     "snow-line condition, so a condition on orbital radius at the "
     "destination, which the arrival coordinate does not yet carry.  "
     "Separation energy is not priced by stockgate.py and no figure here is "
     "an energy.  After DOCKET 64: an instrument that gives the arrival "
     "aperture a value, as an orbital-radius band at the destination; the "
     "formation-epoch disc T(a), P(a) there (NOT-FOUND, "
     "formation.SNOWLINE_SEARCH); and, for the condensed body the survey "
     "does name, its primitive (volatile) state and its accessibility "
     "measured"),

    # ----- DOCKET 64: linearised stability, opened by the docket that built
    # its instrument (docstring section 4).  Text ASKED of linstab.py. ------
    ("D26",
     "%s.  inf beta^2_crit over m > 0 = %s (classical radial sector: %s).  "
     "DOCKET 67: that classical radial THEOREM is this board's own Israel-"
     "shell algebra under P1-P4, not AMM's criterion, whose class is large-N "
     "free quantum fields about a solution of the semiclassical equations; "
     "the '(AMM)' label belongs to the semiclassical half"
     % (linstab.D26_CLAIM, linstab.BETA2_CRIT_INFIMUM,
        linstab.CLASSICAL_RADIAL_STATUS),
     OPEN, ("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND"),
     linstab.D26_ANSWERED_BY),
]

# ----- DOCKET 65 (massform.py), seated on M's ruling "Seat as proposed". -----

#: massform's rows as it states them, by id -- ASKED, never retyped.
PROPOSED = dict((r[0], r) for r in massform.PROPOSED_ROWS)


def _proposed_status(rid):
    """A proposed row's status, which must be one of this board's words: a
    status outside the vocabulary raises rather than seating a new word."""
    st = PROPOSED[rid][3]
    if st not in STATUSES:
        raise ValueError("massform proposes %s as %r, not a ledger status"
                         % (rid, st))
    return st


DEMAND += [(rid, PROPOSED[rid][2], _proposed_status(rid), PROPOSED[rid][4],
            PROPOSED[rid][5]) for rid in ("D27", "D28", "D29")]

# ----- DOCKET 68 (docket68/), seated on M's ruling "1 then 2 then 3 then 4". --
# Docstring section 7.  Every verdict is ASKED of combine.Screen, per variant;
# nothing below types a grade.  The census over all of combine's variants is
# its own full screen and is NOT re-run here (H-LEDGER-ASKS-REPRESENTATIVES).

#: The variants this board asks, by name -> combine literals.  NAMED, not
#: exhaustive: a variant not named here is not asked here.
D68_VARIANTS = (
    ("the board alone", ()),
    ("H-SETTLE alone (W2)", ("W2",)),
    ("H-FRAME clause 1 alone (F1)", ("F1",)),
    ("W2 x F1", ("W2", "F1")),
    ("clause 2b's D-CTC (F2b)", ("F2b",)),
    ("H-IT as an information layer (ITB)", ("ITB",)),
    ("ITB with R-INDEX", ("ITB", "RI")),
    ("H-INFO-SHAPE (SHAPE)", ("SHAPE",)),
    # ADDED (DOCKET 68 residuals): the member contributions combine computes
    # and B-combine.md section 5 lists, which O9 first left unasked -- asked
    # here, printed as combine returns them (OPEN pathways and NOT-BOUND-IF,
    # never removals), R-QUANTUM's beside R-INDEX's (M-D68-C5: both).
    ("H-SETTLE-KR alone (KR)", ("KR",)),
    ("W1 x F1", ("W1", "F1")),
    ("KR x F1", ("KR", "F1")),
    ("H-IT as Jacobson emergent gravity (ITJ)", ("ITJ",)),
    ("H-IT as ER=EPR (ITE)", ("ITE",)),
    ("R-QUANTUM alone (RQ)", ("RQ",)),
    ("ITB with R-QUANTUM (ITB+RQ)", ("ITB", "RQ")),
)
#: The variants asked at combine's second screened cell (1 AU, N = 7).
D68_VARIANTS_AU = (("W2 x F1", ("W2", "F1")), ("W2 x F1 x H-12", ("W2", "F1", "H12")))
D68_SCREEN = combine.Screen()                                # combine.CELL_MAIN
D68_SCREEN_AU = combine.Screen(cell=combine.CELL_AU)
D68_SCREEN_ROUTES = combine.Screen(mutate=("seat-routes",))  # H-SEAT-ROUTES
D68_ASKED = dict((k, D68_SCREEN.variant(set(p))) for k, p in D68_VARIANTS)
D68_ASKED_AU = dict((k, D68_SCREEN_AU.variant(set(p))) for k, p in D68_VARIANTS_AU)
#: O-SEAT on the board alone given H-SEAT-ROUTES ({S10, S13} only).
D68_SEAT_ROUTES = D68_SCREEN_ROUTES.variant(set())["per"]["O-SEAT"]
#: combine's end-to-end pricing of the drift route (figures imported there).
D68_FIRST = combine.first_transit()
#: How many variants combine builds (its screen covers every one; asked).
D68_VARIANT_COUNT = sum(1 for _v in combine.variants())

# ----- DOCKET 68 WAVE 2 (docstring section 7b), seated as wave 1 was. --------
# Every value below is ASKED of its owner -- settle.window_read (W2A-limits),
# vacuum.py (W2B-vacuum), seat.py (W2C-seat), combine.py (W2-combine) -- at
# run time; nothing is retyped.  The expensive pieces the owners carry in
# their own selftests (vacuum.compact_boundary, 44 s; combine's full screen)
# are cited, not re-run (H-LEDGER-ASKS-REPRESENTATIVES, section 7b).

#: settle's support-1 windows on the READ (abstract) Weinberg-family limits:
#: every (L, N, H-MAP reading) row of settle.WINDOW_READ_L x (7, 1e3, 1e6).
D68_WINDOW_READ = settle.window_read()
#: combine's z3 support-1 route alone at 1 AU, N = 7 (support 2 dropped,
#: combine's own mutation 'support1-only'), and the HISTORY encodings that
#: reproduce wave 1's 1 AU and O-MAKE-DIST verdicts (combine's mutations
#: 'wave6-WREAD' and 'wave6-NVAC'), and vacuum.py's nine-hypothesis reading
#: H-VAC-LEFTIF (combine's 'vac-left-if').
D68_AU_SUPPORT1_ONLY = combine.Screen(cell=combine.CELL_AU, mutate=("support1-only",)).variant(
    {"W2", "F1"})["per"]["O-BITS"]
D68_AU3_SUPPORT1_ONLY = combine.Screen(cell=combine.CELL_AU3, mutate=("support1-only",)).variant(
    {"W2", "F1"})["per"]["O-BITS"]
D68_AU_WAVE6_WREAD = combine.Screen(cell=combine.CELL_AU, mutate=("wave6-WREAD", "support1-only")
                                    ).variant({"W2", "F1"})["per"]["O-BITS"]
D68_SCREEN_NVAC = combine.Screen(mutate=("wave6-NVAC",))
D68_SCREEN_VACLEFT = combine.Screen(mutate=("vac-left-if",))
D68_NVAC_ASKED = dict((k, D68_SCREEN_NVAC.variant(set(p))) for k, p in D68_VARIANTS)
D68_VACLEFT_ASKED = dict((k, D68_SCREEN_VACLEFT.variant(set(p))) for k, p in D68_VARIANTS)


def _d68_e(x):
    """1.338e5, not 1.338e+05: a float as index3.py types it."""
    m, e = ("%.3e" % x).split("e")
    return "%se%d" % (m, int(e))


def _d68_x(f):
    """A factor as the owners' reports print it: 96.5x, 1.43e4x (3 figures)."""
    if f < 1000:
        return "%.3gx" % f
    m, e = ("%.2e" % f).split("e")
    return "%se%dx" % (m, int(e))


def _d68_n(n):
    """7, 1e3, 1e6 -- N as the owners label their cells."""
    return "%d" % n if n < 1000 else "1e%d" % round(math.log10(n))


def d68_w2_window_cells(wr=None):
    """[(L, N, word, phrase)] -- settle.window_read's rows grouped by (L, N),
    in its order.  word is EXCLUDED (both H-MAP readings EMPTY), ADMISSIBLE
    (both OPEN) or SPLIT (the readings disagree: printed per reading, never
    one picked).  Where a reading's window is not robust across the four READ
    limits, H-SAME-EPS joins that reading's premises and the limits that
    open it alone are named (settle's own rows; asked)."""
    wr = D68_WINDOW_READ if wr is None else wr
    cells = []
    for r in wr["rows"]:
        key = (r["L"], r["N"])
        if not cells or cells[-1][0] != key:
            cells.append((key, []))
        cells[-1][1].append(r)
    out = []
    for (L, N), rows in cells:
        wins = set(r["window"] for r in rows)
        rd = "/".join(r["reading"][:1] for r in rows)
        fac = []
        for r in rows:
            pb = r["per_bound"][r["bound_used"]]
            fac.append(pb["loosening to open (context)"] if r["window"] == "EMPTY"
                       else pb["tightening to close (context)"])
        same = ["reading %s also given H-SAME-EPS (%s alone opens it)"
                % (r["reading"][:1], ", ".join(sorted(
                    k for k, v in r["per_bound"].items() if v["window"] != r["window"])))
                for r in rows if not r["robust_across_READ_bounds"]]
        if wins == {"EMPTY"}:
            word = "EXCLUDED"
            ph = ("EXCLUDED given W_W2R%s (a READ limit %s looser, readings %s, would open it)"
                  % ("; " + "; ".join(same) if same else "",
                     " / ".join(_d68_x(f) for f in fac), rd))
        elif wins == {"OPEN"}:
            word = "ADMISSIBLE"
            ph = ("ADMISSIBLE given W_W2R -- not excluded, not found%s (%s tighter, readings %s, "
                  "would close it)" % ("; " + "; ".join(same) if same else "",
                                       " / ".join(_d68_x(f) for f in fac), rd))
        else:
            word = "SPLIT"
            ph = "SPLIT across the H-MAP readings: " + "; ".join(
                "%s %s" % (r["reading"][:1], r["verdict"]) for r in rows)
        out.append((L, N, word, "%s, N = %s %s" % (L, _d68_n(N), ph)))
    return out


def d68_w2_windows_agree():
    """combine's exact-rational z3 window (combine.cell_window_open) against
    settle.window_read at each of combine's four screened cells: [(cell,
    combine's open?, settle's open?)] where they DISAGREE ([] = agree)."""
    by = dict(((L, N), w) for L, N, w, _p in d68_w2_window_cells())
    bad = []
    for cell, (attr, mult, N) in combine.CELLS.items():
        L = "1 AU" if attr == "AU_M" else ("1 ly" if mult == 1.0 else "%g ly" % mult)
        if by.get((L, N)) not in ("EXCLUDED", "ADMISSIBLE"):
            bad.append((cell, combine.cell_window_open(cell), by.get((L, N))))
        elif combine.cell_window_open(cell) != (by[(L, N)] == "ADMISSIBLE"):
            bad.append((cell, combine.cell_window_open(cell), by[(L, N)]))
    return bad


def d68_vac_grade():
    """vacuum.GRADES['O-MAKE-DIST'], asked and parsed exactly as combine's
    grounds parse it: (the LEFT-IF set, the OPEN pathways named before the
    grade's history clause)."""
    g = vacuum.GRADES["O-MAKE-DIST"]
    left = tuple(x.strip() for x in re.search(r"LEFT-IF \{([^}]*)\}", g).group(1).split(","))
    now = g.split("Wave 1 said")[0]
    via = tuple(k for k in ("N_NLDIST", "N_W2WEAK", "N_VACNP", "N_VAC")
                if re.search(r"\b" + k + r"\b", now))
    return left, via


def _d68_vac():
    """vacuum.py's cheap figures, asked (the harvested pair at beta = 7,
    lambda = 0.1, its symmetric-extension margins, the recurrence rounds, and
    the window-free floor at 1 ly); compact_boundary (44 s) is NOT re-run."""
    c7 = vacuum.build_cases()["gauss beta=7 (strong supports spacelike, R4)"]
    r7 = vacuum.state_for(c7, 0.1)
    n = vacuum.negativity_x(r7)
    wf = vacuum.window_free_floor(settle.LY_M)
    lt = settle.LY_M / settle.C_LIGHT
    return {"N": n, "f - 1/2": vacuum.fef_minus_half_x(r7),
            "margins B, A": (vacuum.sym_ext_margin_x(r7, "B"), vacuum.sym_ext_margin_x(r7, "A")),
            "rounds (twirl, rotation)": (vacuum.rounds_from(n)["rounds"],
                                         vacuum.rounds_from(n, post="swap")["rounds"]),
            "floor midpoint, one end (L/c)": tuple(
                wf[s]["window-free floor t_hold + L/c"] / lt for s in ("midpoint", "one-end")),
            "midpoint pair source (L/c)": wf["midpoint"]["midpoint pair source ready (D23)"] / lt,
            "R2 guaranteed N at cT = L/2": wf["midpoint"][
                "R2 guaranteed N >= exp(-(L/cT)^3) at cT = x L"][0.5]}


D68_VAC = _d68_vac()


def _d68_seat():
    """seat.py's W2C figures, asked: the grade of O-SEAT on today's board
    state, the gate's binder and runner-up at a CI-like body, whether P and N
    are measured in the Proxima system (seat.proxima_measured's own words),
    and Proxima b's minimum-mass floor over the CI threshold."""
    b = seat.binders()["CI chondrite"]
    pm = seat.proxima_measured()
    gc = seat.gate_conjuncts()
    ratio = [v for k, v in gc.items() if k.startswith("minimum mass over CI threshold")]
    return {"grade": seat.grade_o_seat(seat.board_state()),
            "binder": b[0], "runner-up": b[1],
            "P in the system": seat.P_MEASURED_IN_PROXIMA_SYSTEM,
            "P alpha Cen": pm["P"]["alpha_Cen_AB"], "N alpha Cen": pm["N"]["alpha_Cen_AB"],
            "P any body": pm["P"]["any_body"],
            "min-mass floor": ratio[0] if len(ratio) == 1 else None}


D68_SEAT = _d68_seat()


def d68_s5_owed():
    """seat.DOCKET56_OWED item by item: '<item>: <status head>' -- the item's
    name before its colon and the status's leading capitals, both asked."""
    out = []
    for item, status in seat.DOCKET56_OWED:
        m = re.match(r"[A-Z][A-Z -]*[A-Z]", status)
        out.append("%s: %s" % (item.split(":")[0], m.group(0) if m else status))
    return "; ".join(out)


def d68_grouped(o, asked=None):
    """o's verdict in every asked consistent variant at the main cell, the
    variants GROUPED by verdict ('<verdict> under <n> variants: a, b, ...'),
    each variant named once -- the same content as d68_uniform, compacted."""
    asked = D68_ASKED if asked is None else asked
    groups = {}
    for k, _p in D68_VARIANTS:
        if asked[k]["consistent"]:
            groups.setdefault(d68_verdict(asked[k]["per"][o]), []).append(k)
    if len(groups) == 1:
        return list(groups)[0] + " in every variant asked"
    return "; ".join("%s under %s" % (v, ", ".join(ks)) for v, ks in
                     sorted(groups.items(), key=lambda kv: -len(kv[1])))


def _d68_support(sp):
    """One support as combine states it: {members; named premises} [window]."""
    inside = "; ".join(x for x in (", ".join(sp["members"]), ", ".join(sp["named"])) if x)
    s = "{%s}" % (inside or "no member, no named premise")
    if sp.get("window"):
        s += " [%s]" % sp["window"].split(":")[0]
    return s


def d68_verdict(v):
    """One obstruction's verdict exactly as combine.Screen returns it -- the
    verdict word, its OPEN pathways, every minimal support, a NOT-BOUND's own
    removal status, a non-binding beside a removal, and the attribution."""
    out = v["verdict"]
    if v.get("via"):
        out += " via " + ", ".join(v["via"])
    if v.get("supports"):
        out += " " + " | ".join(_d68_support(s) for s in v["supports"])
    if v.get("removal"):
        out += ", its removal " + d68_verdict(v["removal"])
    if v.get("attribution") and v["verdict"] not in ("NOT-BOUND-IF", "NOT-BOUND"):
        out += " (credited: %s)" % v["attribution"]
    if v.get("nb"):
        out += "; beside it " + d68_verdict(v["nb"])
    return out


def d68_asked(name, o, au=False):
    """Obstruction o's verdict in the named asked variant, as combine says."""
    r = (D68_ASKED_AU if au else D68_ASKED)[name]
    if not r["consistent"]:
        return "INCONSISTENT (combine: a named clash)"
    return d68_verdict(r["per"][o])


def d68_uniform(o):
    """o's verdict if it is the same in every asked consistent variant at the
    main cell; otherwise each variant's, named -- never one picked."""
    got = dict((k, d68_asked(k, o)) for k, _p in D68_VARIANTS
               if D68_ASKED[k]["consistent"])
    vals = sorted(set(got.values()))
    if len(vals) == 1:
        return vals[0] + " in every variant asked"
    return "; ".join("%s under %s" % (v, k) for k, v in got.items())


def d68_o_bits_removed_outright():
    """[variant] among those asked (both cells) where combine says O-BITS is
    REMOVED with NO named premise (combine.counts(r, ('REMOVED',))) -- what
    closing O9 would need.  [] while every removal is REMOVED-IF."""
    out = []
    for lab, asked in (("", D68_ASKED), ("1 AU: ", D68_ASKED_AU)):
        for k, r in asked.items():
            if r["consistent"] and "O-BITS" in combine.counts(r, ("REMOVED",)):
                out.append(lab + k)
    return out


def _d68_s13_share():
    """massform's first-order share of the payload's mass already at the seat
    under S13 (1 - electrons regained - nucleons first order), as measure.py
    computes it -- an estimate on H-LINEAR, not a bound."""
    r = massform.HELD_SEAT_ROUTE
    return 1.0 - r["electrons regained"] - r["nucleons first order"]


def _d68_s13_phrase():
    """combine's own words for why S13 is not the seat's supply, READ from its
    board atom B-S13: 'S13 forms no baryons (C3, under H-C3)' -- the named
    hypothesis H-C3 included, so a row that drops it is caught."""
    for name, text, _e in combine._board(D68_SCREEN.A, D68_SCREEN.win_open):
        if name == "B-S13":
            m = re.search(r"S13 forms no baryons \([^)]*H-C3[^)]*\)", text)
            if m:
                return m.group(0)
    raise ValueError("combine's B-S13 no longer states S13's baryon clause under H-C3")


def _d68_feed():
    """D25's mass conjunct for the 70 kg payload, asked of stockgate (the
    figures measure.seat_route_s5 imports)."""
    return dict((d, stockgate.feedstock_kg(70.0, "as-composed 59", d))
                for d in ("CI chondrite", "stellar photosphere"))


# ----- DOCKET 66, WAVE 1 (docket66/), seated in DOCKET 68's form ------------
# Docstring section 8; M's order (M-D68-10), step 4.  Every verdict is ASKED of
# combine66.D66Screen -- docket68/combine.py's engine, run unchanged, with
# DOCKET 66's commitments as tracked constraints and combine's vocabulary
# extended IN PROCESS ONLY (combine66's E-EXTEND) inside combine66.vocabulary,
# which restores it on exit, so no DOCKET 68 ask above or below sees a D66
# literal (the selftest checks the restore).  Every figure is asked of
# defects.py, throatbits.py or qet.py.  combine66's full screen (3,528 + 1,764
# variants, about 16 minutes with its selftest) and its conservative-extension run
# are ITS OWN, READ from B-combine66.md and not re-run here
# (H-LEDGER-ASKS-REPRESENTATIVES).  Nothing here types a grade.

#: The variants this board asks of combine66, by name -> literals.  NAMED, not
#: exhaustive: one per D66 reading alone, the combinations B-combine66.md
#: section 5 answers, and the D68 contexts each D66 finding needs.
D66_VARIANTS = (
    ("the board alone (D66Screen, no D66 literal)", ()),
    ("H-DEFECT-SEAT: static string seat (DSTR)", ("DSTR",)),
    ("H-DEFECT-SEAT: thin wall seat (DWALL)", ("DWALL",)),
    ("H-DEFECT-SEAT: global monopole seat (DGMON)", ("DGMON",)),
    ("H-DEFECT-SEAT: gauge monopole seat (DMON)", ("DMON",)),
    ("H-DEFECT-SEAT: texture seat (DTEX)", ("DTEX",)),
    ("H-DEFECT-SEAT: string-supported throat (DTHR)", ("DTHR",)),
    ("H-THROAT-BITS: R-HOLO (TBHOLO)", ("TBHOLO",)),
    ("H-THROAT-BITS: R-THINSHELL (TBTSH)", ("TBTSH",)),
    ("H-THROAT-BITS: R-TELEPORT (TBTEL)", ("TBTEL",)),
    ("H-THROAT-BITS: R-ISLAND (TBISL)", ("TBISL",)),
    ("H-THROAT-BITS: R-ITB with ITB (TBITB)", ("TBITB", "ITB")),
    ("H-QET-EXOTIC: R-QET (QET)", ("QET",)),
    ("H-QET-EXOTIC: R-LIT (QLIT)", ("QLIT",)),
    ("R-LIT with W2 x F1", ("QLIT", "W2", "F1")),
    ("DSTR with W2 x F1", ("DSTR", "W2", "F1")),
    ("QET with R-QUANTUM (RQ)", ("QET", "RQ")),
    ("DTHR with ITB", ("DTHR", "ITB")),
    ("TBHOLO with ITB", ("TBHOLO", "ITB")),
    ("DTHR with TBHOLO", ("DTHR", "TBHOLO")),
    ("DTHR with QET", ("DTHR", "QET")),
    ("TBTEL with QET", ("TBTEL", "QET")),
    ("QET with SHAPE", ("QET", "SHAPE")),
    ("DSTR, TBHOLO and QET", ("DSTR", "TBHOLO", "QET")),
)
#: combine66's second screened cell (1 AU, N = 7): W2 x F1 variants only.
D66_VARIANTS_AU = (("DSTR with W2 x F1", ("DSTR", "W2", "F1")),
                   ("R-LIT with W2 x F1", ("QLIT", "W2", "F1")))
#: combine66's named readings (alternatives on record) and its HISTORY
#: encodings (D66 wave 1's own encodings, kept as readings by D66-fix), each
#: asked on one variant: (name, combine66 mutation, literals).
D66_READINGS_ASKED = (
    ("H-SEAT-ROUTES on DSTR", ("seat-routes",), ("DSTR",)),
    ("singok-board on the board alone", ("singok-board",), ()),
    ("singok-board with RQ", ("singok-board",), ("RQ",)),
    ("singok-a2 on DTHR (D66 wave 1's encoding)", ("singok-a2",), ("DTHR",)),
    ("qet-board-paths on QET (D66 wave 1's encoding)", ("qet-board-paths",), ("QET",)),
)


def _d66_ask(variants=None, variants_au=None, readings=None):
    """{'main', 'au', 'readings'}: combine66.D66Screen.screen per named
    variant, asked inside combine66.vocabulary(True), which restores combine's
    vocabulary on exit."""
    variants = D66_VARIANTS if variants is None else variants
    variants_au = D66_VARIANTS_AU if variants_au is None else variants_au
    readings = D66_READINGS_ASKED if readings is None else readings
    out = {"main": {}, "au": {}, "readings": {}}
    with contextlib.redirect_stdout(io.StringIO()), combine66.vocabulary(True):
        scr = combine66.D66Screen()
        scr_au = combine66.D66Screen(cell=combine.CELL_AU)
        for k, p in variants:
            out["main"][k] = scr.screen(set(p))
        for k, p in variants_au:
            out["au"][k] = scr_au.screen(set(p))
        for k, mut, p in readings:
            out["readings"][k] = combine66.D66Screen(mutate=mut).screen(set(p))
    return out


_D66 = _d66_ask()
D66_ASKED, D66_ASKED_AU, D66_READ_ASKED = _D66["main"], _D66["au"], _D66["readings"]


def _d66_r(name, au=False, reading=False):
    return (D66_READ_ASKED if reading else D66_ASKED_AU if au else D66_ASKED)[name]


def d66_core(r):
    """The tracked items of an inconsistent variant's first clash core, as
    combine reports them (its '@' marker dropped)."""
    return "{%s}" % ", ".join(x[1:] for x in r["clash_cores"][0] if x.startswith("@"))


def d66_asked(name, o, au=False, reading=False):
    """Obstruction o's verdict in a named D66 variant, exactly as combine66
    returns it (d68_verdict's form), or the clash core of an inconsistent one."""
    r = _d66_r(name, au, reading)
    if not r["consistent"]:
        return "INCONSISTENT (clash core %s)" % d66_core(r)
    return d68_verdict(r["per"][o])


def d66_seat(name, au=False, reading=False):
    """The seat condition M-S1A-P3 (i) in a named D66 variant, as combine66
    grades it: SATISFIED / SATISFIED-IF {named premises} / OPEN via /
    VIOLATED, and the OPEN pathways under which it is defeasible."""
    r = _d66_r(name, au, reading)
    if not r["consistent"]:
        return "INCONSISTENT"
    s = r["seat"]
    out = s["verdict"]
    if s["verdict"] == "SATISFIED-IF":
        out += " " + " | ".join("{%s}" % ", ".join(sp["named"]) for sp in s["supports"])
    if s.get("via"):
        out += " via " + ", ".join(s["via"])
    if s.get("defeasible"):
        out += ", defeasible via " + ", ".join(s["defeasible"])
    return out


def d66_defeasible(name):
    """{obstruction: [OPEN pathways]} under which a removal's every support can
    fail, in a named D66 variant (combine66's field)."""
    return _d66_r(name)["defeasible"]


def d66_load_bearing():
    """[(variant, [obstructions])] where combine66 credits a D66 literal as
    LOAD-BEARING in a removal or non-binding (combine66.d66_attributed), over
    every asked variant at both cells -- [] is the headline, asked here on the
    named variants; the census is combine66's (d66_census_read)."""
    out = []
    for lab, asked in (("", D66_ASKED), ("1 AU: ", D66_ASKED_AU)):
        for k, r in asked.items():
            got = combine66.d66_attributed(r)
            if got:
                out.append((lab + k, got))
    return out


def d66_in_support_only():
    """[variant] where a D66 literal sits inside a support but is load-bearing
    nowhere (combine66's d66_in_support minus its load-bearing lists)."""
    out = []
    for lab, asked in (("", D66_ASKED), ("1 AU: ", D66_ASKED_AU)):
        for k, r in asked.items():
            ld = r.get("d66_load", {})
            if ld.get("d66_in_support") and not (ld.get("needed") or ld.get("alternative")):
                out.append(lab + k)
    return out


def d66_d68_board_agrees():
    """The D66 screen with no D66 literal against combine.py's own board alone
    (D68_ASKED): [(obstruction, D66's, D68's)] where they DIFFER -- the
    conservative extension asked on one variant here; combine66's full run
    (every D68 variant) is READ from B-combine66.md."""
    a = D66_ASKED["the board alone (D66Screen, no D66 literal)"]["per"]
    b = D68_ASKED["the board alone"]["per"]
    return [(o, d68_verdict(a[o]), d68_verdict(b[o])) for o in b if d68_verdict(a[o]) != d68_verdict(b[o])]


def d66_group(names, field):
    """'<value> for a, b, ...; <value> for c' over named D66 variants, each
    named once -- field is an obstruction or 'SEAT'."""
    groups = {}
    for k in names:
        v = d66_seat(k) if field == "SEAT" else d66_asked(k, field)
        groups.setdefault(v, []).append(k.split(" (")[-1].rstrip(")"))
    return "; ".join("%s for %s" % (v, ", ".join(ks)) for v, ks in groups.items())


D66_DEFECT_SEATS = tuple(k for k, _p in D66_VARIANTS if k.startswith("H-DEFECT-SEAT: ")
                         and "seat (" in k and "texture" not in k)


#: A D66 variant's D68 context, by its D68 literals -> the D68_ASKED variant.
D66_CONTEXT_OF = {frozenset(): "the board alone", frozenset({"W2", "F1"}): "W2 x F1",
                  frozenset({"RQ"}): "R-QUANTUM alone (RQ)",
                  frozenset({"ITB"}): "H-IT as an information layer (ITB)",
                  frozenset({"SHAPE"}): "H-INFO-SHAPE (SHAPE)"}


def _d66_context(r):
    """combine.py's own variant (D68_ASKED) for a D66 variant's D68 literals."""
    return D68_ASKED[D66_CONTEXT_OF[frozenset(set(r["present"]) - set(combine66.D66_LITS))]]


def d66_added_lifts():
    """[(variant, [obstructions])] where an asked D66 variant removes or makes
    not-bound an obstruction its D68 context (combine.py) does not -- [] is
    'none a removal', asked on the named variants at 1 ly."""
    kinds = ("REMOVED", "REMOVED-IF", "NOT-BOUND-IF")
    out = []
    for k, r in D66_ASKED.items():
        if r["consistent"]:
            extra = sorted(set(combine.counts(r, kinds)) - set(combine.counts(_d66_context(r), kinds)))
            if extra:
                out.append((k, extra))
    return out


def d66_added_foreign_pathways():
    """[(variant, obstruction, pathway)] -- an OPEN pathway an asked D66 variant
    shows that neither its D68 context shows nor combine66 names (D66_OPEN)."""
    out = []
    for k, r in D66_ASKED.items():
        if not r["consistent"]:
            continue
        ctx = _d66_context(r)["per"]
        for o, v in r["per"].items():
            for p_ in v.get("via") or []:
                if p_ not in (ctx[o].get("via") or []) and p_ not in combine66.D66_OPEN:
                    out.append((k, o, p_))
    return out


#: B-combine66.md, combine66's own report of its full screen, READ (never
#: retyped): every figure the board cites from the runs it does not repeat.
D66_B_FILE = os.path.join(D66_DIR, "B-combine66.md")
D66_CENSUS_PATTERNS = (
    ("variants", r"That is ([\d,]+) D66 variants at 1 ly plus (\d+) context-only references, "
                 r"and ([\d,]+) \+ (\d+) at 1 AU"),
    ("load-bearing", r"The count is (\d+) in ([\d,]+) consistent variants at 1 ly and (\d+) in "
                     r"([\d,]+) at 1 AU"),
    ("selftest", r"runs \*\*(\d+) counted checks and passes all (\d+)\*\*"),
    ("controls", r"\*\*(\d+) of them are controls\.\*\*"),
    ("conservative", r"\*\*`--conservative-full` was re-run: ([\d,]+) compared .{0,90}?, (\d+) differ\*\*"),
    ("o-seat", r"\*\*O-SEAT\*\* is lifted in none"),
    ("o-make-dist", r"\*\*O-MAKE-DIST\*\* is lifted in none"),
    ("seat violated", r"It is VIOLATED in no consistent variant"),
)


def d66_census_read(path=None):
    """{key: groups} READ from B-combine66.md; raises if the owner's report no
    longer states a figure this board cites (a stale seat is a failure)."""
    with open(D66_B_FILE if path is None else path, encoding="utf-8") as fh:
        t = " ".join(fh.read().split())
    out = {}
    for key, pat in D66_CENSUS_PATTERNS:
        m = re.search(pat, t)
        if not m:
            raise ValueError("B-combine66.md no longer states %r -- the DOCKET 66 seat is stale" % key)
        out[key] = m.groups()
    return out


D66_CENSUS = d66_census_read()

#: qet.grades needs specthm's class verdicts only for its seat-class sentence
#: (about 45 s of z3); this board reads its own-content verdicts and its
#: per-obstruction text, which do not use them, and passes this placeholder --
#: the selftest re-asks with a second placeholder and requires the fields read
#: here to be unchanged.
D66_SPEC_NOT_ASKED = {"S-1": "not asked here", "S-2": "not asked here",
                      "S-3": "not asked here", "Rec": "not asked here"}


def _d66_figures(spec=None):
    """The DOCKET 66 owners' figures this board prints, ASKED: throatbits'
    capacity table and MMP scales, qet's minimal model, arrival-alone energy,
    supremum and board figures and its grades' own-content verdicts,
    defects' grades, gauge-monopole lens and global-monopole Jacobi zero."""
    cb = throatbits.capacity_table_base()
    rows = cb["rows"]
    mm = throatbits.mmp_scales()
    mmp_norm = [r for r in mm["by_coupling"] if r["N_f"] == throatbits.MMP_NF_SM]
    bf = qet.board_figures()
    sr = qet.sup_ratio()
    mv = qet.minimal_values(1.5, 1.0)
    m = qet.model(1.5, 1.0)
    with contextlib.redirect_stdout(io.StringIO()):
        qg = qet.grades(spec=D66_SPEC_NOT_ASKED if spec is None else spec, bf=bf, sr=sr)
        a1 = defects.a1_grades()
    sa, sj = defects.monopole_conjugate()
    return {
        "r_fit": (min(r["r_fit_m"] for r in rows), max(r["r_fit_m"] for r in rows)),
        "M_sat": (min(r["M_sat_kg"] for r in rows), max(r["M_sat_kg"] for r in rows)),
        "M_sat/payload": (min(r["M_sat_over_payload"] for r in rows),
                          max(r["M_sat_over_payload"] for r in rows)),
        "largest board throat (l_P), bits": (cb["largest_board_throat_over_lP"],
                                             cb["capacity_of_largest_board_throat_bits"]),
        "payload over it": (min(cb["payload_over_that_capacity"]),
                            max(cb["payload_over_that_capacity"])),
        "MMP binding = payload at r_e (max), l_P": (
            max(r["r_e_where_binding_equals_payload_m"] for r in mm["by_coupling"]), mm["l_P_m"]),
        "MMP N_f at r_fit (species count)": (
            min(r["at_r_fit"][0]["N_f_needed_for_payload"] for r in mmp_norm),
            max(r["at_r_fit"][0]["N_f_needed_for_payload"] for r in mmp_norm)),
        "MMP payload over SM throat": (
            min(min(r["payload_bits_over_capacity_at_r_e_SM"]) for r in mmp_norm),
            max(max(r["payload_bits_over_capacity_at_r_e_SM"]) for r in mmp_norm)),
        "QET arrival alone": qet.ev(qet.post_alice(m), m["HB"] + m["V"]),
        "QET E_B, E_A (1.5, 1)": (mv["E_B"], mv["E_A"]),
        "QET sup E_B/E_A": float(sr["sup"]),
        "QET payload rest J, injection J": (bf["payload_rest_J"], bf["payload_rest_J"] / 0.25),
        "QET r_quantum fraction": bf["r_quantum_fraction"],
        "R-QET own content": qg[0]["verdict_on_own_content"],
        "R-LIT own content": qg[1]["verdict_on_own_content"],
        "R-QET O-HOLD head": qg[0]["per"]["O-HOLD"].split(":")[0],
        "R-QET O-SEAT head": qg[0]["per"]["O-SEAT"].split(":")[0],
        "A1 seat": [(g["hypothesis"], g["seat_conditions"].split(". ")[0]) for g in a1],
        "gauge monopole lens": defects.gauge_monopole_lens(),
        "global monopole Jacobi zero / axis recrossing": sj / sa if sj else None,
    }


D66_FIG = _d66_figures()


def _d66_e(x, f=3):
    """A float as the owners' reports print it: 7.40e-22, not 7.40e-022."""
    m, e = ("%.*e" % (f - 1, x)).split("e")
    return "%se%d" % (m, int(e))


def d66_qet_literature():
    """[(the item as named to M, the READ entry qet.py records for it or
    None)] -- READ from qet.py's own SOURCES section (its docstring), whose
    header records the route: an item counts as READ only where it heads an
    entry there.  'Hotta 2008' is the entry whose head names Hotta and 2008."""
    doc = qet.__doc__
    i = doc.index("SOURCES, READ at source through alphaXiv")
    block = doc[i:doc.index("WHAT IT COMPUTES", i)]
    entries = [e for e in re.split(r"\n  (?=[A-Z])", block)[1:]]
    heads = [e.split("\n")[0] for e in entries]
    out = []
    for item in [x.strip() for x in M_D65_1_LITERATURE_ITEMS]:
        aid = re.search(r"arXiv:(\S+)", item)
        if aid:
            hit = [h for h in heads if "arXiv:" + aid.group(1) in h]
        else:
            name, year = item.split()
            hit = [h for h in heads if h.startswith(name) and year in h]
        out.append((item, hit[0].split(" (")[0].split(" = ")[0] if len(hit) == 1 else None))
    return out


#: The QET literature as it was named to M, item by item (M_D65_1_LITERATURE,
#: split at its own separators, is checked equal to these by the selftest).
M_D65_1_LITERATURE_ITEMS = ("Hotta 2008", "Funai & Martin-Martinez arXiv:1701.03805",
                            "Ikeda arXiv:2301.02666", "review arXiv:2505.04689",
                            "arXiv:2506.19878")
#: qet.py's route, READ from its SOURCES header (the words after 'READ at
#: source through ' up to the date).
D66_QET_ROUTE = re.search(r"SOURCES, READ at source through (alphaXiv \([^)]*\))",
                          qet.__doc__).group(1)


def _d66_string_crossing_only():
    """A1's own clause, READ from defects.HISTORY: 'only the string is
    crossing-only'; raises if the owner no longer says it."""
    hits = [h[2] for h in defects.HISTORY if "only the string is crossing-only" in h[2]]
    if len(hits) != 1:
        raise ValueError("defects.HISTORY no longer says 'only the string is crossing-only'")
    return "only the string is crossing-only"


#: DOCKET 66'S QUESTION FOR M (recorded, not applied): spec.py's 'TURN'.  The
#: question is A1's (defects.HYPOTHESES H-TURN-CONJUGATE / H-TURN-CROSSING),
#: carried as 'for M' since wave 1 and by D66-fix; the values are asked.
#: RULED since (M-RULINGS item 27, M: "Any crossing"; the row M-D68-27): kept
#: as HISTORY, printed as FIRST RECORDED in M-D68-27's row and after the
#: ruling in O9's DOCKET 66 answer; its values are still asked.
def d66_turn_question():
    """(question, why, proposed, waiting on it) for the TURN question, every value
    asked of defects.py."""
    h = defects.HYPOTHESES
    gm = D66_FIG["gauge monopole lens"]
    return (
        "spec.py's PART 2 'TURN': H-TURN-CONJUGATE (%s) or H-TURN-CROSSING (%s)?  Since "
        "D66-fix it decides one class only, the straight string"
        % (h["H-TURN-CONJUGATE"].split(" read as ")[1], h["H-TURN-CROSSING"].split(" read as ")[1]),
        "A1 (defects.py, asked): the global monopole's first Jacobi zero falls at the axis "
        "recrossing (ratio %.12f; defects.monopole_conjugate) and the gauge monopole is an "
        "S-1 point lens IF {H-MONOPOLE-MASS, H-WEAK-FIELD, H-S1-VACUUM} (a 1 AU focus at "
        "b = %s m; S-1 conditions hold: %s; defects.gauge_monopole_lens), so both TURN "
        "under either reading; and, in A1's words (defects.HISTORY), %s -- the straight "
        "string TURNs under H-TURN-CROSSING only.  The board never fixed which"
        % (D66_FIG["global monopole Jacobi zero / axis recrossing"], _d66_e(gm["b_m"]),
           gm["S-1 conditions hold"], _d66_string_crossing_only()),
        "none: the reading is M's; A1 grades the string under both, side by side",
        "the straight string's TURN, and with it whether a string seat lenses (A1's seat "
        "grade); no obstruction on this board moves either way")


#: DOCKET 68 NOTES on the rows O-SEAT and the pair supply touch.  A note, not a
#: status change: no owner's computed status moved.  Every figure asked.
#: WAVE 1'S WORDS ON THE PAIR SUPPLY AND THE SEAT GATE, kept as history and
#: printed in the notes after wave 2's: the text wave 1 printed, with its one
#: asked value -- O-MAKE-DIST, which wave 1 read OPEN via N_VAC -- re-asked of
#: combine's HISTORY encoding 'wave6-NVAC' (the as-of value), never typed.
D68_D23_AS_WAVE1 = (
    "combine.py screens vacuum entanglement used as the channel's pairs with no "
    "distribution as the OPEN pathway N_VAC, and O-MAKE in its distribution form reads "
    "%s; whether any setup supplies the pairs a qubit needs faster than distribution "
    "is not computed, and D68 wave 2 reads it (M-D68-10).  IF W2 x F1's first support "
    "held (N_EPS at the NAMED-NOT-READ Weinberg-family limit, H-C2, F1, H-BLOCK -- none "
    "shown), a midpoint source would give the first read %.5f of the light time after "
    "firing at 1 ly"
    % (d68_grouped("O-MAKE-DIST", D68_NVAC_ASKED),
       D68_FIRST["first_transit_midpoint"]["t_read"] / D68_FIRST["light_time_s"]))

D68_NOTES = {
    "D23": (
        "  DOCKET 68 (a note; no status change): the pair supply.  Wave 1 screened "
        "vacuum entanglement used as the channel's pairs with no distribution -- "
        "combine's reading of M's \"because is already exists everywhere\" "
        "(CHARTER.md, verbatim; combine.py's own gloss of it, 'it already exists "
        "everywhere', is an emended text and is not M's) -- as the OPEN pathway "
        "N_VAC.  WAVE 2 COMPUTED IT (vacuum.py, W2B-vacuum; its sources READ via "
        "alphaXiv and Firecrawl, each route recorded there, M-D68-16): N_VAC splits "
        "-- the vacuum's entanglement reaches probes that cannot communicate, but "
        "is not usable as the channel's pairs with nothing crossing at <= c first "
        "-- and combine retires N_VAC to its history (in combine.HISTORY_OPEN: %s).  "
        "vacuum.py grades O-MAKE-DIST LEFT-IF {%s}, and OPEN outside that set via "
        "%s, none computed (vacuum.GRADES, asked); combine screens O-MAKE in its "
        "distribution form as %s -- and LEFT in every asked variant given "
        "H-VAC-LEFTIF, the nine taken together (%s).  Asked of vacuum.py: the "
        "harvested pair at beta = 7, lambda = 0.1 has N = %s and f - 1/2 = %s "
        "(the single-copy LOCC ceiling), symmetric-extendible on both sides "
        "(margins %s, %s), so a near-maximal pair distilled from it needs "
        "classical messages each way; recurrence before hashing pays takes %d rounds (twirl) or %d "
        "(rotation).  With no window family assumed (R2 harvests with cT << L at "
        "every L, at a negativity R2 guarantees only down to exp(-(L/cT)^3): %.3g "
        "at cT = L/2) the vacuum route's floor is t_hold + L/c, %.2f L/c from a "
        "midpoint and %.2f L/c from one end (vacuum.window_free_floor), after the "
        "light time and after a midpoint pair source (%.2f L/c): the distribution "
        "is relocated to the probes and to at least one classical message, not "
        "removed -- two-way (R9) in the two computed families, the Gaussian and "
        "Reznik's; for R2's windows only >= 1 message is shown, and the floor "
        "counts only the one (the wave-2 seat first said 'relocated to the probes "
        "and to two-way messages', unscoped).  The "
        "family-specific window bound (Reznik's window over gaps in [2, 40]) is "
        "vacuum.compact_boundary's and is not re-run here.  IF W2 x F1's first "
        "support held (N_EPS at the READ (abstract) Weinberg-family limit under "
        "W_W2R, H-C2, F1, H-BLOCK -- none shown), a midpoint source would give the "
        "first read %.5f of the light time after firing at 1 ly "
        "(combine.first_transit), against this row's zero advantage, which is "
        "exact in linear quantum mechanics; with one-end distribution, S5's case, "
        "it beats light launched at firing: %s.  This row also binds S5's CHANNEL "
        "under O9's O-SEAT reading, not S5's substance.  WAVE 1 FIRST SAID (kept): "
        "%s"
        % ("N_VAC" in combine.HISTORY_OPEN, ", ".join(d68_vac_grade()[0]),
           ", ".join(d68_vac_grade()[1]), d68_grouped("O-MAKE-DIST"),
           d68_grouped("O-MAKE-DIST", D68_VACLEFT_ASKED),
           _d68_e(D68_VAC["N"]), _d68_e(D68_VAC["f - 1/2"]), _d68_e(D68_VAC["margins B, A"][0]),
           _d68_e(D68_VAC["margins B, A"][1]), D68_VAC["rounds (twirl, rotation)"][0],
           D68_VAC["rounds (twirl, rotation)"][1], D68_VAC["R2 guaranteed N at cT = L/2"],
           D68_VAC["floor midpoint, one end (L/c)"][0], D68_VAC["floor midpoint, one end (L/c)"][1],
           D68_VAC["midpoint pair source (L/c)"],
           D68_FIRST["first_transit_midpoint"]["t_read"] / D68_FIRST["light_time_s"],
           D68_FIRST["first_transit_one_end"]["beats_light_launched_at_firing"],
           D68_D23_AS_WAVE1)),
    "D25": (
        "  DOCKET 68 (a note; no status change): this gate is half of O-SEAT's "
        "one open route.  Under H-SEAT-S5 (M-D68-7) O-SEAT, the supply at the "
        "seat, is removed only if S5's supply is shown AND this gate holds "
        "(combine's OPEN pathway N_S5); for the 70 kg payload the mass "
        "conjunct is %.1f kg of CI chondrite or %.4g kg of stellar photosphere "
        "in the arrival aperture (stockgate.feedstock_kg, asked: this row's "
        "per-kg figures for 70 kg).  WAVE 2 ASKED IT AT PROXIMA (seat.py, "
        "W2C-seat; sources READ via alphaXiv and Firecrawl, routes recorded "
        "there, M-D68-16): seat.grade_o_seat on today's board state = %s.  The "
        "gate's binder at a CI-like body is %s, as this row's claim states "
        "(seat.binders, asked, agrees on the element; runner-up %s, %.2f kg per "
        "kg of payload).  P in alpha Cen A/B: %s; in any body: %s "
        "(seat.P_MEASURED_IN_PROXIMA_SYSTEM = %s) -- so the composition conjunct "
        "cannot be evaluated at its binder on READ data.  N, the runner-up: %s.  "
        "Proxima b's minimum mass (m sin i, READ) is at least %s x the CI "
        "threshold, a floor on total mass and NOT accessible mass (H-BODY-ACCESS); "
        "the aperture is NOT EVALUABLE.  Unchecked at every destination, so "
        "O-SEAT stays OPEN"
        % (tuple(_d68_feed()[d] for d in ("CI chondrite", "stellar photosphere"))
           + (D68_SEAT["grade"], D68_SEAT["binder"][0], D68_SEAT["runner-up"][0], D68_SEAT["runner-up"][1], D68_SEAT["P alpha Cen"],
              D68_SEAT["P any body"], D68_SEAT["P in the system"], D68_SEAT["N alpha Cen"],
              _d68_e(D68_SEAT["min-mass floor"])))),
}


def _d68_note(rid):
    """The DOCKET 68 note a row carries, or ''."""
    return D68_NOTES.get(rid, "")


DEMAND = [(r[0], r[1] + _d68_note(r[0])) + tuple(r[2:]) for r in DEMAND]

#: THE WORDING DOCKET 64 REPLACED ON DEMAND ROWS, kept for SUPERSEDED_WORDING.
#: Typed here because it is HISTORY -- what the board said -- and not a result;
#: the one computed clause (create.py's) is still asked.
#: CORRECTED (DOCKET 67), recorded against this kept wording and not edited
#: into it: "Every demand row is a demand on <rho>" is exact only at
#: alpha = beta = 0; Kuo & Ford PROPOSE Delta as "a measure" -- it is not
#: shown to be "that equation's error"; and their 1993 remark that the
#: renormalisation of quartic operator products did not exist is dated and
#: concerns POINTWISE normal-ordered quartics (Brunetti-Fredenhagen-Koehler
#: 1996, NAMED-NOT-READ; Hollands & Wald 2001, READ), which Kuo & Ford exempt
#: from averaged quantities, so it is not a remark about the smeared price.
D22_DOCKET62 = (
    "THE SEMICLASSICAL DEBT.  Every demand row is a demand on <rho> inside "
    "G = 8 pi G <T>, and Kuo & Ford's measure of that equation's error, "
    "Delta, is re-derived exactly in flat space: the pointwise measure is "
    "recomputed two independent ways, and Delta >= 1/3 is PROVED (z3) for "
    "EVERY zero-mean Gaussian state, without Kuo & Ford's diagonal "
    "assumption.  The pointwise Delta is sign-blind -- it condemns thermal "
    "radiation too -- so it cannot be the demand.  THE SMEARED PRICE AT THE "
    "CORRIDOR'S OWN SCALES IS OPEN [status OPEN, owner "
    "fluctuation.PRICES_THE_CORRIDOR] || the SMEARED fluctuation priced at "
    "the corridor's scales -- the width b and Fewster's sampling time -- "
    "which needs the curved-space renormalisation of quartic operator "
    "products Kuo & Ford said did not exist.  If it is of order one there, "
    "the demand column must be written about a distribution rather than an "
    "expectation")
D24_ANSWER_DOCKET62 = (
    "[what would move it] the nucleation construction run rather than named "
    "(%s, %s here), or the 'find one and enlarge it' route priced; and for "
    "any configuration that changes no topology, the passage from flat "
    "space to it priced at all -- no instrument in the tree does that yet "
    "[owner create.NUCLEATION_STATUS]"
    % (create.NUCLEATION_LITERATURE, create.NUCLEATION_STATUS))

#: THE PRINCIPLE'S OTHER HALF (docstring section 4): a question with no
#: instrument is opened by the docket that builds one.  (question, why it has
#: no row yet, what opens it.)  Printed in LEDGER.md so a deferral is visible.
WAITS_FOR_ITS_INSTRUMENT = []

#: WHAT LEFT WAITS_FOR_ITS_INSTRUMENT, AND HOW.  (question, the docket that
#: built its instrument, the row it became, why it waited -- as first written.)
#: Kept so the deferral stays visible after it ended.
OPENED_FROM_WAITING = [
    ("linearised stability", "DOCKET 64", "D26",
     "no instrument asks it.  Anderson-Molina-Paris-Mottola state the validity "
     "criterion in print (no gauge-invariant perturbation unbounded in time), "
     "and the literature is split on Minkowski itself (AMM: infrared-stable; "
     "Galanda-Meda-Murro-Pinamonti-Schmid 2604.01047: linearly unstable, "
     "attributed to the renormalisation constants) -- as DOCKET 62's ruling "
     "reports them, not read here.  stability.py asks the "
     "CLASSICAL radial stability of a shell, not this.  [DOCKET 67, both "
     "read: AMM's 'completely infrared stable' assumes O(1) fourth-order "
     "coefficients and beta >= 0 and leaves the k = 0 modes untreated; "
     "GMMPS's mode needs alpha~^S_1 != 0, and grows only for alpha~^S_1 > 0]"),
]

#: QUESTIONS THAT NEED M'S RULING, recorded and NOT applied.  This file edits no
#: peer and changes no requirement; it records the question so the board shows
#: it.  (id, question, why it is asked -- with the owner's computed values --,
#: the restatement proposed, and what waits on it.)
#: DOCKET 65's one pending question (M-D65-2, the finite Higgs share) has been
#: RULED by M and is on RULED_BY_M; nothing is pending.
#: DOCKET 66's question for M (spec.py's 'TURN', d66_turn_question) is NOT
#: seated here: specthm.py pins pending_rulings() empty and is not edited by
#: DOCKET 66's seating (no class verdict moved), so the question is carried in
#: O9's DOCKET 66 answer and reported for M (docstring section 8).  M has since
#: ruled it (M-D68-27, "Any crossing"); it was never pending here.
PENDING_RULINGS = []

#: M'S OWN WORDS FOR DOCKET 65's RULINGS, each held ONCE and interpolated into
#: every cell that prints it, so no cell can carry a variant under the label
#: "verbatim" (the selftest extracts every printed copy and compares).
M_D65_1_WORDS = ("consider the idea that the introduction of information into a "
                 "space that never previously contained it would be considered "
                 "exotic matter")
M_D65_1_ANSWER = "Fold into D66"
#: The QET literature as it was named to M, CITED, not READ -- held once.
M_D65_1_LITERATURE = ("Hotta 2008; Funai & Martin-Martinez arXiv:1701.03805; "
                      "Ikeda arXiv:2301.02666; review arXiv:2505.04689; "
                      "arXiv:2506.19878")

#: DOCKET 66 HAS RUN (docstring section 8): what M-S1A-P3's and M-D65-1's cells
#: now say ran, every value asked of the docket66 owners (D66_ASKED, D66_FIG,
#: D66_CENSUS, d66_qet_literature) -- the 'opens' / 'NOT YET RUN' wording each
#: cell first carried is kept in it as history, and the selftest requires both.
#: M-S1A-P3's unblocks cell as first written -- kept, and followed by what ran.
M_S1A_P3_UNBLOCKS_AS_FIRST_WRITTEN = (
    "the seat of every object must be free of a closed causal curve and a pathology; "
    "the throat-creation classes stay OPEN; DOCKET 66 opens")


def d66_p3_ran():
    """What M-S1A-P3's unblocks cell says DOCKET 66 did, asked."""
    lb = D66_CENSUS["load-bearing"]
    return (
        "wave 1, verified both ways, fixed (D66-fix) and seated (docstring section 8).  "
        "(i): the throat-creation classes stay OPEN for every D66 throat (O-MAKE-TOPO %s); "
        "the seat condition reads %s (combine66).  (ii) stays NOT applied, H-DEFECT-SEAT "
        "carried as M's hypothesis: a defect seat supplies no matter (O-SEAT %s), and "
        "load-bearing D66 removals number %s in %s consistent variants at 1 ly (READ, "
        "B-combine66.md); O9 and the S5 and S13 notes carry it"
        % (d66_group(("H-DEFECT-SEAT: string-supported throat (DTHR)", "H-THROAT-BITS: R-HOLO (TBHOLO)",
                      "H-THROAT-BITS: R-THINSHELL (TBTSH)", "H-THROAT-BITS: R-TELEPORT (TBTEL)"),
                     "O-MAKE-TOPO"),
           d66_group(D66_DEFECT_SEATS, "SEAT"), d66_group(D66_DEFECT_SEATS, "O-SEAT"),
           lb[0], lb[1]))


def d66_m_d65_1_ran():
    """What M-D65-1's ruling cell says DOCKET 66 did with QET, asked."""
    lit = d66_qet_literature()
    return (
        "wave 1 run, verified both ways, fixed and seated (docstring section 8).  The "
        "literature named to M is READ by qet.py (route: %s), each item heading an entry "
        "of its sources: %s.  The question's "
        "parenthetical, tested, is INEXACT: after the bit arrives and before the "
        "conditioned operation the local energy at the seat is %s (qet.post_alice, |E| < "
        "1e-12: %s); R-QET, the operational reading, is %s and R-LIT, the parenthetical "
        "read as arrival alone, %s (qet.grades).  As a hold QET is %s, OPEN via N_QETHAD "
        "alone; as a supply %s (O9; S5's note)"
        % (D66_QET_ROUTE, "; ".join("%s: READ (%s)" % (i, e.split(",")[0]) for i, e in lit),
           _d66_e(D66_FIG["QET arrival alone"], 1), abs(D66_FIG["QET arrival alone"]) < 1e-12,
           D66_FIG["R-QET own content"].split(";")[0], D66_FIG["R-LIT own content"].split(":")[0],
           D66_FIG["R-QET O-HOLD head"], D66_FIG["R-QET O-SEAT head"]))


#: M-D65-1's ruling cell, a TEMPLATE filled from the asked constants (the
#: selftest requires EQUALITY): M's answer, M's words, the literature as named
#: to M, and what DOCKET 66 ran (d66_m_d65_1_ran).  FIRST APPLIED (kept): the
#: cell as DOCKET 65's seating wrote it, ending 'QET is to be tested inside
#: DOCKET 66 (NOT YET RUN)'.
M_D65_1_RULING_T = (
    "RULED BY M: FOLD INTO DOCKET 66 -- M's answer: '%s'.  M's words, verbatim: '%s'.  "
    "The QET literature (%s) was CITED, not READ, when M ruled; the question's "
    "parenthetical is the question's description as put to M, not READ.  APPLIED: no "
    "separate docket and no row; QET IS TESTED inside DOCKET 66: %s.  FIRST APPLIED "
    "(kept): QET is to be tested inside DOCKET 66 (NOT YET RUN)")
#: The ruling cell as DOCKET 65's seating wrote it -- history, re-derived by the
#: selftest's control (the old cell must now be caught).
M_D65_1_RULING_AS_FIRST_WRITTEN_T = (
    "RULED BY M: FOLD INTO DOCKET 66 -- M's answer: '%s'.  M's words, verbatim: '%s'.  "
    "The QET literature (%s) is CITED, not READ; the question's parenthetical is the "
    "question's description as put to M, not READ.  APPLIED: no separate docket and no "
    "row; QET is to be tested inside DOCKET 66 (NOT YET RUN)")
M_D65_1_UNBLOCKS_AS_FIRST_WRITTEN = ("DOCKET 66 (NOT YET RUN) is to test QET beside seating "
                                     "at a topological defect")
#: M-D65-3 (DOCKET 67): the question exactly as it was put to M, M's words
#: verbatim -- they hold apostrophes, so every cell quotes them in double
#: quotes -- and M's answer verbatim.  PROVENANCE: M_D65_3_WORDS is verbatim
#: from the session, witnessed by the lead against the transcript; the tree
#: holds no copy of M's message, so nothing here can verify the constant
#: against M -- the selftest checks every printed copy against it, no more.
M_D65_3_QUESTION = ("Should I open a docket auditing the external results the "
                    "board's refusals rest on (theorem / measurement / "
                    "extrapolation; hypotheses, the data each used, re-derived "
                    "or machine-checked, graded STANDS / NARROWED / WRONG / "
                    "DATA-DEPENDENT)? If so, when?")
M_D65_3_WORDS = ("I didn't expect proving warp theory travel easy, but I'm "
                 "starting suspect that some of the previously established math "
                 "from outside art may be inaccurate or incomplete, or even "
                 "wrong. My justification is that some previous physicists may "
                 "have all lacked certain data")
M_D65_3_ANSWER = "After D65, before D66"
#: M-D65-3's ruling cell, a TEMPLATE over (M_D65_3_ANSWER, M_D65_3_WORDS): the
#: selftest checks the seated cell EQUALS the template filled from the
#: constants, so no verdict on DOCKET 67 can be typed beside them.
M_D65_3_RULING_T = ("RULED BY M: OPEN IT -- M's answer: '%s'.  M's words, "
                    'verbatim: "%s".  APPLIED: DOCKET 67 is opened on '
                    "specthm's DOCKETS_OPENED, NOT YET RUN; no row here")
#: M-D65-3's `why` cell, a TEMPLATE filled by m_d65_3_why() from the owners'
#: own records (fluctuation.py, massform.py): the characterisation is theirs,
#: the figures are asked, and the lead-in's COUNTS are asked too -- the
#: discrepancies fluctuation.py records are COUNTED from its KF flags
#: (fluctuation_discrepancies()), the divergences massform.py records are the
#: sentences under its own heading (massform_divergences()), the nouns are
#: regexed from the owners ('discrepancies', 'refuted', 'typographical',
#: 'divergences'), and the 'N of' numerators are len() of the tuples naming
#: the items the cell details -- tuples TIED to the cell by the selftest:
#: every fluct member is printed as 'fluctuation.<flag> = ' and no other KF_
#: flag is, and every mass label is a
#: substring of the cell naming exactly one sentence under massform's heading
#: by its subject.  The framing is SCOPED to what the cell cites, not
#: a project-wide total (hpscentre.py counts three disagreements of its own).
#: Precedent: hpscentre.py withdrew a typed 'two misprints and two errors'
#: for its asked 'three disagreements'.
M_D65_3_WHY_ITEMS_FLUCT = ("KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1", "KF_341_HALF_IS_TYPOGRAPHICAL",
                           "KF_QUALITATIVE_CONCLUSION_SURVIVES")
M_D65_3_WHY_ITEMS_MASS = ("Rubakov-Shaposhnikov's eq. (2.8)", "Tye-Wong's p.2 pairing")
M_D65_3_WHY_T = (
    'M\'s words, verbatim: "%s" (verbatim from the session, witnessed by the '
    "lead; the tree holds no copy to check them against).  Of what this project "
    "has recorded against outside results, the items whose owners expose flags "
    "asked here: %d of the %d %s fluctuation.py records against a preprint "
    "version (its own words: the inequality after (3.8) %s -- \"%s\" -- and "
    "(3.41)'s 1/2 \"%s\"; their qualitative conclusion, below; the rest, %d "
    "KF_*_IS_EXACT flags False), and %d of "
    "the %d %s massform.py records under its own heading.  "
    "fluctuation.py, against arXiv %s -- the journal version, %s, is %s "
    "(fluctuation.JOURNAL_VERSION_READ = %s), and its own clause holds: '%s': "
    "Kuo & Ford's printed 'rho < 0 => Delta > 1' is %s (fluctuation.KF_CLAIM_"
    "NEGATIVE_MEANS_DELTA_GT_1 = %s) and the 1/2 their eq. (3.41) prints where "
    "1/4 holds is %s (fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL = %s).  "
    "massform.py, under its own heading '%s': Rubakov-Shaposhnikov's eq. (2.8) "
    "prints 10^%.0f at alpha_W = 1/%g where the arithmetic gives 10^%.2f "
    "(massform.RS96_PRINTED_LOG10, RS96_ALPHA_INV, log10_suppression); "
    "Tye-Wong's p.2 pairing prints 10^%.0f at alpha_W ~ 1/%g where the "
    "arithmetic gives 10^%.2f, %.2f decades off, and their p.7 pairing, "
    "1/%g, gives 10^%.2f, which %s the printed figure (massform.TW_PRINTED_"
    "LOG10, TW_ALPHA_INV, log10_suppression).  Kuo & Ford's qualitative "
    "conclusion %s (fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = %s) and "
    "%s (fluctuation.LEDGER_ROW_MOVES = %s)")
#: M-D65-4: the paper's caveat (b).  The question exactly as it was put to M
#: and M's answer verbatim -- both verbatim from the session, witnessed by
#: the lead; the tree holds no copy to check them against.  The clause the paper carries is
#: held once and READ back from paper/CLAIMS.md by paper_caveat_b_faults().
M_D65_4_QUESTION = ("The paper's caveat (b) states the Higgs vacuum's uniformity "
                    "as fact; the tree now carries it as a named premise "
                    "(P-UNIFORM). Does that count as a finding that changes the "
                    "paper?")
M_D65_4_ANSWER = "Yes, qualify it (Recommended)"
PAPER_CAVEAT_B_LINE = 7228
PAPER_CAVEAT_B_CLAUSE = ("on P-UNIFORM, a named premise (`massform.P_UNIFORM_STATUS`; "
                         "DOCKET 65, ruling M-D65-4)")
PAPER_CAVEAT_B_HEAD = "- **(b) It is uniform where nothing sources it**"
#: M's RULE FOR THE PAPER, M's words verbatim.  PROVENANCE: verbatim from the
#: session, witnessed by the lead; the tree holds no copy to check them
#: against.  M said it BEFORE DOCKET 63's paper edit (commit 524ccae,
#: 2026-09-24, applied on M's ruling under this same rule), which the paper
#: marks at PAPER_D63_MARKER_LINE -- the tree witnesses that marker by READING
#: it (paper_d63_marker()), so the DOCKET 65 edit is not the paper's only
#: edit on M's ruling: the paper marks the edits these rows name (DOCKET 65's
#: at PAPER_CAVEAT_B_LINE, DOCKET 63's at PAPER_D63_MARKER_LINE); its other
#: DOCKET markers are asked by paper_docket_markers() and printed in
#: M-D65-5's cell; this file names them and counts none.  Since M-D65-5 put
#: the ruling id into the paper's clause, M_D65_4_RULING_T's "the paper's
#: other marked edit on M's ruling is DOCKET 63's" is what the paper's own
#: markers said when M ruled M-D65-4: the selftest asked paper_docket_markers()
#: which markers name a ruling, and the answer was those at PAPER_CAVEAT_B_LINE
#: and inside the DOCKET 63 marker, no other.  CORRECTED (DOCKET 67
#: follow-ups): the paper's DOCKET 67 corrections are marked '(Corrected on
#: M's "Repair all", DOCKET 67: ...)' -- M's ruling named by M's quoted words,
#: not by the word 'ruling', so the census first READ them as naming none.
#: paper_docket_markers() now reads M's quoted words before the docket token
#: (PAPER_M_QUOTED_RULING_RE) as a ruling named; the selftest asks which of
#: the paper's DOCKET 67 tokens carry that form, and the template below keeps
#: M-D65-4's sentence as it stood, with the correction after it.
M_PAPER_RULE_WORDS = ("the paper is finalized and in the website now. No further "
                      "edit will be made to it unless a finding changes any of the "
                      "already existing paper")
#: paper/CLAIMS.md's DOCKET 63 marker starts on this line and runs to the
#: close of its parenthesis (two lines in the paper); both fragments
#: '(Corrected on M's ruling:' and 'DOCKET 63' must sit inside the same marker,
#: and the regex, never a typed copy, supplies the quoted text.
PAPER_D63_MARKER_LINE = 7233
PAPER_D63_MARKER_RE = re.compile(r"\(Corrected on M's ruling:.*?DOCKET 63\.\)", re.S)
#: M-D65-4's ruling cell, a TEMPLATE over (M's answer, the caveat line and
#: clause, M's rule for the paper, the DOCKET 63 marker's lines and text):
#: the paper's edits on M's ruling are NAMED by their markers, never counted.
M_D65_4_RULING_T = ("RULED BY M: YES, QUALIFY IT -- M's answer: '%s'.  APPLIED: "
                    'paper/CLAIMS.md:%d caveat (b) carries "%s" (as it now reads; the '
                    "ruling id was added on M-D65-5) -- a paper edit on "
                    "M's ruling under M's rule for the paper (\"%s\", verbatim from "
                    "the session, witnessed by the lead); the paper's other marked "
                    "edit on M's ruling is DOCKET 63's (paper/CLAIMS.md:%s: \"%s\") "
                    "-- so it stood when M ruled.  CORRECTED (DOCKET 67 follow-ups): "
                    "the paper has since carried DOCKET 67's markers, '" +
                    "(Corrected on M's \"Repair all\", DOCKET 67: ...)', which name "
                    "M's ruling \"Repair all\" by M's words; M-D65-5's census READs "
                    "them.  CORRECTED (DOCKET 67 close): the M's words the paper's "
                    "DOCKET 67 marker heads carry, READ from the paper: %s")
M_D65_4_UNBLOCKS_T = ("nothing; M's rule for the paper stands (\"%s\", verbatim from "
                      "the session, witnessed by the lead)")
#: M-D65-4's `why` cell, a TEMPLATE over (the caveat line, massform's asked
#: status): the selftest checks the seated cell EQUALS it, so no verdict on
#: the paper can be typed beside the finding.
M_D65_4_WHY_T = ("The completeness lens's finding: paper/CLAIMS.md:%d caveat (b) "
                 "stated 'It is uniform where nothing sources it' as fact; massform "
                 "seats it as P-UNIFORM (massform.P_UNIFORM_STATUS = %s).  The "
                 "question and M's answer are verbatim from the session, witnessed "
                 "by the lead; the tree holds no copy to check them against")
#: M-D65-5: the ruling id in the paper's clause.  The question exactly as the
#: lead put it to M and M's answer verbatim -- both verbatim from the session,
#: witnessed by the lead; the tree holds no copy to check them against.
M_D65_5_QUESTION = ("One item is yours, not the board's: the paper's new clause at "
                    "CLAIMS.md:7228 names \"DOCKET 65\" but not the ruling id "
                    "M-D65-4, unlike the DOCKET 63 marker at line 7233. Leaving it "
                    "as you ruled unless you want the id added.")
M_D65_5_ANSWER = "add the id"
M_D65_5_WHY = ("the lenses' finding of rounds 6-7: the paper marked DOCKET 65's "
               "edit by docket only, so the paper itself did not say the edit was "
               "ruled -- that record lived in ledger.py, LEDGER.md and higgs.py")
#: The tail of M-D65-5's ruling cell, shared with specthm's SR5 through
#: paper_markers_clause(): a TEMPLATE over (the caveat line, the DOCKET 63
#: marker's lines READ back, the paper's DOCKET markers READ by
#: paper_docket_markers()).  The markers the rows name are named; the paper's
#: markers are printed as the paper carries them, and the reader counts.
PAPER_MARKERS_CLAUSE_T = ("the markers these rows name each name a ruling (M-D65-4 at "
                          "%d; 'on M's ruling', DOCKET 63 at %s); the paper's DOCKET "
                          "markers, READ: %s")
#: M-D65-5's ruling cell, a TEMPLATE over (M's answer, the caveat line and
#: clause, then PAPER_MARKERS_CLAUSE_T's pieces): the selftest checks the
#: seated cell EQUALS it, so no verdict can be typed beside it.
M_D65_5_RULING_T = ("RULED BY M: ADD THE ID -- M's answer: '%s'.  APPLIED: "
                    "paper/CLAIMS.md:%d's clause now reads \"%s\" (READ back by "
                    "paper_caveat_b_faults()); " + PAPER_MARKERS_CLAUSE_T)
#: A DOCKET marker in the paper: the word and its number.
PAPER_DOCKET_MARKER_RE = re.compile(r"DOCKET (\d+)")
#: M's ruling named by M's quoted words immediately before a docket token --
#: the paper's DOCKET 67 markers read '(Corrected on M's "Repair all", DOCKET
#: 67: ...)'.  Matched against the line up to the token (DOCKET 67
#: follow-ups); a docket mentioned later inside such a marker is not its
#: docket and is not matched.
PAPER_M_QUOTED_RULING_RE = re.compile(r"\bM's \"[^\"]+\", $")
#: The head of the paper's DOCKET 67 markers, READ in the selftest.
PAPER_D67_MARKER_HEAD = "(Corrected on M's \"Repair all\", DOCKET 67:"
#: CORRECTED (DOCKET 67 close, on M's rulings "Carry both" and "Re-size to 4544
#: m"): the paper's DOCKET 67 markers no longer all carry "Repair all" -- the
#: closing rulings' corrections are marked with M's words for those rulings.
#: PAPER_D67_MARKER_HEAD stays the head as first written, kept and still checked
#: (RECORD); the census READs the general head -- any of M's quoted words --
#: by PAPER_D67_MARKER_HEAD_RE (group 1 is M's words), and paper_d67_words()
#: lists the words the paper carries, READ, never typed.
PAPER_D67_MARKER_HEAD_AS_FIRST_WRITTEN = PAPER_D67_MARKER_HEAD
PAPER_D67_MARKER_HEAD_RE = re.compile(r"\(Corrected on M's \"([^\"]+)\", DOCKET 67:")
#: the general head as printed in labels: M's words left as a slot
PAPER_D67_MARKER_HEAD_FORM = "(Corrected on M's \"<M's words>\", DOCKET 67:"
#: M's quoted words immediately before ', DOCKET 67' -- what the CONTROL strips
PAPER_D67_M_WORDS_RE = re.compile(r"M's \"[^\"]+\", DOCKET 67")
#: A COUNT of the paper's edits or markers in this board's own words -- what
#: the selftests forbid in the M-D65-4 / M-D65-5 cells, the docstring, the
#: source region around them and specthm's SR5: the items are NAMED and the
#: paper's census is ASKED (paper_docket_markers()); nothing counts them.
#: One vocabulary, here, imported by specthm rather than copied.
COUNT_RE = re.compile(
    r"\b(the one|the second|both|all|every|the only|"
    r"(?:the |all |each of the )?(?:two|three|four|five|six|seven|eight|nine|ten|"
    r"eleven|twelve)|(?<!DOCKET )\d+) (?:of the paper's )?(paper |marked |DOCKET )?"
    r"(edits?|markers?)\b")  # a docket's own number ('DOCKET 63 marker') is not a count
#: M-D65-2's question exactly as it was put to M, and M's answer verbatim.
M_D65_2_QUESTION = ("The finite Higgs share (how much of atomic mass the Higgs "
                    "gives with the field switched off entirely): keep it as its "
                    "own open row O8, or record it inside S10's note as the "
                    "approved proposal had it?")
M_D65_2_ANSWER = "Fold into S10 (Recommended)"
#: Two fragments of the option M chose, as it was described to M (verbatim).
M_D65_2_OPTION = ("an open item inside S10's note, not a separate row",
                  "It stays a named candidate for a future docket")

def _owner_phrase(doc, pattern, owner):
    """A phrase READ out of an owner's own docstring by regex, never retyped;
    raises if the owner no longer says it."""
    m = re.search(pattern, " ".join(doc.split()))
    if not m:
        raise ValueError("%s no longer records '%s'" % (owner, pattern))
    return m.groups() if m.re.groups > 1 else m.group(1)


def fluctuation_discrepancies():
    """The discrepancies fluctuation.py records against the preprint version,
    COUNTED from its module namespace: every KF_*_IS_EXACT flag that is False,
    plus KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 False, plus
    KF_341_HALF_IS_TYPOGRAPHICAL True, plus KF_QUALITATIVE_CONCLUSION_SURVIVES
    False (DOCKET 67).  Returns (total, not-exact count)."""
    not_exact = sum(1 for k, v in vars(fluctuation).items()
                    if k.startswith("KF_") and k.endswith("_IS_EXACT") and v is False)
    total = (not_exact + (fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 is False)
             + (fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL is True)
             + (fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES is False))
    return total, not_exact


def massform_divergences():
    """[sentence] of the paragraph under massform.py's own heading
    'DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED', split by regex
    at a full stop followed by whitespace; the owner's count is len()."""
    m = re.search(r"DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED\.\s*"
                  r"(.*?)\n[ \t]*\n", massform.__doc__, re.S)
    if not m:
        raise ValueError("massform.py no longer carries its divergences paragraph")
    return [s for s in re.split(r"(?<=\.)\s+", " ".join(m.group(1).split())) if s]


def m_d65_3_why():
    """M-D65-3's `why` cell, built from the owners' own records: the counts
    and nouns of the lead-in (fluctuation_discrepancies(),
    massform_divergences(), the owners' own words by regex), the preprint
    version fluctuation.py checked and its clause on the journal version, the
    KF flags the cell details; massform.py's own heading and the divergences
    the cell details (the items M_D65_3_WHY_ITEMS_FLUCT / _MASS name, each
    guarded present in the cell), with Tye-Wong's p.7 pairing printed beside
    the p.2 one; and fluctuation.py's verdict on Kuo & Ford's qualitative
    conclusion (DOCKET 67: it does not survive), asked of its flags."""
    n_fluct, n_not_exact = fluctuation_discrepancies()
    n_mass = len(massform_divergences())
    with open(fluctuation.__file__, encoding="utf-8") as fh:
        fluct_src = fh.read()
    discrepancies = _owner_phrase(
        fluctuation.__doc__, r"the (discrepancies) above are against v1", "fluctuation.py")
    refuted = _owner_phrase(
        fluct_src, r"KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 = False\s+# (refuted)",
        "fluctuation.py")
    typographical = _owner_phrase(
        " ".join(k for k in vars(fluctuation) if k.startswith("KF_")),
        r"KF_341_HALF_IS_(TYPOGRAPHICAL)", "fluctuation.py").lower()
    false_by_z3 = "%s by %s" % _owner_phrase(
        fluctuation.__doc__, r"that is (FALSE), and (z3) finds the counterexample",
        "fluctuation.py")
    divergences = _owner_phrase(
        massform.__doc__, r"(DIVERGENCES) FROM THE SOURCES, RECORDED AND NOT REPAIRED",
        "massform.py").lower()
    preprint = _owner_phrase(fluctuation.SOURCE, r"(gr-qc/\d+ v\d)", "fluctuation.SOURCE")
    journal, jstatus = _owner_phrase(
        fluctuation.__doc__,
        r"The published version, (Phys\. Rev\. D 47, 4510 \(1993\)), is ([A-Z-]+)",
        "fluctuation.py")
    if jstatus != ("READ" if fluctuation.JOURNAL_VERSION_READ else
                   "COMPARED-BY-M" if fluctuation.JOURNAL_VERSION_COMPARED_BY_M
                   else "NAMED-NOT-READ"):
        raise ValueError("fluctuation.py's docstring and its journal-version flags disagree")
    clause = _owner_phrase(
        fluctuation.__doc__,
        r"(they carry to the journal version on M's comparison, "
        r"not on this file's reading)",
        "fluctuation.py")
    heading = _owner_phrase(
        massform.__doc__, r"(DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED)",
        "massform.py")
    not_survive = "fluctuation.py: \"%s\"" % _owner_phrase(
        fluctuation.__doc__,
        r"(a displaced squeezed state carries negative energy with Delta = 0 \(section 2\))",
        "fluctuation.py")
    tw_p2 = massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1])
    tw_p7 = massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[0])
    return M_D65_3_WHY_T % (
        M_D65_3_WORDS,
        len(M_D65_3_WHY_ITEMS_FLUCT), n_fluct, discrepancies, false_by_z3, refuted,
        typographical, n_not_exact, len(M_D65_3_WHY_ITEMS_MASS), n_mass, divergences,
        preprint, journal, jstatus, fluctuation.JOURNAL_VERSION_READ,
        clause,
        ("FALSE by z3" if not fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1
         else "NOT refuted, AGAINST fluctuation.py's record"),
        fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1,
        ("typographical" if fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL
         else "NOT typographical, AGAINST fluctuation.py's record"),
        fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL,
        heading,
        massform.RS96_PRINTED_LOG10, massform.RS96_ALPHA_INV,
        massform.log10_suppression(1.0 / massform.RS96_ALPHA_INV),
        massform.TW_PRINTED_LOG10, massform.TW_ALPHA_INV[1], tw_p2,
        abs(tw_p2 - massform.TW_PRINTED_LOG10),
        massform.TW_ALPHA_INV[0], tw_p7,
        ("rounds to" if round(tw_p7) == massform.TW_PRINTED_LOG10
         else "does NOT round to"),
        # Built from the owner's flags, so a flip moves the sentence.
        ("SURVIVES" if fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES
         else "does NOT survive -- %s" % not_survive),
        fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES,
        ("no ledger row moves" if not fluctuation.LEDGER_ROW_MOVES
         else "a ledger row MOVES, AGAINST fluctuation.py's record"),
        fluctuation.LEDGER_ROW_MOVES)


def _paper_lines(path=None):
    path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper", "CLAIMS.md")
            if path is None else path)
    with open(path, encoding="utf-8") as fh:
        return fh.read().split("\n")


def paper_d63_marker(lines=None):
    """(lines, text) of the paper's DOCKET 63 marker, READ from paper/CLAIMS.md
    by PAPER_D63_MARKER_RE starting at PAPER_D63_MARKER_LINE: 'lines' is
    '7233-7234' as the marker spans them, 'text' the marker itself with its
    whitespace joined.  Raises if the marker is not there: the tree witnesses
    it only by reading it."""
    lines = _paper_lines() if lines is None else lines
    tail = lines[PAPER_D63_MARKER_LINE - 1:PAPER_D63_MARKER_LINE + 3]
    m = PAPER_D63_MARKER_RE.search("\n".join(tail))
    if not m or "\n" in "\n".join(tail)[:m.start()]:
        raise ValueError("paper/CLAIMS.md:%d does not start the DOCKET 63 marker "
                         "'(Corrected on M's ruling: ... DOCKET 63.)'"
                         % PAPER_D63_MARKER_LINE)
    end = PAPER_D63_MARKER_LINE + "\n".join(tail)[:m.end()].count("\n")
    span = ("%d" % PAPER_D63_MARKER_LINE if end == PAPER_D63_MARKER_LINE
            else "%d-%d" % (PAPER_D63_MARKER_LINE, end))
    return span, " ".join(m.group(0).split())


def paper_d63_faults(lines=None):
    """[fault] where the paper no longer carries DOCKET 63's marker at
    PAPER_D63_MARKER_LINE with both fragments inside it."""
    try:
        _span, text = paper_d63_marker(lines)
    except ValueError as e:
        return [str(e)]
    return [f for f in ("marker lacks '(Corrected on M's ruling:'"
                        if "(Corrected on M's ruling:" not in text else "",
                        "marker lacks 'DOCKET 63'" if "DOCKET 63" not in text else "")
            if f]


def _marker_text(lines, i, pos=0):
    """The text a DOCKET marker on line i (1-based), at column pos, belongs to:
    the innermost parenthetical enclosing that token when one opens or closes
    on the line before or after (the DOCKET 63 marker's parenthesis closes on
    a later line than it opens -- its span is READ by paper_d63_marker()),
    else the line itself.  Read out of the paper's lines, nothing typed; the
    token is the one at pos, not the first 'DOCKET' on the line."""
    lo = max(0, i - 2)
    joined = "\n".join(lines[lo:i + 1])
    off = sum(len(l) + 1 for l in lines[lo:i - 1])
    tok = off + pos
    depth, opener = 0, None
    for k in range(tok - 1, -1, -1):
        if joined[k] == ")":
            depth += 1
        elif joined[k] == "(":
            if depth == 0:
                opener = k
                break
            depth -= 1
    if opener is None:
        return lines[i - 1]
    depth = 0
    for k in range(tok, len(joined)):
        if joined[k] == "(":
            depth += 1
        elif joined[k] == ")":
            if depth == 0:
                return joined[opener:k + 1]
            depth -= 1
    return lines[i - 1]


def paper_docket_markers(lines=None):
    """{docket: [(line, ruling_named)]} -- every 'DOCKET <n>' the paper carries,
    READ from paper/CLAIMS.md by PAPER_DOCKET_MARKER_RE with its line number,
    and for each whether a ruling is named: the word 'ruling' in the marker's
    own text (_marker_text(): the enclosing parenthetical, or the line), or
    M's quoted words immediately before the token (PAPER_M_QUOTED_RULING_RE,
    the DOCKET 67 form '(Corrected on M's "Repair all", DOCKET 67: ...)' --
    CORRECTED, DOCKET 67 follow-ups: the census first read only the word, and
    printed those markers as naming none).  Asked, never typed: a marker
    added to or dropped from the paper moves the census."""
    lines = _paper_lines() if lines is None else lines
    out = {}
    for i, line in enumerate(lines, 1):
        for m in PAPER_DOCKET_MARKER_RE.finditer(line):
            named = (bool(re.search(r"\bruling\b", _marker_text(lines, i, m.start()), re.I))
                     or bool(PAPER_M_QUOTED_RULING_RE.search(line[:m.start()])))
            out.setdefault(int(m.group(1)), []).append((i, named))
    return out


def paper_docket_markers_clause(lines=None):
    """The census paper_docket_markers() returns, printed docket by docket:
    'DOCKET <n> at <line>, <line> (no ruling named in those markers); DOCKET
    <m> at <line> (a ruling named); ...' -- the parenthetical computed from
    the per-marker flags, so the reader counts and this file does not."""
    parts = []
    for d, sites in sorted(paper_docket_markers(lines).items()):
        named = [l for l, r in sites if r]
        unnamed = [l for l, r in sites if not r]
        if not unnamed:
            what = "a ruling named"
        elif not named:
            what = "no ruling named in %s" % ("those markers" if len(sites) > 1
                                              else "that marker")
        else:
            what = "a ruling named in the markers at %s; none in those at %s" % (
                ", ".join("%d" % l for l in named), ", ".join("%d" % l for l in unnamed))
        parts.append("DOCKET %d at %s (%s)" % (d, ", ".join("%d" % l for l, _r in sites),
                                               what))
    return "; ".join(parts) or "none"


def paper_markers_clause():
    """PAPER_MARKERS_CLAUSE_T filled from the caveat line, the DOCKET 63
    marker's lines READ back and the paper's DOCKET markers READ -- the tail
    of M-D65-5's ruling cell, and SR5's clause in specthm."""
    try:
        span = paper_d63_marker()[0]
    except ValueError as e:
        # The board still imports; the selftest goes red on paper_d63_faults().
        span = "%d (MARKER NOT FOUND -- %s)" % (PAPER_D63_MARKER_LINE, e)
    return PAPER_MARKERS_CLAUSE_T % (PAPER_CAVEAT_B_LINE, span, paper_docket_markers_clause())


def paper_d67_words(lines=None):
    """M's quoted words in the paper's DOCKET 67 marker heads, in order of
    first appearance, READ by PAPER_D67_MARKER_HEAD_RE (DOCKET 67 close)."""
    lines = _paper_lines() if lines is None else lines
    out = []
    for line in lines:
        for m in PAPER_D67_MARKER_HEAD_RE.finditer(line):
            if m.group(1) not in out:
                out.append(m.group(1))
    return out


def paper_d67_words_clause(lines=None):
    """paper_d67_words() printed as the paper carries them: '"w1", "w2"'."""
    return ", ".join('"%s"' % w for w in paper_d67_words(lines)) or "none"


#: The head of the paper's DOCKET 68 markers, read as DOCKET 67's are
#: (PAPER_D67_MARKER_HEAD_RE): group 1 is M's quoted words.  ADDED with
#: M-D68-12 and M-D68-13 (M-RULINGS-2026-10-03.md items 12-13), the rulings
#: on the paper whose corrections carry it.
PAPER_D68_MARKER_HEAD_RE = re.compile(r"\(Corrected on M's \"([^\"]+)\", DOCKET 68:")


def paper_d68_words(lines=None):
    """M's quoted words in the paper's DOCKET 68 marker heads, in order of
    first appearance, READ by PAPER_D68_MARKER_HEAD_RE."""
    lines = _paper_lines() if lines is None else lines
    out = []
    for line in lines:
        for m in PAPER_D68_MARKER_HEAD_RE.finditer(line):
            if m.group(1) not in out:
                out.append(m.group(1))
    return out


def paper_d68_marker(words, lines=None):
    """(line, marker text) of the paper's DOCKET 68 marker whose head carries
    M's `words`, READ from paper/CLAIMS.md: the line of its head and the whole
    parenthetical (_marker_text, as the census reads it).  (None, 'MARKER NOT
    FOUND ...') if no head carries those words -- the board still imports, and
    the selftest goes red."""
    lines = _paper_lines() if lines is None else lines
    for i, line in enumerate(lines, 1):
        for m in PAPER_D68_MARKER_HEAD_RE.finditer(line):
            if m.group(1) == words:
                pos = line.index("DOCKET 68", m.start())
                return i, " ".join(_marker_text(lines, i, pos).split())
    return None, "MARKER NOT FOUND -- no DOCKET 68 marker head carries M's words %s" % words


#: The head of the paper's DOCKET 66 markers, read as DOCKET 67's and 68's are
#: (group 1 is M's quoted words).  ADDED with M-D68-26 (M-RULINGS-2026-10-03.md
#: item 26, one of M's DOCKET 66 rulings: "Correct it (Recommended)" on the
#: paper's Gott pair bound), whose correction the lead applied in
#: paper/CLAIMS.md under this head.  The census (paper_docket_markers) already
#: READs the token as naming a ruling by M's quoted words before it
#: (PAPER_M_QUOTED_RULING_RE); this head ties that reading to the marker, as
#: PAPER_D68_MARKER_HEAD_RE does for DOCKET 68, and the selftest's control
#: strips M's words from it in a private copy.
PAPER_D66_MARKER_HEAD_RE = re.compile(r"\(Corrected on M's \"([^\"]+)\", DOCKET 66:")


def paper_d66_words(lines=None):
    """M's quoted words in the paper's DOCKET 66 marker heads, in order of
    first appearance, READ by PAPER_D66_MARKER_HEAD_RE."""
    lines = _paper_lines() if lines is None else lines
    out = []
    for line in lines:
        for m in PAPER_D66_MARKER_HEAD_RE.finditer(line):
            if m.group(1) not in out:
                out.append(m.group(1))
    return out


def paper_d66_marker(words, lines=None):
    """(line, marker text) of the paper's DOCKET 66 marker whose head carries
    M's `words`, READ from paper/CLAIMS.md exactly as paper_d68_marker() reads
    DOCKET 68's.  (None, 'MARKER NOT FOUND ...') if no head carries them."""
    lines = _paper_lines() if lines is None else lines
    for i, line in enumerate(lines, 1):
        for m in PAPER_D66_MARKER_HEAD_RE.finditer(line):
            if m.group(1) == words:
                pos = line.index("DOCKET 66", m.start())
                return i, " ".join(_marker_text(lines, i, pos).split())
    return None, "MARKER NOT FOUND -- no DOCKET 66 marker head carries M's words %s" % words


def paper_d66_first_wording(words, lines=None):
    """The paper's own first wording inside its DOCKET 66 marker ('first
    written "..."'), READ from the marker paper_d66_marker() returns; None if
    the marker or the phrase is not there."""
    _line, text = paper_d66_marker(words, lines)
    m = re.search(r'first written "([^"]+)"', text)
    return m.group(1) if m and _line is not None else None


def m_d65_4_ruling():
    """M-D65-4's ruling cell: M_D65_4_RULING_T filled from M's answer, the
    caveat's line and clause, M's rule for the paper and the DOCKET 63 marker
    READ back from the paper -- the marked edits this file names (DOCKET 65's,
    DOCKET 63's) named, none counted."""
    try:
        span, text = paper_d63_marker()
    except ValueError as e:
        # The board still imports; the selftest goes red on paper_d63_faults().
        span, text = "%d" % PAPER_D63_MARKER_LINE, "MARKER NOT FOUND -- %s" % e
    return M_D65_4_RULING_T % (M_D65_4_ANSWER, PAPER_CAVEAT_B_LINE, PAPER_CAVEAT_B_CLAUSE,
                               M_PAPER_RULE_WORDS, span, text, paper_d67_words_clause())


def m_d65_4_why():
    """M-D65-4's `why` cell, M_D65_4_WHY_T filled from the caveat's line and
    massform's asked status."""
    return M_D65_4_WHY_T % (PAPER_CAVEAT_B_LINE, massform.P_UNIFORM_STATUS)


def m_d65_5_ruling():
    """M-D65-5's ruling cell: M_D65_5_RULING_T filled from M's answer, the
    caveat's line and clause (READ back by paper_caveat_b_faults()), the
    DOCKET 63 marker's lines READ back from the paper and the paper's DOCKET
    markers READ (paper_docket_markers()) -- the cell ends in
    paper_markers_clause()."""
    try:
        span = paper_d63_marker()[0]
    except ValueError as e:
        # The board still imports; the selftest goes red on paper_d63_faults().
        span = "%d (MARKER NOT FOUND -- %s)" % (PAPER_D63_MARKER_LINE, e)
    return M_D65_5_RULING_T % (M_D65_5_ANSWER, PAPER_CAVEAT_B_LINE, PAPER_CAVEAT_B_CLAUSE,
                               PAPER_CAVEAT_B_LINE, span, paper_docket_markers_clause())


def paper_caveat_b_line(path=None):
    """paper/CLAIMS.md's line PAPER_CAVEAT_B_LINE, READ from the file."""
    path = (os.path.join(os.path.dirname(os.path.abspath(__file__)), "paper", "CLAIMS.md")
            if path is None else path)
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    return lines[PAPER_CAVEAT_B_LINE - 1]


def paper_caveat_b_faults(line=None):
    """[fault] where the paper's caveat (b) (paper/CLAIMS.md:PAPER_CAVEAT_B_LINE)
    does not carry the clause M-D65-4 applied, or still states the premise as
    fact (the wording as it stood: 'It is uniform where nothing sources it.**
    The same inside')."""
    line = paper_caveat_b_line() if line is None else line
    bad = []
    if not line.startswith(PAPER_CAVEAT_B_HEAD):
        bad.append("line %d is not caveat (b)" % PAPER_CAVEAT_B_LINE)
    if PAPER_CAVEAT_B_CLAUSE not in line:
        bad.append("caveat (b) does not carry '%s'" % PAPER_CAVEAT_B_CLAUSE)
    if "It is uniform where nothing sources it.**" in line:
        bad.append("caveat (b) states the premise as fact (the wording as it stood)")
    return bad


#: DOCKET 65's seated row ids, built from massform.PROPOSED_ROWS (the rows,
#: not the S10 (open) item or the S5 append), for M-S1A-P1's unblocks cell.
D65_SEATED_IDS = ", ".join(r[0] for r in massform.PROPOSED_ROWS
                           if re.fullmatch(r"[DS]\d+", r[0]))

#: QUESTIONS M HAS RULED ON, same shape, kept so the ruling has its question.
#: The last two fields now read: what M ruled, and what it unblocks.
#: M-D67-1: arXiv and journal versions.  M ruled unprompted after Kuo &
#: Ford's journal version could not be retrieved here and M compared it with
#: arXiv v1.  M's words, verbatim from the session, witnessed by the lead; the
#: tree holds no copy to check them against.
M_D67_1_WORDS = ("a formal paper published to Arxiv.org carries the same weight as "
                 "the same paper published in a journal and may be used for our "
                 "purposes, as long as I have confirmed they are the same paper.")
M_D67_1_QUESTION = ("(No question was put: M ruled after the journal version of Kuo & "
                    "Ford, %s, could not be retrieved through this session's network "
                    "policy and M read it beside arXiv %s.)")
M_D67_1_RULING_T = ("RULED BY M: 'New Ruling: %s'  APPLIED where M has confirmed "
                    "the pair -- Kuo & Ford: fluctuation.py records the journal "
                    "version %s (fluctuation.JOURNAL_VERSION_COMPARED_BY_M = %s; M's "
                    "words in fluctuation.M_JOURNAL_COMPARISON), so its findings against "
                    "arXiv v1 carry the journal version's weight.  Its condition stands "
                    "for every other source: an arXiv read carries a journal version's "
                    "weight only once M has confirmed they are the same paper")


def m_d67_1_row():
    """M-D67-1's row, asked of fluctuation.py: the journal status is READ out of
    its docstring and must agree with its flags."""
    journal, jstatus = _owner_phrase(
        fluctuation.__doc__,
        r"The published version, (Phys\. Rev\. D 47, 4510 \(1993\)), is ([A-Z-]+)",
        "fluctuation.py")
    if (jstatus == "COMPARED-BY-M") != bool(fluctuation.JOURNAL_VERSION_COMPARED_BY_M):
        raise ValueError("fluctuation.py's docstring and JOURNAL_VERSION_COMPARED_BY_M disagree")
    preprint = _owner_phrase(fluctuation.SOURCE, r"(gr-qc/\d+ v\d)", "fluctuation.SOURCE")
    return ("M-D67-1",
            M_D67_1_QUESTION % (journal, preprint),
            "fluctuation.py, against arXiv %s: the journal version, %s, is %s -- "
            "M read both and reports: \"%s\" (verbatim from the session, witnessed "
            "by the lead)" % (preprint, journal, jstatus, fluctuation.M_JOURNAL_COMPARISON),
            M_D67_1_RULING_T % (M_D67_1_WORDS, jstatus,
                                fluctuation.JOURNAL_VERSION_COMPARED_BY_M),
            "DOCKET 67's audits and the per-source comments M ruled: an audit read "
            "at arXiv stands for the journal version once M confirms the pair; "
            "until then it stands for the arXiv version alone")


#: M-D67-2: which arXiv/journal pairs M confirms under M-D67-1.  The question
#: exactly as it was put to M, M's answer and the option as it was described to
#: M, verbatim from the session, witnessed by the lead.  The pairs the audits
#: read are listed for M in docket67-raw/PAIRS-FOR-M.md.
M_D67_2_QUESTION = ("Your ruling M-D67-1 needs you to confirm each arXiv/journal pair "
                    "as the same paper. 54 pairs are unconfirmed. Which should you "
                    "confirm?")
M_D67_2_ANSWER = "arXiv is the object"
M_D67_2_OPTION = ("Where the journal can't be read, every finding is stated against "
                  "the arXiv version read, by its version number, with no claim "
                  "about the journal.")
M_D67_2_RULING_T = ("RULED BY M: '%s' -- the option as described to M: \"%s\"  "
                    "APPLIED to DOCKET 67's record and its per-source comments: where M "
                    "has not confirmed a pair under M-D67-1, a finding is stated against "
                    "the arXiv version the audit read, by its version number, and claims "
                    "nothing about the journal version.  Kuo & Ford is outside it: its "
                    "journal version is %s (fluctuation.JOURNAL_VERSION_COMPARED_BY_M = %s)")


def m_d67_2_row():
    """M-D67-2's row; Kuo & Ford's journal status is READ out of fluctuation.py
    as m_d67_1_row() reads it, so the exception the ruling names cannot drift."""
    journal, jstatus = _owner_phrase(
        fluctuation.__doc__,
        r"The published version, (Phys\. Rev\. D 47, 4510 \(1993\)), is ([A-Z-]+)",
        "fluctuation.py")
    return ("M-D67-2",
            M_D67_2_QUESTION,
            "M-D67-1 lets an arXiv read carry a journal version's weight only once M "
            "confirms the pair, and the journal versions of the papers DOCKET 67's "
            "audits read are behind this session's network policy",
            M_D67_2_RULING_T % (M_D67_2_ANSWER, M_D67_2_OPTION, jstatus,
                                fluctuation.JOURNAL_VERSION_COMPARED_BY_M),
            "DOCKET 67's verified grades and the per-source comments, stated "
            "against the arXiv versions read, without waiting on pair confirmations")


#: DOCKET 67's close record (M-D68-C1: "Open after D67").
D67_CLOSE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "docket67-raw", "CLOSE.md")


def d67_close_present():
    """docket67-raw/CLOSE.md is in the tree and is DOCKET 67's close-out."""
    return os.path.exists(D67_CLOSE_FILE) and d67_close_head().startswith("DOCKET 67")


def d67_close_head():
    """CLOSE.md's first heading, READ (the '# ' stripped), or '' if absent."""
    if not os.path.exists(D67_CLOSE_FILE):
        return ""
    with open(D67_CLOSE_FILE, encoding="utf-8") as fh:
        return fh.readline().lstrip("#").strip()


#: M-D65-3's unblocks cell as first written -- kept, and followed by what ran
#: (2026-10-05: DOCKET 67 closed on 2026-10-03; the cell still said NOT YET RUN).
M_D65_3_UNBLOCKS_AS_FIRST_WRITTEN = (
    "DOCKET 67, NOT YET RUN, runs after DOCKET 65 is seated and before DOCKET 66")


def d67_close_sections():
    """CLOSE.md's numbered section headings, READ (the '## ' stripped)."""
    if not os.path.exists(D67_CLOSE_FILE):
        return []
    with open(D67_CLOSE_FILE, encoding="utf-8") as fh:
        return [ln[3:].strip() for ln in fh if ln.startswith("## ")]


def d67_ran():
    """What M-D65-3's unblocks cell says DOCKET 67 did, READ from its close
    record: nothing typed here beyond the pointer to it."""
    secs = d67_close_sections()
    return ("closed; its close record is in the tree (docket67-raw/CLOSE.md present, its "
            "head '%s': %s), and its sections, READ, are: %s.  Which values it moved is "
            "that record's, not this cell's" % (d67_close_head(), d67_close_present(),
                                                 "; ".join("'%s'" % h for h in secs)))


def m_d65_3_unblocks_faults(text=None):
    """[fault] where M-D65-3's unblocks cell is not its first wording ('NOT YET
    RUN', kept) followed by 'DOCKET 67 has run: ' and d67_ran() -- EQUALITY, so
    no verdict can be typed beside it."""
    text = ([r for r in RULED_BY_M if r[0] == "M-D65-3"][0][4]
            if text is None else text)
    want = M_D65_3_UNBLOCKS_AS_FIRST_WRITTEN + ".  DOCKET 67 has run: " + d67_ran()
    if " ".join(text.split()) != " ".join(want.split()):
        return ["not its first wording followed by 'DOCKET 67 has run: ' and d67_ran()"]
    if not d67_close_present():
        return ["docket67-raw/CLOSE.md is absent or not DOCKET 67's close-out"]
    return []


RULED_BY_M = [
    ("M-D64-1",
     "phase1.py's D4 (not this board's D4): restate '%s' for the process?"
     % phase1.D4_AS_FIRST_WRITTEN,
     "phase1.py classes any momentum flux as PROPULSION (is_transition with a "
     "momentum flux and every other condition met returns %s).  formation.py "
     "shows every U = 0 passage from flat space has T^{0r} != 0 at some "
     "instant wherever m_1 != 0 (PHASE1_D4_POINTWISE_DURING_PASSAGE = %s; "
     "THEOREM under F1's hypotheses), with zero net momentum by symmetry.  "
     "Kept pointwise for the process, D4 makes every U = 0 formation "
     "propulsion by phase1's own classifier"
     % (phase1.is_transition(True, True, True, True, True),
        formation.PHASE1_D4_POINTWISE_DURING_PASSAGE),
     "RULED BY M: RESTATE IT, as DOCKET 64 ruling D.2 proposed -- (i) T^{0i} = 0 "
     "in each configuration g_s; (ii) zero NET momentum (no thrust) across the "
     "passage between them.  APPLIED in phase1.py (D4_RESTATED_ON_M_RULING = %s); "
     "a device that thrusts still fails D4 (ii) (is_transition = %s), and a "
     "transient flux with zero net momentum does not (is_transition = %s)"
     % (phase1.D4_RESTATED_ON_M_RULING,
        phase1.is_transition(False, True, True, True, True, net_momentum=True),
        phase1.is_transition(False, True, True, True, True, passage_flux=True)),
     "step 1a, the specification theorem, may now state D4"),

    # M's five rulings on specthm.py's PENDING FOR M (step 1a review).  M's
    # words are quoted; what is applied, and what is opened instead, is said.
    ("M-S1A-P1",
     "Is the seat (specthm's object S) required to contract?",
     "a positive lens mass lengthens proper distance: contraction iff m < 0 "
     "(certify.theorem_holds() = %s), so S-1's witness does not contract"
     % certify.theorem_holds(),
     "RULED BY M: NO, S IS NOT REQUIRED TO CONTRACT -- M's words: 'I would "
     "imagine the seat is an expansion.'  APPLIED: no contraction requirement "
     "binds S.  M's mechanism -- 'As soon as the "
     "information hits the seat, it triggers the higgs field, and atomic mass "
     "forms', with 'If the elements required for seating are present, then the "
     "conditions for a higgs field or something like it are also present' -- is "
     "NOT applied: M ruled it be TESTED AS A DOCKET (DOCKET 65), against D15, "
     "D16, S9 and a full energy and conservation-law account",
     "S-1 stands NONEMPTY with no contraction requirement; DOCKET 65 opens.  "
     "DOCKET 65 has run: %s (massform.py)" % D65_SEATED_IDS),

    ("M-S1A-P2",
     "Is aimability binding (DOCKET 62's R5)?",
     "D14 proves the destination UNDEFINED on a static spherically symmetric "
     "device (ledger D14 %s); no ruling had made aimability a requirement"
     % [r[2] for r in DEMAND if r[0] == "D14"][0],
     "RULED BY M: YES, NOT SOLE -- 'aiming is definitely part of it, but it "
     "doesn't have to be the only function.'  CLARIFIED BY M: the device's "
     "geometry must single out a POINT, not a sphere, and a subsystem may supply "
     "it -- 'consider the device shape a cylinder.  The idea is the user aims "
     "the device, the corridor is like another agent that verifies it.'  "
     "APPLIED: aimability is a REQUIRED function (necessary, not sufficient) of "
     "the device's whole geometry",
     "specthm imposes aimability on C; with D14 every static spherically "
     "symmetric member fails it"),

    ("M-S1A-P3",
     "Is a closed causal curve, or a Borde pathology, disqualifying?",
     "create.py reads Geroch and Borde: causally compact topology change forces "
     "causality violation with no matter assumption "
     "(GEROCH_NEEDS_MATTER_ASSUMPTION = %s), and no escape stays in Lorentzian "
     "GR without a pathology (any_escape_stays_in_lorentzian_gr() = %s)"
     % (create.GEROCH_NEEDS_MATTER_ASSUMPTION,
        create.any_escape_stays_in_lorentzian_gr()),
     "RULED BY M: BOTH readings of 'these are defects' -- (i) a closed causal "
     "curve or a Borde pathology DISQUALIFIES, and CLARIFIED BY M it does so AT "
     "THE SEAT ONLY: 'My ruling refers to the seat/destination.  Singular occurs "
     "in the throat where the geometry is compressed to binary information, and "
     "then push to the seat'.  APPLIED at the seat; a singular throat is not "
     "disqualified.  (ii) topological defects are candidate SEATING SITES "
     "('Seating occurs in a place where matter can occur but not in its "
     "original geometric form'): NOT applied, opened as DOCKET 66, with M's "
     "throat-compression mechanism",
     M_S1A_P3_UNBLOCKS_AS_FIRST_WRITTEN + ".  DOCKET 66 has run: " + d66_p3_ran()),

    ("M-S1A-P4",
     "Is phase1's D3 read per R1 (pointwise invariant contraction)?",
     "phase1's D3 is a slice statement and a slice statement is gauge; the "
     "anchor lemma does not close it (foliation.NONSTATIC_ANCHOR_CLOSES_D3 = %s)"
     % foliation.NONSTATIC_ANCHOR_CLOSES_D3,
     "RULED BY M: RUN BOTH AND COMPARE -- 'this can go either way according to "
     "the math, so we should run both scenarios and compare. Maybe its a "
     "combination of the two.'  APPLIED: specthm runs three readings -- R1 "
     "pointwise, phase1's slice D3 literally, and net contraction along the "
     "static slice between fixed places (the combination)",
     "specthm prints what T admits under each reading, side by side"),

    ("M-S1A-P5",
     "For the reconstruction route: what is specified, at what fidelity, "
     "classical or quantum?",
     "DOCKET 62's R11 note recorded three rulings unmade; transit.py already "
     "holds that teleportation is a move, not a copy "
     "(IT_IS_A_MOVE_NOT_A_COPY = %s), consumes its channel "
     "(CHANNEL_IS_CONSUMED_BY_USE = %s), carries no substance "
     "(CARRIES_SUBSTANCE = %s) and does not beat light (BEATS_LIGHT = %s) -- "
     "each exact at fidelity F = 1, one pure ebit and an unknown state, in "
     "linear, chronology-respecting quantum mechanics, and 'consumed' is "
     "LOCC non-increase of entanglement, not a conservation law (DOCKET 67: "
     "these hypotheses were unnamed here, while O3 is open)"
     % (transit.IT_IS_A_MOVE_NOT_A_COPY, transit.CHANNEL_IS_CONSUMED_BY_USE,
        transit.CARRIES_SUBSTANCE, transit.BEATS_LIGHT),
     "RULED BY M: BOTH, QUANTUM FIRST -- 'both. Quantum first, which should "
     "derive the classical.'  APPLIED: the specification is a quantum state; "
     "the classical specification is to be derived from it, and no derivation "
     "exists yet",
     "R11 is stated on a quantum specification; transit.py's four results bind "
     "it IF it is carried by teleportation as an unknown quantum state, at "
     "F = 1, in linear, chronology-respecting quantum mechanics"),

    # M's ruling at DOCKET 65's seating.  M's words are quoted verbatim; the
    # literature is CITED as the question was put, and nothing here has READ it.
    # PROVENANCE: the question's parenthetical is exactly the question as the
    # lead put it to M -- verbatim from the session, witnessed by the lead
    # against the transcript; the tree holds no copy and cannot verify it.
    ("M-D65-1",
     "Should Quantum Energy Teleportation (information arriving at the "
     "destination creates a local negative-energy region there) be tested as "
     "its own docket?",
     "M's words, verbatim: '" + M_D65_1_WORDS + "'.  The question's "
     "parenthetical is the question's description as put to M, not READ.  The "
     "literature anchor, CITED, not READ: " + M_D65_1_LITERATURE + "  (As the "
     "question stood when M ruled; DOCKET 66 has since READ the literature -- "
     "the ruling cell.)",
     # The ruling cell is the one LEDGER.md and the report print, so M's words
     # and the literature's status are carried here too, not only in `why` --
     # from the SAME constants, so the two copies cannot differ.  DOCKET 66's
     # seating: the cell is M_D65_1_RULING_T filled from the constants and
     # what DOCKET 66 ran (asked); its first wording is kept inside it.
     M_D65_1_RULING_T % (M_D65_1_ANSWER, M_D65_1_WORDS, M_D65_1_LITERATURE,
                         d66_m_d65_1_ran()),
     "DOCKET 66 has tested QET beside seating at a topological defect (wave 1, "
     "seated: O9's DOCKET 66 part and S5's note).  FIRST SAID (kept): "
     + M_D65_1_UNBLOCKS_AS_FIRST_WRITTEN),

    # M's second ruling at DOCKET 65's seating.  The seating had opened the
    # finite share as its own row, O8; the question was put to M as below.
    ("M-D65-2",
     M_D65_2_QUESTION,
     "Section 4's principle gives no row to an unsettled question internal to "
     "an already-REFUSED row that gates nothing.  The finite share is internal "
     "to S10 (S10 is %s), it gates nothing (its own answer: '%s'), and nothing "
     "computes it (massform.FINITE_HIGGS_SHARE_STATUS = %s).  The option M "
     "chose was described to M as '%s'; '%s'"
     % ((massform.MECHANISM_VERDICT[0], PROPOSED["S10 (open)"][5].split("; ")[-1],
         massform.FINITE_HIGGS_SHARE_STATUS) + M_D65_2_OPTION),
     "RULED BY M: FOLD INTO S10's NOTE -- M's answer: '" + M_D65_2_ANSWER + "'.  "
     "APPLIED: no row; the finite share stays an OPEN item inside S10's note "
     "(massform's item 'S10 (open)', its status massform.FINITE_HIGGS_SHARE_"
     "STATUS, asked), a candidate question for a future docket.  O8 is not "
     "seated, and the OPEN census is statuses()'s without it",
     "S10's note carries the finite share as an OPEN item; massform.NOT_OPENED "
     "lists it again; specthm's SR5 places no O8"),

    # M's third ruling at DOCKET 65's seating: DOCKET 67, the audit of the
    # external results the board's refusals rest on.  M's words are quoted
    # verbatim; `why` is m_d65_3_why(), built from what fluctuation.py and
    # massform.py themselves record -- the discrepancies fluctuation.py
    # records against a preprint version, COUNTED from its KF flags, and the
    # divergences massform.py records under its own heading, COUNTED from its
    # sentences; the cell details the items M_D65_3_WHY_ITEMS_FLUCT / _MASS
    # name, each guarded present in the cell -- every figure and count ASKED,
    # never retyped, and fluctuation's verdict on Kuo & Ford's conclusion
    # and on the ledger (no row moves) asked beside them; the ruling cell is
    # M_D65_3_RULING_T filled from the constants.
    ("M-D65-3",
     M_D65_3_QUESTION,
     m_d65_3_why(),
     M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS),
     M_D65_3_UNBLOCKS_AS_FIRST_WRITTEN + ".  DOCKET 67 has run: " + d67_ran()),

    # M's fourth ruling at DOCKET 65's seating: the paper.  The completeness
    # lens found paper/CLAIMS.md's caveat (b) stating the Higgs vacuum's
    # uniformity as fact while massform seats it as the premise P-UNIFORM; the
    # question was put to M as M_D65_4_QUESTION and M answered M_D65_4_ANSWER.
    # The paper carries the clause (paper_caveat_b_faults() READS it back);
    # `why` is M_D65_4_WHY_T filled from the caveat line and massform's asked
    # status; the ruling cell is m_d65_4_ruling() -- M_D65_4_RULING_T filled
    # from the constants, M's rule for the paper (M_PAPER_RULE_WORDS) and the
    # DOCKET 63 marker READ back from the paper (paper_d63_marker()), so the
    # marked edits this file names are named and none is counted;
    # unblocks is M_D65_4_UNBLOCKS_T filled from M's rule for the paper.
    ("M-D65-4",
     M_D65_4_QUESTION,
     m_d65_4_why(),
     m_d65_4_ruling(),
     M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS),

    # M's fifth ruling at DOCKET 65's seating: the ruling id in the paper's
    # clause.  The lead put M_D65_5_QUESTION to M and M answered
    # M_D65_5_ANSWER (both verbatim from the session, witnessed by the lead);
    # the paper's clause now carries the id (PAPER_CAVEAT_B_CLAUSE, READ back
    # by paper_caveat_b_faults()); `why` is M_D65_5_WHY, the lenses' finding;
    # the ruling cell is m_d65_5_ruling() -- M_D65_5_RULING_T filled from the
    # constants, the DOCKET 63 marker's lines READ back and the paper's DOCKET
    # markers READ (paper_docket_markers(), a census the reader counts);
    # unblocks is
    # M_D65_4_UNBLOCKS_T filled from M's rule for the paper, which stands.
    ("M-D65-5",
     M_D65_5_QUESTION,
     M_D65_5_WHY,
     m_d65_5_ruling(),
     M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS),

    # M's ruling on arXiv and journal versions (DOCKET 67), asked of
    # fluctuation.py's journal status by m_d67_1_row().
    m_d67_1_row(),

    # M's ruling on which pairs M confirms (DOCKET 67): none -- the arXiv
    # version read is the object of every finding M has not confirmed.
    m_d67_2_row(),
]

# ----- DOCKET 68's rulings (docstring section 7) ----------------------------
# Kept OUTSIDE the list above on purpose: the selftest reads the source region
# from the M-D65-4 constants to that list's end for counts of the paper's
# edits, and nothing here belongs to it.

#: The tree's own copies of M's words for DOCKET 68: the selftest checks every
#: constant in D68_M_WORDS against the file it names, whitespace and the
#: Markdown quote marks normalised -- not against memory.
D68_RULINGS_FILE = os.path.join(D68_DIR, "M-RULINGS-2026-10-03.md")
D68_CHARTER_FILE = os.path.join(D68_DIR, "CHARTER.md")
D68_PAPER_BRIEF = os.path.join(D68_DIR, "PAPER-BRIEF-Q1s.md")

#: M'S OWN WORDS FOR DOCKET 68's RULINGS, each held ONCE: id -> (words, file).
#: Every ruling cell interpolates them, quoted in double quotes (some hold
#: apostrophes).  Where the tree holds M's answer only as the charter's
#: carrying of it, the words held are M's words the carrying answers, and the
#: cell names the carrying as the charter's (M-D68-C2, M-D68-C3).
D68_M_WORDS = {
    "M-D68-1": ("Teleportation carries no physical substance, but does carry information "
                "(non physical properties/bounds that give shape to the geometry at the seat)",
                D68_RULINGS_FILE),
    "M-D68-2": ("Carry both (Recommended)", D68_RULINGS_FILE),
    "M-D68-3": ("All of the above. Remember that the center begins at the ground state values "
                "given in real numbers from the periodic table. That is the calibration",
                D68_RULINGS_FILE),
    "M-D68-4": ("Keep held, noted (Recommended)", D68_RULINGS_FILE),
    "M-D68-5": ("Yes, from the seat", D68_RULINGS_FILE),
    "M-D68-6": ("Mass/ binding. But could work for any of the other options depending on the "
                "question being asks or the object of study", D68_RULINGS_FILE),
    "M-D68-7": ("S5 counts (Recommended)", D68_RULINGS_FILE),
    "M-D68-8": ("Keep both (Recommended)", D68_RULINGS_FILE),
    "M-D68-9": ("Wait", D68_RULINGS_FILE),
    "M-D68-10": ("1 then 2 then 3 then 4", D68_RULINGS_FILE),
    # ADDED (DOCKET 68 residuals): item 11, recorded 2026-10-04 (77a16a1)
    # after the seating's baseline was taken; first left unseated.
    "M-D68-11": ("The paper is not a priority, just an additional if the math concept is novel "
                 "or introduces new theorems/proofs not otherwise previously published art",
                 D68_RULINGS_FILE),
    # ADDED: items 12 and 13 (2026-10-04), M's rulings on the paper; applied
    # by the lead in paper/CLAIMS.md under DOCKET 68 marker heads, which
    # paper_d68_marker() READs back.
    "M-D68-12": ("Correct it (Recommended)", D68_RULINGS_FILE),
    "M-D68-13": ("Scope it (Recommended)", D68_RULINGS_FILE),
    # ADDED (DOCKET 68 wave 2): items 15 and 16, M's words on the retrieval
    # route; item 15 superseded by item 16, both held (history kept).
    "M-D68-15": ("The methods own navigation and retrieval instruments are available for "
                 "obtaining outside art in non-conventional ways", D68_RULINGS_FILE),
    "M-D68-16": ("No. I mean their are instruments to assist navigating and retrieval of "
                 "papers from the web", D68_RULINGS_FILE),
    "M-D68-C1": ("Open after D67", D68_CHARTER_FILE),
    "M-D68-C2": ("test the 12 fields in the 12 vertex trajectory model of the warp device idea",
                 D68_CHARTER_FILE),
    # CORRECTED (DOCKET 68 residuals): first held as "Quantum mechanics is
    # slightly non-linear. - quantum easing/quantum settling", which put the
    # route put to M (D68_ROUTES) inside M's words; M's reply follows the ' - '.
    "M-D68-C3": ("quantum easing/quantum settling", D68_CHARTER_FILE),
    "M-D68-C5": ("Consider both 1 and 2", D68_CHARTER_FILE),
    "M-D68-C8": ("we can define this. We plot it. With all its inverses, and reflections on the "
                 "same multi-axis graph and the positive values will triangulate the negative "
                 "values", D68_CHARTER_FILE),
    "M-D68-C8b": ("Yes. When docket 68 workflow is finished. Let's create the instrument and "
                  "implement its use. Incidently, if this does prove useful, we should set up "
                  "instructions for a new separate session to write a professional paper about "
                  "the complex and negative entropy findings", D68_CHARTER_FILE),
    # ADDED (M-D68-P1 converted): M answered the ER = EPR citation question on
    # 2026-10-02, before DOCKET 68 opened, and it was applied the same day
    # (emtension.py's ER_EPR_*).  The charter, written before the answer,
    # still reads 'asked of M and unanswered', so the ledger first carried it
    # as pending (M-D68-P1).  The words are held from M-RULINGS-2026-10-03.md
    # item 14, which records the question and answer verbatim.  C12, not C9:
    # M-D68-C9 is the charter's carried H-IT instruction (D68_CARRIED_WORDS).
    "M-D68-C12": ("Record it (Recommended)", D68_RULINGS_FILE),
    # ADDED (D66-seat of M's DOCKET 66 rulings, R-seat): items 26-28 of the
    # same rulings file, under its heading 'DOCKET 66 rulings (2026-10-04)'.
    # The ids follow the item number, as M-D68-12..16 do: the file is
    # DOCKET 68's rulings file and items 26-28 are held there.  Item 26's words
    # are the same as item 12's ("Correct it (Recommended)"); each is held
    # under its own id and each paper marker is READ by its own docket head.
    "M-D68-26": ("Correct it (Recommended)", D68_RULINGS_FILE),
    "M-D68-27": ("Any crossing", D68_RULINGS_FILE),
    "M-D68-28": ("Re-grade D68 (Recommended)", D68_RULINGS_FILE),
    # ADDED (W3S1B-seat, docstring section 8c): M's answers to questions put,
    # items 22 and 24 (the corridor, 2026-10-04, held since then in the
    # rulings file and first seated here, when wave 3 did their work) and
    # items 29, 30, 33 and 34 (Step 1b, 2026-10-05).  Items 21, 23, 25, 31, 32
    # and 35 are M's statements, hypothesis and question, carried by the
    # rulings file and not rulings: D68_CARRIED_WORDS, D68_FILE_CARRIED.
    "M-D68-22": ("Yes. Exactly.", D68_RULINGS_FILE),
    "M-D68-24": ("Or you may mean the twelve conditions are literally quantum-correlated between "
                 "the positions. - this.", D68_RULINGS_FILE),
    "M-D68-29": ("Balanced means that the value of the object at first position must equal the "
                 "value of the object at the second position. And any variable input must be "
                 "accounted for in output", D68_RULINGS_FILE),
    "M-D68-30": ("Information only", D68_RULINGS_FILE),
    "M-D68-33": ("Keep all four", D68_RULINGS_FILE),
    "M-D68-34": ("Corridor (D68 wave 3)", D68_RULINGS_FILE),
    # ADDED (W3S1B-seat): item 36, M's ruling to seat wave 3 and Step 1b.
    "M-D68-36": ("Seat both (Recommended)", D68_RULINGS_FILE),
    # ADDED (S1C-seat, docstring section 8d): items 37-39, M's answers on
    # Step 1c.
    "M-D68-37": ("All three (Recommended)", D68_RULINGS_FILE),
    "M-D68-38": ("Take the coupling route", D68_RULINGS_FILE),
    "M-D68-39": ("3, then 2. Then 1 last please", D68_RULINGS_FILE),
    # ADDED (D68-close, docstring section 8e): item 40.
    "M-D68-40": ("2 then 1 please", D68_RULINGS_FILE),
    # ADDED (CMB-seat, docstring section 8f): items 42, 43 and 45.
    "M-D68-42": ("3, then 1", D68_RULINGS_FILE),
    "M-D68-43": ("No paper", D68_RULINGS_FILE),
    "M-D68-45": ("Seat it, then medium", D68_RULINGS_FILE),
    # ADDED (CMB2-seat, docstring section 8g): items 47, 49, 51, 53 and 54.
    "M-D68-47": ("2, then 1", D68_RULINGS_FILE),
    "M-D68-49": ("1. Also, yes, matter itself is capable of observation, however, it is not conscious "
                 "conversation, which requires sentience . A different type of observation...", D68_RULINGS_FILE),
    "M-D68-51": ("3. But I also want you to consider multiple sentient/conscious observers. Each observation "
                 "is a different and relative perspective of the same object, thus each observation is "
                 "inhomogeneous when compared to the others", D68_RULINGS_FILE),
    "M-D68-53": ("READ, then model", D68_RULINGS_FILE),
    "M-D68-54": ("3, then 2, then 1 please", D68_RULINGS_FILE),
    # ADDED (CMB3-seat, docstring section 8h): item 55.
    "M-D68-55": ("Seat both", D68_RULINGS_FILE),
}

#: THE QUESTIONS PUT TO M FOR M'S DOCKET 66 RULINGS (items 26-28), as the
#: rulings file records them (the file's words, held once, checked against it
#: through D68_INLINE_QUOTES), and what the file records as applied for each --
#: the file's words, NOT M's (M's are D68_M_WORDS only).
D66_RULING_QUESTIONS = {
    "M-D68-26": ("Asked whether to replace 'gamma > 1.33e5 at the bound G mu <~ 6e-7' with the "
                 "Planck 2013 bound READ at source (G mu/c^2 < 1.5e-7, giving gamma > 5.3e5)"),
    "M-D68-27": "Asked whether TURN means a genuine conjugate point or any crossing of light paths",
    "M-D68-28": ("Asked whether to apply M-S1A-P3 ('a singular throat is not disqualified'; throat "
                 "creation stays OPEN) in D68's combine.py too"),
}
D66_RULING_CARRIED = {
    "M-D68-26": "Applied under a marked note.",
    "M-D68-27": ("H-TURN-CROSSING is adopted; the straight cosmic string TURNs (rays cross "
                 "without focusing)."),
    "M-D68-28": ("O-MAKE-TOPO reads OPEN via N_WNCC in D68's board-context variants as in D66's; "
                 "history kept."),
}
#: The paper's first wording as item 26 quotes it (ASCII); the paper's own
#: marker quotes the same first wording in its own typography, READ back by
#: paper_d66_first_wording() and compared number by number in the selftest.
D66_PAPER_FIRST_WORDING = "gamma > 1.33e5 at the bound G mu <~ 6e-7"
#: The same first wording as the paper's DOCKET 66 marker prints it, held and
#: checked against paper/CLAIMS.md (D68_INLINE_QUOTES): the paper's words, not
#: M's and not the rulings file's, so it is declared in D68_NOT_QUOTES too.
D66_PAPER_FIRST_WORDING_AS_PRINTED = "`γ > 1.33e5` at the bound `Gμ ≲ 6e−7`"
PAPER_FILE = os.path.join(HERE, "paper", "CLAIMS.md")

#: THE QUESTION PUT TO M FOR M-D68-C12, verbatim, as M-RULINGS-2026-10-03.md
#: item 14 records it -- held once, checked against that file like M's words
#: (D68_INLINE_QUOTES), and quoted in the ruling's question cell.
D68_C12_QUESTION = ("emtension.py states that the ER = EPR bridge cannot be crossed, but cites "
                    "no source. Should I record today's reading of Maldacena & Susskind (arXiv "
                    "1306.0533 v2, read at source) there?")

#: THE QUESTIONS PUT TO M FOR M-D68-12 AND M-D68-13, as items 12 and 13 of
#: M-RULINGS-2026-10-03.md record them (the file's words, held once, checked
#: against it through D68_INLINE_QUOTES), and the paper's first wording as
#: item 12 quotes it -- which the paper's own marker also quotes.
D68_PAPER_QUESTIONS = {
    "M-D68-12": ("Asked whether to correct 'For an object to arrive, an identical stock of "
                 "matter must already be there — and that had to travel', which says more than "
                 "the board holds under 'S5 counts'."),
    "M-D68-13": ("Asked whether to scope the no-communication statements to linear quantum "
                 "mechanics."),
}
D68_PAPER_FIRST_WORDING = ("an identical stock of matter must already be there — and that had "
                           "to travel")

#: M'S OWN WORDS FOR WHAT THE CHARTER CARRIES WITHOUT A RULING: id -> (words,
#: file), checked exactly as D68_M_WORDS is.  M's proposals, statements and
#: instructions, each carried by CHARTER.md as a hypothesis or a standing
#: instruction.  NOT RULINGS and NOT COUNTED AS RULINGS: they sit in
#: D68_CARRIED, not RULED_BY_M.  MOVED (DOCKET 68 residuals): C4, C6 and C7
#: were first seated on RULED_BY_M under 'RULED BY M: M'S PROPOSAL ... M
#: worded no ruling', a prefix their own text contradicted.  C9-C11 ADDED:
#: H-IT, H-FRAME and H-INFO/Q-1 had no row while H-ZERO and H-NULL had one.
#: Where M replied to a route put to M, only the reply is held (D68_ROUTES
#: holds the route), as for M-D68-C2 and M-D68-C3.
D68_CARRIED_WORDS = {
    "M-D68-C4": ("Remember that some of the hypothesies lined up for docket 68 may turn out, "
                 "after initial testing, to work better in combination.", D68_CHARTER_FILE),
    "M-D68-C6": ("What if we redefine 0. Consider 0 to me a point of ground state, and anything "
                 "less that 0 is not negative, just less than the ground state", D68_CHARTER_FILE),
    "M-D68-C7": ("Null (NEC) is a containment. This is where information lives, and is "
                 "quantifiable", D68_CHARTER_FILE),
    "M-D68-C9": ("let's assume this is correct", D68_CHARTER_FILE),
    "M-D68-C10": ("maybe messages can travel into the past, it seems impossible because our "
                  "lack of understanding about cosmic information", D68_CHARTER_FILE),
    "M-D68-C10b": ("what if our error is accepting that spacetime is flat?", D68_CHARTER_FILE),
    "M-D68-C11": ("Cosmic/quantum information is all that matters. It is the only "
                  "multi-universal currency. Without it, matter cannot exist, let alone form "
                  "structural mass. We need to quantify information, unambiguously and "
                  "independently of all cosmic/quantum physicalities", D68_CHARTER_FILE),
    # ADDED (W3S1B-seat, docstring section 8c): M's words the RULINGS FILE
    # carries without a ruling -- statements (21, 23, 25), an instruction (31),
    # a hypothesis given in answer to a question (32: "I suspect") and a
    # question (35).  Each is checked against M-RULINGS-2026-10-03.md, not the
    # charter.  M-D68-24b is the sentence M added to item 24's answer, held
    # beside the answer as M-D68-C10b is beside C10.
    "M-D68-21": ("speed is not a question in my work. The two positions technically exist as one. "
                 "So the corridor allows for the the entanglement of two positions at once. The "
                 "object in transit requires no speed. It is either at the beginning or end "
                 "position, never in between them", D68_RULINGS_FILE),
    "M-D68-23": ("the math for the corridor is formed by the 12 trajectories of navigation. Each "
                 "one is a physics condition that governs an aspect of the reconstruction at "
                 "seating. These 12 allow for the predetermination of seat compatibility based on "
                 "the starting state - entanglement at 12 criteria.", D68_RULINGS_FILE),
    "M-D68-24b": ("The 12 conditions only need to supply enough for the object to reconstruct in "
                  "the new environment, based on the stock of available matter, whether or not "
                  "the environment is habitable/hospitable by the object, is not a factor.",
                  D68_RULINGS_FILE),
    "M-D68-25": ("this is where the magnitude of probabilities (negative and positive), and "
                 "complex binary come into play. The stronger negative magnitudes will "
                 "automatically triangulate the stronger positive magnitudes which rank the "
                 "probability of seating", D68_RULINGS_FILE),
    "M-D68-31": ("Be sure to account for compensation in the physics.... Let's say mass energy "
                 "density is different at the seat, but some other discrepancy makes up of that "
                 "and dissolves the defect...", D68_RULINGS_FILE),
    "M-D68-32": ("I suspect so, to satisfy the no-cloning clause.", D68_RULINGS_FILE),
    "M-D68-35": ("Question... If information is what is being sent, how big does the corridor "
                 "actually have to be? We assumed 1 meter, but that was for moving matter instead "
                 "of information", D68_RULINGS_FILE),
    # ADDED (CMB-seat, docstring section 8f): M's question after DOCKET 68's
    # close (41, carrying two hypotheses) and M's instruction (44).
    "M-D68-41": ("Have we considered the universe's own background radiation as the means by which "
                 "the corridor is constructed? As it is likely that background only "
                 "multi-spacetime/multiversal constant?", D68_RULINGS_FILE),
    "M-D68-44": ("No. The physics as it applies to the frame is what matters", D68_RULINGS_FILE),
    # ADDED (CMB2-seat, docstring section 8g): M's question (46) and statements (48, 50, 52).
    "M-D68-46": ("Now what happens if we consider that the universe not only expands, but it contracts as "
                 "well?", D68_RULINGS_FILE),
    "M-D68-48": ("what if this is the ground state without first principles/without observation? The "
                 "decoupling only exists upon observation of a universe? And this would be why it is a "
                 "constant", D68_RULINGS_FILE),
    "M-D68-50": ("I just had a thought.... Matter based observation is natural and always occurring, with all "
                 "probabilities available, until conscious observation occurs. Consciousness observation "
                 "forces a specific and measurable behavior from the object being observed", D68_RULINGS_FILE),
    "M-D68-52": ("time is always relative, so the clock of the observer doesn't matter in the second position, "
                 "as time may move differently in the second position compared to the first. The clock is "
                 "always present relative to the position of measurement within its plane/dimension The "
                 "clock is relative to the matter-based observation. Consciousness observation is a "
                 "perception of matter-observed time.", D68_RULINGS_FILE),
}

#: THE ROUTES PUT TO M, as CHARTER.md records them -- the charter's words, not
#: M's -- each the question an M reply above answers.  Checked against
#: CHARTER.md like M's words, so a route is never retyped.
D68_ROUTES = {
    "M-D68-C2": "I varied Alice's measurement angle across seven settings:",
    "M-D68-C3": "Quantum mechanics is slightly non-linear.",
    "M-D68-C9": "Spacetime comes from information.",
    "M-D68-C10": "A preferred frame",
    "M-D68-C10b": "Which moment the two ends share.",
}


def d68_paper_brief_present():
    """PAPER-BRIEF-Q1s.md is in the tree (M-D68-9: 'Wait')."""
    return os.path.exists(D68_PAPER_BRIEF)


def d68_brief_has_gate(path=None):
    """PAPER-BRIEF-Q1s.md carries M's condition (M-D68-11's words, verbatim)
    and names the prior-art search as the gate -- READ, not assumed."""
    path = D68_PAPER_BRIEF if path is None else path
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8") as fh:
        text = _d68_norm(fh.read())
    return (" ".join(D68_M_WORDS["M-D68-11"][0].split()) in text
            and "prior-art search" in text and "is also the gate" in text)


def _d68_held(rid):
    """(words, file) for an id in D68_M_WORDS or D68_CARRIED_WORDS."""
    return D68_M_WORDS[rid] if rid in D68_M_WORDS else D68_CARRIED_WORDS[rid]


def d68_words(rid):
    """M's words for a DOCKET 68 ruling (or a carried item), quoted as every
    cell prints them."""
    w, path = _d68_held(rid)
    return 'M\'s words, verbatim: "%s" (%s)' % (w, os.path.basename(path))


def d68_route(rid):
    """The route put to M that M's reply `rid` answers, as CHARTER.md records
    it (the charter's words, not M's)."""
    return 'the route put to M, as CHARTER.md records it: "%s"' % D68_ROUTES[rid]


def _d68_norm(text):
    """A Markdown source as prose: quote marks ('> ') and line breaks gone."""
    return " ".join(re.sub(r"(?m)^\s*>\s?", "", text).split())


def _d68_held_texts():
    """Every text this file holds as the tree's words for DOCKET 68, with the
    file it must occur in: M's words (rulings and carried items), the routes
    put to M, M's thesis and the docket's question, and the inline quotations
    D68_INLINE_QUOTES names.  {key: (text, file)}."""
    out = {}
    out.update(D68_M_WORDS)
    out.update(D68_CARRIED_WORDS)
    out.update(("route " + k, (v, D68_CHARTER_FILE)) for k, v in D68_ROUTES.items())
    out["D68_THESIS"] = (D68_THESIS, D68_CHARTER_FILE)
    out["D68_QUESTION"] = (D68_QUESTION, D68_CHARTER_FILE)
    out.update(D68_INLINE_QUOTES)
    return out


def d68_words_faults(held=None):
    """[key] whose held text does not occur verbatim in the tree's copy --
    M's words for every DOCKET 68 ruling and carried item, the routes, the
    thesis and question, and every inline quotation (_d68_held_texts())."""
    bad = []
    cache = {}
    for rid, (w, path) in (_d68_held_texts() if held is None else held).items():
        if path not in cache:
            with open(path, encoding="utf-8") as fh:
                cache[path] = _d68_norm(fh.read())
        if " ".join(w.split()) not in cache[path]:
            bad.append(rid)
    return bad


def d67_comments_present():
    """Whether docket67-raw/COMMENTS-INDEX.md, the D67 per-source comments'
    index, is in the tree (asked of the file system, M-D68-10 step 3)."""
    return os.path.exists(os.path.join(HERE, "docket67-raw", "COMMENTS-INDEX.md"))


def _d68_rule(option, rid, applied):
    """A DOCKET 68 ruling cell: the option taken, M's words, what was applied."""
    return "RULED BY M: %s -- %s.  APPLIED: %s" % (option, d68_words(rid), applied)


def _d68_index3_held():
    """index3.py's OPEN-AT-NULL-HELD rows (asked: index3 is stdlib-only)."""
    import index3
    return sorted(k[0] for k in index3.OPEN_AT_NULL_HELD)


def _emtension_flag():
    """emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE, asked (combine.board_flags
    reads the same module)."""
    with contextlib.redirect_stdout(io.StringIO()):
        import emtension
    return emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE


def _emtension_record():
    """What M-D68-C12 applied, ASKED of emtension.py (never typed here): the
    ER = EPR source, its status, the assumption flag, whether footnote 1 is
    held whole (its first and last sentences READ), the speculation flag, and
    the bridge flag the citation concerns."""
    with contextlib.redirect_stdout(io.StringIO()):
        import emtension
    fn = getattr(emtension, "ER_EPR_FOOTNOTE_1", "")
    return {
        "ER_EPR_SOURCE": getattr(emtension, "ER_EPR_SOURCE", None),
        "ER_EPR_SOURCE_STATUS": getattr(emtension, "ER_EPR_SOURCE_STATUS", None),
        "ER_EPR_NONTRAVERSABLE_IS_ASSUMED": getattr(emtension,
                                                    "ER_EPR_NONTRAVERSABLE_IS_ASSUMED", None),
        "ER_EPR_FOOTNOTE_1 whole": (fn.startswith("This can be shown using the integrated null")
                                    and fn.endswith("the ER=EPR connection would be wrong.")),
        "ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION": getattr(
            emtension, "ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION", None),
        "ENTANGLED_BRIDGE_IS_TRAVERSABLE": emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE,
    }


#: M-D68-P1 AS FIRST RECORDED -- the pending question M-D68-C12 replaced, kept
#: as history and printed in M-D68-C12's ruling cell: (question, why it was
#: asked, proposed, waiting on it), as the PENDING_RULINGS row stood.  STALE
#: WHEN WRITTEN: M had answered before DOCKET 68 opened; the charter's
#: 'asked of M and unanswered' predates the answer, and the row read the
#: charter.
D68_P1_AS_FIRST_RECORDED = (
    "Whether to record emtension.py's ENTANGLED_BRIDGE_IS_TRAVERSABLE = False, which cites "
    "no source, against Maldacena & Susskind arXiv:1306.0533v2 (CHARTER.md records the "
    "question as asked of M and unanswered)",
    "emtension.ENTANGLED_BRIDGE_IS_TRAVERSABLE = %s (asked) cites no source; combine.py "
    "reads it as a board flag; DOCKET 68 READ 1306.0533v2 at source, whose footnote 1 makes "
    "non-traversability an assumption of the conjecture" % _emtension_flag(),
    "none: the record is M's to rule.  Either way the flag's value stands and no grade "
    "moves; only its citation would change",
    "emtension.py's citation; nothing on this board",
)


def d68_w2_routes():
    """Wave 2's recorded retrieval routes, ASKED of the owners: settle's four
    Weinberg-family statuses (settle.window_read), vacuum.py's R-sources (its
    docstring's 'R<n> ... -- READ ... via <route>' lines) and seat.py's source
    records (its module dicts carrying a 'route'); and W2-fix's own reads,
    added after the W2 reproduction found them uncounted: the wave-2 row of
    settle.PROXIMA_DISTANCES_READ (its status names W2-fix; the board's
    DOCKET 67 row is not a wave-2 read) and vacuum.BDSW_TABLE1_ROUTE.  Counted
    by route; a source whose route names neither instrument is listed, never
    dropped."""
    st = list(D68_WINDOW_READ["statuses"].values())
    vac = re.findall(r"^\s+R(\d+) .*? -- (READ[^\n]*)", vacuum.__doc__, re.M)
    sea = [v["route"] for k, v in sorted(vars(seat).items())
           if isinstance(v, dict) and isinstance(v.get("route"), str)]
    pdr = [v["status"] for v in settle.PROXIMA_DISTANCES_READ.values() if "W2-fix" in v["status"]]
    bdt = [vacuum.BDSW_TABLE1_ROUTE]
    via = lambda t, w: sum(1 for x in t if ("via " + w) in x)
    other = ([x for x in st + [r for _n, r in vac] + sea + pdr + bdt
              if "via alphaXiv" not in x and "via Firecrawl" not in x])
    return ("settle's four Weinberg-family limits, %d of %d via Firecrawl (scrape of the "
            "publisher's public abstract page); vacuum.py's R1-R%s, %d via alphaXiv and %d via "
            "Firecrawl; seat.py's %d recorded sources, %d via alphaXiv and %d via Firecrawl; "
            "W2-fix's own reads: settle.PROXIMA_DISTANCES_READ's wave-2 row%s (Faria 2022 "
            "Table 1 p.2, the paper seat.py also records), %d via alphaXiv, and "
            "vacuum.BDSW_TABLE1_ROUTE (R6 Table 1 p.24 and p.29, inside R6's recorded pages), "
            "%d via alphaXiv; routes naming neither instrument: %s"
            % (via(st, "Firecrawl"), len(st), vac[-1][0] if vac else "?",
               via([r for _n, r in vac], "alphaXiv"), via([r for _n, r in vac], "Firecrawl"),
               len(sea), via(sea, "alphaXiv"), via(sea, "Firecrawl"),
               "" if len(pdr) == 1 else "s (%d)" % len(pdr), via(pdr, "alphaXiv"),
               via(bdt, "alphaXiv"), other or "none"))


_SEAT = d68_uniform("O-SEAT")


# ----- M's DOCKET 66 rulings (M-RULINGS-2026-10-03.md items 26-28) ----------
# Seated as rows of D68_RULED (the rulings file is DOCKET 68's, and specthm
# places D68_RULED's rows), every value ASKED of its owner: the paper's marked
# line READ back (item 26), defects.py and spec.py (item 27), combine.py and
# its history mutation 'd68w2-topo' (item 28).  Docstring section 8b.

#: D68 wave 2's O-MAKE-TOPO encoding, kept by combine.py as the history
#: mutation 'd68w2-topo' (M-RULINGS item 28: 'history kept'), asked on the
#: variants M-D68-28's cell prints beside the adopted screen's.
D68_SCREEN_TOPO_W2 = combine.Screen(mutate=("d68w2-topo",))
D68_TOPO_W2_ASKED = dict((k, D68_SCREEN_TOPO_W2.variant(set(p))) for k, p in D68_VARIANTS
                         if k in ("the board alone", "R-QUANTUM alone (RQ)",
                                  "H-IT as Jacobson emergent gravity (ITJ)",
                                  "ITB with R-QUANTUM (ITB+RQ)",
                                  "H-IT as an information layer (ITB)"))
#: docket68/B-combine.md, combine.py's own report of its full screen, READ for
#: the census of M-D68-28's re-grade (never retyped): its section 0
#: (D66-RULINGS) table.
D68_B_FILE = os.path.join(D68_DIR, "B-combine.md")
D68_TOPO_CENSUS_PATTERNS = (
    ("moved", r"LEFT in ([\d,]+) of ([\d,]+) at 1 ly \(board alone included\) and ([\d,]+) of "
              r"([\d,]+) at 1 AU; NOT-BOUND-IF with removal OPEN via N_ILFREE in ([\d,]+) / ([\d,]+)"),
    ("contexts", r"\*\*the same (\d+)\*\* of its (\d+) contexts move LEFT -> OPEN via N_WNCC here: "
                 r"([^|;]+?)(?:;| \|)"),
    ("drift", r"Drift: \*\*(\d+) of (\d+) agree\*\*"),
)


def d68_topo_census_read(path=None):
    """{key: groups} READ from docket68/B-combine.md's section 0 (D66-RULINGS);
    raises if the owner's report no longer states a figure M-D68-28's cell
    cites (a stale seat is a failure)."""
    with open(D68_B_FILE if path is None else path, encoding="utf-8") as fh:
        t = " ".join(fh.read().split())
    out = {}
    for key, pat in D68_TOPO_CENSUS_PATTERNS:
        m = re.search(pat, t)
        if not m:
            raise ValueError("B-combine.md no longer states %r -- the M-D68-28 seat is stale" % key)
        out[key] = m.groups()
    return out


D68_TOPO_CENSUS = d68_topo_census_read()

#: docket66/B-combine66.md READ for the same re-grade from combine66's side:
#: how many rows combine's history encoding d68w2-topo moves back (and how many
#: of them context-only), and how many singok-board now moves.
D66_TOPO_PATTERNS = (
    ("d68w2-topo", r"\| \*\*d68w2-topo\*\* \(R-apply: D68 wave 2's O-MAKE-TOPO encoding, "
                   r"combine's history mutation\) \| (\d+), of which (\d+) context-only \|"),
    ("singok-board", r"\| \*\*singok-board\*\* \(M's ruling reaching every geometric throat, "
                     r"D68's included\) \| \*\*(\d+)\*\*"),
)


def d66_topo_read(path=None):
    """{key: groups} READ from B-combine66.md's readings table; raises if the
    owner's report no longer states them."""
    with open(D66_B_FILE if path is None else path, encoding="utf-8") as fh:
        t = " ".join(fh.read().split())
    out = {}
    for key, pat in D66_TOPO_PATTERNS:
        m = re.search(pat, t)
        if not m:
            raise ValueError("B-combine66.md no longer states %r -- the M-D68-28 seat is stale" % key)
        out[key] = m.groups()
    return out


D66_TOPO_READ = d66_topo_read()


def specthm_seat_class_literals(path=None):
    """{S class id: [literal names]} READ from specthm.py's source (the class
    table's '"id": "S-n", "object": "S", "space": "S", "lits": {...}'
    entries) -- read, not imported: specthm imports this file."""
    path = os.path.join(HERE, "specthm.py") if path is None else path
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    out = {}
    for m in re.finditer(r'\{"id": "(S-\d+)", "object": "S", "space": "S", "lits": \{([^}]*)\}', src):
        out[m.group(1)] = sorted(re.findall(r'"(\w+)":', m.group(2)))
    return out


def spec_turn_note():
    """spec.py's PART 2 RULED note on item 27, READ from its docstring: the
    sentence that opens 'RULED (M, 2026-10-04; ...item 27)' up to its first
    full stop after the citation; None if spec.py no longer carries it."""
    import spec
    d = " ".join(spec.__doc__.split())
    m = re.search(r"(RULED \(M, 2026-10-04; docket68/M-RULINGS-2026-10-03\.md item 27\)\.)", d)
    return m.group(1) if m else None


def d66_turn_figures():
    """M-D68-27's figures, asked of defects.py: the ruling it records
    (TURN_RULING), and the straight string at the Planck Nambu-Goto bound with
    b = R_sun under both readings (string_turn)."""
    import spec
    sun = [x for x in spec.LENSES if x[0] == "Sun"][0]
    st = defects.string_turn(defects.PLANCK_NG_GMU, sun[2])
    return {"ruling": defects.TURN_RULING, "string": st, "AU": spec.AU,
            "L AU": st["crossing L"] / spec.AU,
            "L AU (line intersection)": st["crossing L (line intersection)"] / spec.AU}


D66_TURN = d66_turn_figures()


def _d68_g2(x):
    """5.3e5, as the paper prints Gott's gamma: two significant figures."""
    m, e = ("%.1e" % x).split("e")
    return "%se%d" % (m, int(e))


#: The owners' Gott figures item 26 bears on, asked of defects.py: the Lorentz
#: factor Gott's pair needs at the Planck 2013 Nambu-Goto and Abelian-Higgs
#: bounds (gott_gamma_needed, CFG94 eq.(32)).
D66_GOTT = {"NG": (defects.PLANCK_NG_GMU, defects.gott_gamma_needed(defects.PLANCK_NG_GMU)),
            "AH": (defects.PLANCK_AH_GMU, defects.gott_gamma_needed(defects.PLANCK_AH_GMU))}


def _paper_e(x):
    """1.5e−7, as the paper prints a bound (two figures, a true minus)."""
    m, e = ("%.1e" % x).split("e")
    return "%se%s%d" % (m, "\u2212" if int(e) < 0 else "", abs(int(e)))


def d66_paper_gott_figures(lines=None):
    """[(figure, found)] -- defects.py's Gott figures (gamma at the Planck
    Nambu-Goto and Abelian-Higgs bounds, and the bounds themselves) as the
    paper prints them, each looked for in the paper's line that carries the
    DOCKET 66 marker (READ); [] if the marker is not found."""
    lines = _paper_lines() if lines is None else lines
    ln, _t = paper_d66_marker(D68_M_WORDS["M-D68-26"][0], lines)
    if ln is None:
        return []
    line = lines[ln - 1]
    figs = ["\u03b3 > %s" % _d68_g2(D66_GOTT["NG"][1]), _paper_e(D66_GOTT["NG"][0]),
            "\u03b3 > %s" % _d68_g2(D66_GOTT["AH"][1]), _paper_e(D66_GOTT["AH"][0])]
    return [(f, f in line) for f in figs]


# ----- DOCKET 68 WAVE 3 AND STEP 1b (docstring section 8c) -----------------
# Their owners sit in docket68/wave3/ and step1b/ and are loaded HERE, not with
# the peers at the top, for two reasons, both checked by the selftest:
#   * openterms.py imports THIS file (for M_NEUTRON_KG, defined above).  When
#     this file runs as __main__ it is lent to that import under its own name
#     for the duration, so ledger.py is never loaded twice; when it is being
#     imported as 'ledger', that import finds it, already past M_NEUTRON_KG.
#   * docket68/wave3/corridor.py shares its NAME with this directory's
#     corridor.py.  It is loaded by path as 'w3corridor' and never registered
#     as 'corridor'; no other wave-3 or Step 1b owner has a namesake here, in
#     docket68/, docket66/ or tools/ (checked when this was seated), and none
#     imports corridor.
#   * this file can itself be reached FROM an owner part-way through its load
#     (bsupply.py and placement.py, run as __main__, import openterms, which
#     imports this file before it has finished).  Any owner already in
#     sys.modules is therefore set aside for the duration, this file loads its
#     own copies, and the originals are put back -- the outer chain resumes
#     with its own modules.  First written without this: bsupply.py's and
#     placement.py's selftests then failed on a partially initialised
#     openterms (W3S1B-seat's own run, 2026-10-05).
# The owners insert their own directories at the front of sys.path; sys.path
# is restored after the load, so nothing imported later is shadowed.
W3_DIR = os.path.join(D68_DIR, "wave3")
S1B_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step1b")
W3S1B_OWNERS = ("balance", "compensate", "openterms", "bsupply", "placement",
                "criteria12", "seatrank", "aperture")


def _w3s1b_load():
    """{name: module} for the nine owners, corridor.py as 'w3corridor'; and
    the facts the selftest checks about the load itself."""
    import importlib
    import importlib.util
    saved = list(sys.path)
    stashed = dict((n, sys.modules.pop(n)) for n in W3S1B_OWNERS if n in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    try:
        sys.path.append(S1B_DIR)
        sys.path.append(W3_DIR)
        with contextlib.redirect_stdout(io.StringIO()):
            mods = dict((n, importlib.import_module(n)) for n in W3S1B_OWNERS)
            spec = importlib.util.spec_from_file_location(
                "w3corridor", os.path.join(W3_DIR, "corridor.py"))
            cor = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cor)
        mods["w3corridor"] = cor
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        sys.modules.update(stashed)
    facts = {"lent": lent, "path_restored": sys.path == saved, "set_aside": sorted(stashed),
             "put_back": all(sys.modules.get(n) is m for n, m in stashed.items()),
             "openterms_ledger": getattr(mods["openterms"], "ledger", None) is sys.modules[__name__],
             "corridor_registered": "w3corridor" in sys.modules
             or getattr(sys.modules.get("corridor"), "__file__", "") == cor.__file__}
    return mods, facts


W3S1B, W3S1B_LOAD = _w3s1b_load()


def _g(x, n=3):
    """A figure as the owners print it: n significant figures."""
    return "%.*g" % (n, x)


def w3s1b_asked():
    """Every wave-3 and Step 1b value a cell below prints, ASKED of its owner
    at call time (all cheap: about a second in total)."""
    b, cm, ot = W3S1B["balance"], W3S1B["compensate"], W3S1B["openterms"]
    bs, pl = W3S1B["bsupply"], W3S1B["placement"]
    c12, sr, ap, co = W3S1B["criteria12"], W3S1B["seatrank"], W3S1B["aperture"], W3S1B["w3corridor"]
    with contextlib.redirect_stdout(io.StringIO()):
        counts = b.counts()
        bits = counts[0][1]
        eq = b.equation(bits, "R-QUANTUM")
        out = {
            "counts": counts, "eq_ids": [r[0] for r in eq], "eq_open": b.open_terms(eq),
            "eq_unaccounted": b.unaccounted(eq), "eq_energy_total": b.energy_total(eq),
            "qvb": b.quantum_value_balance(), "nc": b.no_cloning(), "stock": b.stock_terms(),
            "closure": b.conserved_closure(),
            "frame": cm.frame_defect(), "ebb": cm.energy_buys_bits(),
            "bbf": cm.baryon_from_energy_floor(),
            "read": ot.read_terms(), "chem": ot.chem_ceiling_j(), "retire": ot.retire_term(),
            "flux": bs.flux_b(), "flux_boy": bs.flux_b_boyajian(),
            "days": bs.collect()["chem_100m2_days"],
            "floor": pl.floor_total(bits, "R-CLASSICAL"), "sei": pl.stock_entropy_illustration(),
            "conc": co.mid_transfer_concurrence()[0], "sig": co.signalling_coupled(),
            "interior": co.interior_occupation(), "bl": co.before_light(),
            "kinds": c12.kinds(), "alpha": c12.alpha_ab_bound(), "dvb": c12.definite_vs_bell(),
            "rrs": c12.rrs_lower_bound(seat.YEAR_S), "carrier": c12.carrier_route(),
            "pred": c12.predetermination(),
            "family": sr.family_prediction(), "tri": sr.triangulation(), "cost": sr.cost_table(),
            "ap": ap.collect(),
        }
    return out


W3S1B_ASKED = w3s1b_asked()


def w3s1b_owner_words():
    """[(owner constant, held id, the owner's text occurs in the held words)]
    -- each owner's own copy of M's words against the ledger's (D68_M_WORDS /
    D68_CARRIED_WORDS), so neither can drift alone."""
    pairs = (("balance.M_WORDS_29", W3S1B["balance"].M_WORDS_29, "M-D68-29"),
             ("balance.M_WORDS_30", W3S1B["balance"].M_WORDS_30, "M-D68-30"),
             ("balance.M_WORDS_32", W3S1B["balance"].M_WORDS_32, "M-D68-32"),
             ("compensate.M_WORDS_31", W3S1B["compensate"].M_WORDS_31, "M-D68-31"),
             ("w3corridor.M_WORDS_21", W3S1B["w3corridor"].M_WORDS_21, "M-D68-21"),
             ("criteria12.M_WORDS_23", W3S1B["criteria12"].M_WORDS_23, "M-D68-23"),
             ("seatrank.M_WORDS_25", W3S1B["seatrank"].M_WORDS_25, "M-D68-25"),
             ("aperture.M_WORDS", W3S1B["aperture"].M_WORDS, "M-D68-35"))
    return [(name, rid, " ".join(w.split()) in " ".join(_d68_held(rid)[0].split()))
            for name, w, rid in pairs]


def _w3_streamed(count_prefix, T):
    a = W3S1B_ASKED["ap"]
    return [r for r in a["streamed"] if r["count"].startswith(count_prefix) and r["T_s"] == T][0]


def w3_throat_factors():
    """(smallest, largest) factor by which an information-sized throat
    (aperture.py's all-at-once radii, and its streamed openings over the
    three schedules, every count) lowers the throat mass against the 1 m
    throat's -- asked of aperture.collect."""
    a = W3S1B_ASKED["ap"]
    m1 = a["one_metre_throat_mass_kg"]
    ms = [r["throat_mass_kg"] for r in a["all_at_once"]] + [r["throat_mass_kg"] for r in a["streamed"]]
    return m1 / max(ms), m1 / min(ms)


# ----- STEP 1c (docstring section 8d) --------------------------------------
# Its owners sit in step1c/ and SHARE THEIR NAMES with modules in this
# directory (demand.py, supply.py, coupling.py), so each is loaded by PATH
# under a private name ('s1c_demand', ...), never by its bare name; the selftest
# checks the bare names still answer to this directory's modules.  step1c's
# demand.py reaches step1b's openterms, which imports THIS file: the same
# lending and setting-aside as _w3s1b_load (section 8c), so a run of a step1c
# owner as __main__ that reaches this file part-way through its own load still
# finds a whole set of owners.
S1C_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "step1c")
S1C_OWNERS = ("demand", "supply", "coupling", "nonlocal", "coherence")


def _s1c_load():
    """{name: module} for step1c's five owners, each loaded by path as 's1c_<name>'; and the facts the selftest checks
    about the load."""
    import importlib.util
    saved = list(sys.path)
    keys = ["s1c_" + n for n in S1C_OWNERS] + list(W3S1B_OWNERS)
    stashed = dict((k, sys.modules.pop(k)) for k in keys if k in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    mods = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for n in S1C_OWNERS:
                key = "s1c_" + n
                if key in sys.modules:          # loaded already as a sibling of an earlier owner
                    mods[n] = sys.modules[key]
                    continue
                spec = importlib.util.spec_from_file_location(key, os.path.join(S1C_DIR, n + ".py"))
                m = importlib.util.module_from_spec(spec)
                sys.modules[key] = m
                spec.loader.exec_module(m)
                mods[n] = m
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        for k in ["s1c_" + n for n in S1C_OWNERS]:
            sys.modules.pop(k, None)
        sys.modules.update(stashed)
    facts = {"path_restored": sys.path == saved, "set_aside": sorted(stashed),
             "bare_names_not_step1c": [n for n in ("demand", "supply", "coupling")
                                       if os.path.dirname(os.path.abspath(
                                           getattr(sys.modules.get(n), "__file__", "") or "x")) == S1C_DIR],
             "from_step1c": [n for n, m in mods.items() if os.path.dirname(os.path.abspath(m.__file__)) != S1C_DIR]}
    return mods, facts


S1C, S1C_LOAD = _s1c_load()


def s1c_asked():
    """Every Step 1c value a cell below prints, ASKED of its owner at call time."""
    de, su, co, nl, ch = (S1C[n] for n in S1C_OWNERS)
    with contextlib.redirect_stdout(io.StringIO()):
        g = su.gaps()
        yr = [r for r in g["rows"] if r["schedule"] == "1 yr"][0]
        cs = co.supply_rows()
        cen = [r for r in co.demand_rows() if r["schedule"] == "1 century"][0]
        nd = nl.collect()
        cd = ch.collect()
        out = {
            "crossover_yr": de.collect()["crossover_yr"],
            "gap_1yr": yr, "best": g["best"],
            "link_power_rise_1yr": su.link_at_proxima()["power_rise_needed"]["1 yr"],
            "dsoc_law": su.dsoc_law_test()["measured_over_predicted"],
            "dsoc_long": su.dsoc_long_range_test()["measured_over_predicted"],
            "errors": su.placement_errors(),
            "inst_signal_century": co.instantaneous_signal(cen["J_pair_rad_s"]),
            "near_field_m": (cs["rydberg_near_field_limit_m"], cs["kotler_near_field_limit_m"]),
            "J_far": cs["rydberg_J_far_at_L_rad_s"], "J_century": cen["J_pair_rad_s"],
            "dipole_over_L": co.dipole_needed(cen["J_pair_rad_s"])["separation_over_L"],
            "frame": nd["frame"], "tightest": nd["tightest"], "tightest_C": nd["tightest_C"],
            "falloff_alpha": nd["falloff_alpha"], "day_J": nd["demand_J"]["1 day"],
            "hold_by_source": cd["demand"]["hold_by_source"],
            "shortfall_by_overhead": cd["shortfall_by_overhead"],
            "best_T2_s": ch.best_measured(),
        }
    return out


S1C_ASKED = s1c_asked()

#: WHAT STEP 1c LEAVES OPEN (docstring section 8d), as step1c/DEVICE.md states
#: it: (id, what is open, what would answer it, owner).  Named, not ranked.
S1C_OPEN = [
    ("S1C-O1", "an atom-resolving read of a bulk object that reads every atom it removes, or removes none, at any "
     "rate", "a demonstrated method, READ at source", "step1c/supply.py"),
    ("S1C-O2", "placement into a bonded solid at any demonstrated rate", "a demonstrated rate, READ at source",
     "step1c/supply.py"),
    ("S1C-O3", "an optical link rate measured beyond 400e6 km (DSOC's 494e6 km contact states no rate)",
     "a measured rate at a larger distance", "step1c/supply.py"),
    ("S1C-O4", "whether the speed-free routes make a non-local J distance-free (H-J-DISTANCE-FREE)", "a model or a "
     "measurement of J against separation", "step1c/nonlocal.py"),
    ("S1C-O5", "which NIST aggregate Table S-II is (1-pulse or 5-pulse margin); whether Munich's runs are the per-run "
     "maximum", "the supplements, READ", "step1c/nonlocal.py"),
    ("S1C-O6", "a fault-tolerant memory holding a quantum payload for years (H-FT-MEMORY), and its operations and energy "
     "on 9.5e27 x k physical qubits", "a demonstrated memory, and the demand priced", "step1c/coherence.py"),
    ("S1C-O7", "the spins per ensemble-stored qubit (H-ENSEMBLE-PER-QUBIT)", "the count, READ or computed",
     "step1c/coherence.py"),
    ("S1C-O8", "the transmitted power at the device's apertures (seat.channel_floor establishes received power only)",
     "the link budget with diffraction loss, computed", "step1c/supply.py"),
]


# ----- DOCKET 68 WAVE 4 AND THE CLOSE (docstring section 8e) ---------------
# Wave 4's owners sit in docket68/wave4/ and reach step1c's owners by path
# (they register 's1c_*' keys); loaded here BY PATH as 'w4_<name>', with the
# same lending and setting-aside as _s1c_load, and every 's1c_*' key they add
# removed afterwards.
W4_DIR = os.path.join(D68_DIR, "wave4")
W4_OWNERS = ("linkbudget", "ftmemory")
D68_CLOSE_FILE = os.path.join(D68_DIR, "CLOSE.md")


def _w4_load():
    """{name: module} for wave 4's two owners, loaded by path as 'w4_<name>'; and the load facts."""
    import importlib.util
    saved = list(sys.path)
    keys = ["s1c_" + n for n in S1C_OWNERS] + list(W3S1B_OWNERS)
    stashed = dict((k, sys.modules.pop(k)) for k in keys if k in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    mods = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for n in W4_OWNERS:
                spec = importlib.util.spec_from_file_location("w4_" + n, os.path.join(W4_DIR, n + ".py"))
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                mods[n] = m
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        for k in ["s1c_" + n for n in S1C_OWNERS]:
            sys.modules.pop(k, None)
        sys.modules.update(stashed)
    return mods, {"path_restored": sys.path == saved,
                  "from_wave4": [n for n, m in mods.items() if os.path.dirname(os.path.abspath(m.__file__)) != W4_DIR]}


W4, W4_LOAD = _w4_load()


def w4_asked():
    """Every wave-4 value a cell below prints, ASKED of its owner at call time."""
    with contextlib.redirect_stdout(io.StringIO()):
        lb = W4["linkbudget"].collect()
        fm = W4["ftmemory"].collect()
    yr = [b for b in lb["budget"] if b["schedule"] == "1 yr"][0]
    fl = lb["figure_limited_1yr"]
    sp = list(fm["by_count"].values())[0]
    return {"kT_keV": yr["kT_eV"] / 1e3, "single_mode_D_m": yr["single_mode_D_m"],
            "fig_min_Lsun": min(v["P_t_over_L_sun"] for k, v in fl.items() if isinstance(v, dict)),
            "fig_max_Lsun": max(v["P_t_over_L_sun"] for k, v in fl.items() if isinstance(v, dict)),
            "sun_width_arcsec": lb["sun_threshold_width_arcsec"]["7 m^2 (design)"],
            "d": sp["d"], "phys": sp["physical_qubits"], "per_atom": sp["qubits_per_object_atom"],
            "landauer_J": sp["landauer_J"], "failures_at_floor": sp["failures_at_floor"],
            "d_half": fm["tolerance"]["50% of the payload"]["d"]}


W4_ASKED = w4_asked()


def d68_close_sections():
    """docket68/CLOSE.md's numbered section headings, READ (the '## ' stripped); [] if absent."""
    if not os.path.exists(D68_CLOSE_FILE):
        return []
    with open(D68_CLOSE_FILE, encoding="utf-8") as fh:
        return [ln[3:].strip() for ln in fh if ln.startswith("## ")]


#: WHAT WAVE 4 LEAVES OPEN (docstring section 8e), as docket68/wave4/WAVE4.md
#: states it.  Named, not ranked.
W4_OPEN = [
    ("W4-O1", "a focusing optic at the floor quantum (263 keV at a year; 96 MeV at a day) with a measured figure",
     "a demonstrated optic, READ at source", "docket68/wave4/linkbudget.py"),
    ("W4-O2", "a coherent source at the floor quantum (H-NO-COHERENT-SOURCE)", "a demonstrated source, READ",
     "docket68/wave4/linkbudget.py"),
    ("W4-O3", "the minimum transmitted power over quanta (seat's floor cannot be evaluated off its optimum)",
     "a floor evaluated at any quantum, computed", "docket68/wave4/linkbudget.py"),
    ("W4-O4", "the origin and removal of the 1e-10 burst floor; whether Lambda holds to distance 245",
     "a measured memory at that distance, READ", "docket68/wave4/ftmemory.py"),
    ("W4-O5", "the streamed hold of a quantum payload (H-INSTANT-ASSEMBLY)", "a progressive coherent assembly, "
     "computed or READ", "docket68/wave4/ftmemory.py"),
    ("W4-O6", "the real dissipation of either subsystem", "a measured dissipation, READ",
     "docket68/wave4/ftmemory.py"),
]


# ----- THE Q-1s GATE AND H-CMB-CORRIDOR READING 1 (docstring section 8f) ----
# Reading 1's owner sits in docket68/cmb/ and reaches frame.py and
# step1c/nonlocal.py by path (it registers 'cmb_frame' and 's1c_*' keys);
# loaded here BY PATH as 'cmb_cmbframe', with the same lending and
# setting-aside as _w4_load, and every such key it adds removed afterwards.
CMB_DIR = os.path.join(D68_DIR, "cmb")
CMB_OWNERS = ("cmbframe",)
Q1S_GATE_FILE = os.path.join(D68_DIR, "Q1s-PRIORART.md")


def _cmb_load():
    """{name: module} for reading 1's owner, loaded by path as 'cmb_<name>'; and the load facts."""
    import importlib.util
    saved = list(sys.path)
    added = ["s1c_" + n for n in S1C_OWNERS] + ["cmb_frame"]
    keys = added + list(W3S1B_OWNERS)
    stashed = dict((k, sys.modules.pop(k)) for k in keys if k in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    mods = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for n in CMB_OWNERS:
                spec = importlib.util.spec_from_file_location("cmb_" + n, os.path.join(CMB_DIR, n + ".py"))
                m = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(m)
                mods[n] = m
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        for k in added:
            sys.modules.pop(k, None)
        sys.modules.update(stashed)
    return mods, {"path_restored": sys.path == saved,
                  "from_cmb": [n for n, m in mods.items() if os.path.dirname(os.path.abspath(m.__file__)) != CMB_DIR]}


CMB, CMB_LOAD = _cmb_load()


def cmb_asked():
    """Every reading-1 value a cell below prints, ASKED of its owner at call time."""
    cf = CMB["cmbframe"]
    with contextlib.redirect_stdout(io.StringIO()):
        d = cf.collect()
    ld, lf, mf, un = d["lead"], d["lab_frame"], d["matter_frames"], d["universal"]
    q = mf["quasar dipole read kinematically (WISE 2022)"]
    return {"beta_amp": d["physics"]["beta_from_amp_over_T0"], "T": d["physics"]["T_ahead_across_behind"],
            "theta": d["geometry"]["theta_deg"], "lead_h": ld["lead_h"], "annual_s": ld["annual_mod_earth_frame_s"],
            "sigma_s": ld["sigma_dipole_s"], "lab_all": all(v["holds"] for v in lf["tests"].values()),
            "n_tests": len(lf["tests"]), "J_tight": min(v["J_bound_cmb_A_or_B"] for v in lf["tests"].values()),
            "J_factor_max": max(v["J_factor"] for v in lf["tests"].values()),
            "q_max_h": max(abs(x) for x in q["signed_shift_range_h"]), "lg_shift_h": mf["Local Group"]["shift_h"],
            "gap_orders": un["slicing_gap_orders"], "dTT_lead": un["dT_over_T_to_resolve_lead"],
            "tz_max_sigma": max(v["n_sigma"] for v in un["T_of_z"].values()),
            "scarani": [v["v_min_over_c"] for v in cf.CMB_FRAME_SPEED_BOUNDS.values() if v["v_min_over_c"]][0]}


CMB_ASKED = cmb_asked()


def _cmb_fig(f, s=1.0):
    """The reading-1 figures M-D68-45's cell prints, formatted once (the selftest's needles use the same)."""
    return {"theta": "%.2f" % (s * f["theta"]), "lead_h": "%.2f" % (s * f["lead_h"]),
            "sigma": "%.1f" % (s * f["sigma_s"]), "J": _g(s * f["J_tight"]), "qmax": "%.1f" % (s * f["q_max_h"])}


def q1s_gate_sections():
    """docket68/Q1s-PRIORART.md's section headings, READ (the '## ' stripped); [] if absent."""
    if not os.path.exists(Q1S_GATE_FILE):
        return []
    with open(Q1S_GATE_FILE, encoding="utf-8") as fh:
        return [ln[3:].strip() for ln in fh if ln.startswith("## ")]


#: WHAT H-CMB-CORRIDOR READING 1 LEAVES OPEN (docstring section 8f), as
#: docket68/cmb/CMB.md states it.  Named, not ranked.
CMB_OPEN = [
    ("CMB-O1", "which frame H-FRAME means if the matter dipole is kinematic (reading b): the CMB rest frame or the "
     "frame matter defines", "a resolution of the cosmic dipole anomaly, READ", "docket68/cmb/cmbframe.py"),
    ("CMB-O2", "H-CMB-UNIVERSAL's multi-spacetime clause", "any measurement bearing on it", "docket68/cmb/cmbframe.py"),
    ("CMB-O3", "the other readings of H-CMB-CORRIDOR: the background as the medium, as the register, as the coupling's "
     "carrier (M-D68-45: the medium next)", "each priced against READ figures, computed", "docket68/cmb/CMB.md"),
    ("CMB-O4", "a CMB-frame speed-of-influence figure from Salart 2008 or Yin 2013 at the CMB's own beta (none is "
     "printed)", "a printed figure, READ", "docket68/cmb/cmbframe.py"),
]


# ----- H-CMB-CORRIDOR READINGS 2 AND 3, AND THE LOCAL CLOCKS (docstring 8g) --
# The owners sit in docket68/cmb/ and reach cmbframe.py, nosig.py and
# step1c/demand.py by path (keys 'cmb_*', 'd68_nosig', 's1c_demand',
# 'cmb_frame', 's1c_nonlocal').  Loaded here BY PATH with the ledger lent; every
# module key the load adds is removed after, and any key it would displace is
# stashed first and restored.
CMB2_OWNERS = ("medium", "unobserved", "localclock")


def _cmb2_load():
    """{name: module} for readings 2 and 3 and the local clocks, loaded by path as 'cmb_<name>'; and the load facts."""
    import importlib.util
    saved = list(sys.path)
    before = set(sys.modules)
    collide = (["cmb_" + n for n in ("cmbframe",) + CMB2_OWNERS] + ["d68_nosig", "s1c_demand", "cmb_frame"]
               + ["s1c_" + n for n in S1C_OWNERS] + list(W3S1B_OWNERS))
    stashed = dict((k, sys.modules.pop(k)) for k in collide if k in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    mods = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for n in CMB2_OWNERS:
                key = "cmb_" + n
                if key in sys.modules:
                    mods[n] = sys.modules[key]
                    continue
                spec = importlib.util.spec_from_file_location(key, os.path.join(CMB_DIR, n + ".py"))
                m = importlib.util.module_from_spec(spec)
                sys.modules[key] = m
                spec.loader.exec_module(m)
                mods[n] = m
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        added = [k for k in sys.modules if k not in before]
        for k in added:
            sys.modules.pop(k, None)
        sys.modules.update(stashed)
    return mods, {"path_restored": sys.path == saved, "keys_left": [k for k in added if k in sys.modules],
                  "from_cmb": [n for n, m in mods.items() if os.path.dirname(os.path.abspath(m.__file__)) != CMB_DIR]}


CMB2, CMB2_LOAD = _cmb2_load()


def cmb2_asked():
    """Every reading-2, reading-3 and local-clock value a cell below prints, ASKED of its owner at call time."""
    with contextlib.redirect_stdout(io.StringIO()):
        dm = CMB2["medium"].collect()
        du = CMB2["unobserved"].compute()
        dl = CMB2["localclock"].compute()
    co, ap, ns, ct = dm["collisionless"], dm["acoustic_past"], dm["noise_and_sink"], dm["contraction"]
    lcl, cf, dq = dl["local_clocks"], dl["cmb_frame"], dl["delocalised_qubit"]
    return {"mfp_orders": co["orders_mean"], "cs": ap["cs_over_c_at_R_star"], "T_dec": ap["T_decoupling_K"],
            "landauer_J": ns["landauer_J"], "trace_L": dm["coherence"]["L"]["trace"],
            "lqc_ratio": ct["T_max_over_T_pl"], "slow_T": ct["slow_T_reached_K"],
            "lemma": ct["lemma"]["claim"],
            "td_ground": [du["readings_ground"][k]["TD"] for k in ("uniform ticks", "conformal time", "cosmic time")],
            "td_control": max(du["readings_ground_constant_g"][k]["TD"]
                              for k in ("uniform ticks", "conformal time", "cosmic time")),
            "sel_diff": du["selection"]["difference_before_vs_coherent"],
            "agree_link": du["perspectives"]["P_agree_cross_perspective_link"],
            "sky_mK": 1e3 * du["skies"]["dipole_difference_K"], "o9_a": du["o9"]["max_marginal_shift_a"],
            "clock_s": lcl["seconds_per_year"], "clock_sigma": lcl["sigma_seconds_per_year"],
            "lc_vs_iau": lcl["A_vs_IAU_LC"], "cmb_frame_s": cf["prox_minus_sun_seconds_per_year"],
            "sun_frame_s": lcl["sun_frame_motion_term_seconds_per_year"], "f_1rad": dq["f_max_sigma_1rad_Hz"]}


CMB2_ASKED = cmb2_asked()


def _cmb2_fig(f, s=1.0):
    """The figures M-D68-54's cell prints, formatted once (the selftest's needles use the same)."""
    return {"mfp": "%.1f" % (s * f["mfp_orders"]), "cs": "%.3f" % (s * f["cs"]),
            "td": "%.3f" % (s * f["td_ground"][0]), "clock": "%.3f" % (s * f["clock_s"]),
            "cmbf": "%.3f" % (s * f["cmb_frame_s"])}


#: WHAT READINGS 2 AND 3 AND THE LOCAL CLOCKS LEAVE OPEN (docstring section
#: 8g), as MEDIUM.md, UNOBSERVED.md and LOCALCLOCK.md state them.  Named, not
#: ranked.
CMB2_OPEN = [
    ("CMB2-O1", "whether the universe will contract, and what the background does through a bounce (H-CONTRACT)",
     "a measurement of future contraction, or of evolving dark energy at high significance, READ",
     "docket68/cmb/medium.py"),
    # CMB2-O2 and CMB2-O4 first said support.py and bias.py were 'built and verified, not seated' (CMB2-seat); both
    # are seated in section 8h (M-D68-55), and the items now say what stays open there.
    ("CMB2-O2", "how observation extends the clock's support (H-M-SUPPORT's dynamics); support.py's record reading "
     "(seated, section 8h) agrees with M-SUPPORT largely by construction", "a dynamics that is not by construction",
     "docket68/cmb/support.py"),
    ("CMB2-O3", "which clock weighting, if any, is physical (H-CLOCK-WEIGHT)", "a physical principle fixing it, READ",
     "docket68/cmb/unobserved.py"),
    ("CMB2-O4", "any experiment separating sentient from physical observation, or measuring an outcome bias with "
     "conscious intention on an entangled pair (H-CONSCIOUS-SELECTS reading b); bias.py prices it (seated, section 8h)",
     "an interference/Zeno test of a consciousness-collapse model, or a bias with its sign, READ",
     "docket68/cmb/bias.py"),
    ("CMB2-O5", "a clock that interacts with the system it times (the relational-time equivalence is not shown "
     "there)", "a result for interacting clocks, READ", "docket68/cmb/localclock.py"),
    ("CMB2-O6", "Page & Wootters 1983, the Feynman-Kitaev originals and the full Hartle & Hawking 1983",
     "each READ at source", "docket68/cmb/UNOBSERVED.md"),
]


# ----- M-SUPPORT'S DYNAMICS AND READING (b)'S PRICE (docstring section 8h) --
CMB3_OWNERS = ("support", "bias")


def _cmb3_load():
    """{name: module} for support.py and bias.py, loaded by path as 'cmb_<name>' with _cmb2_load's lending and key
    restoration; and the load facts."""
    import importlib.util
    saved = list(sys.path)
    before = set(sys.modules)
    collide = (["cmb_" + n for n in ("cmbframe",) + CMB2_OWNERS + CMB3_OWNERS]
               + ["d68_nosig", "s1c_demand", "cmb_frame", "wd_arrival"]
               + ["s1c_" + n for n in S1C_OWNERS] + list(W3S1B_OWNERS))
    stashed = dict((k, sys.modules.pop(k)) for k in collide if k in sys.modules)
    lent = "ledger" not in sys.modules
    if lent:
        sys.modules["ledger"] = sys.modules[__name__]
    mods = {}
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            for n in CMB3_OWNERS:
                key = "cmb_" + n
                spec = importlib.util.spec_from_file_location(key, os.path.join(CMB_DIR, n + ".py"))
                m = importlib.util.module_from_spec(spec)
                sys.modules[key] = m
                spec.loader.exec_module(m)
                mods[n] = m
    finally:
        sys.path[:] = saved
        if lent:
            del sys.modules["ledger"]
        added = [k for k in sys.modules if k not in before]
        for k in added:
            sys.modules.pop(k, None)
        sys.modules.update(stashed)
    return mods, {"path_restored": sys.path == saved, "keys_left": [k for k in added if k in sys.modules],
                  "from_cmb": [n for n, m in mods.items() if os.path.dirname(os.path.abspath(m.__file__)) != CMB_DIR]}


CMB3, CMB3_LOAD = _cmb3_load()


def cmb3_asked():
    """Every support.py and bias.py value M-D68-55's cell prints, ASKED of its owner at call time."""
    with contextlib.redirect_stdout(io.StringIO()):
        ds = CMB3["support"].compute()
        db = CMB3["bias"].compute()
    r, t = ds["records"], ds["toy"]
    rows = dict((x["case"], x) for x in db["rows"])
    re_ = [x for x in db["rows"] if x["case"].startswith("Bosch 2006 random")][0]
    fe = [x for x in db["rows"] if x["case"].startswith("Bosch 2006 fixed")][0]
    return {"z_star": r["z_tau1"], "z_gamma_H": r["z_gamma_eq_H"], "z_peak": r["z_peak"],
            "reion_share": r["last_record_reion"], "toy_rec": t["ALL-RECORDS"]["TD_vs_static_M_SUPPORT"],
            "toy_free": t["record_free_T8_TD"], "toy_amb": t["M_SUPPORT_reweighting_ambiguity"],
            "toy_norec": t["no_recombination_thomson_TD"], "sw_rms_yr": ds["local"]["decoupling_time_offset_rms_yr"],
            "eps_re": re_["eps"], "bits_re": re_["bits_per_pair"], "eps_fe": fe["eps"], "bits_fe": fe["bits_per_pair"],
            "bf_r01": db["bayes"]["r=0.1"], "bf_point": db["bayes"]["point at Bosch's size (raw)"],
            "reading_a": db["reading_a_marginal_spread"], "n_rows": len(rows)}


CMB3_ASKED = cmb3_asked()


def _cmb3_fig(f, s=1.0):
    """The figures M-D68-55's cell prints, formatted once (the selftest's needles use the same)."""
    return {"z_star": "%.2f" % (s * f["z_star"]), "z_gH": "%.0f" % (s * f["z_gamma_H"]),
            "norec": "%.3f" % (s * f["toy_norec"]), "bf": "%.2f" % (s * f["bf_r01"]),
            "bits_re": _g(s * f["bits_re"], 2)}


#: WHAT SUPPORT.PY AND BIAS.PY LEAVE OPEN (docstring section 8h), as SUPPORT.md
#: and BIAS.md state them.  Named, not ranked.
CMB3_OPEN = [
    ("CMB3-O1", "whether photon (Thomson) records are the right records for M-SUPPORT, and where a record lasts "
     "(H-SUPPORT-IS-RECORDS, H-RECORD-DURABLE)", "decoherence sources READ (Joos-Zeh, Zurek; relational QM)",
     "docket68/cmb/support.py"),
    ("CMB3-O2", "whether LAST-RECORD or ALL-RECORDS is M's support", "M's ruling, or a principle READ",
     "docket68/cmb/SUPPORT.md"),
    ("CMB3-O3", "Bosch et al.'s primary, with both estimates and their intervals, and the MegaREG primary",
     "each READ by a route whose permission is established", "docket68/cmb/bias.py"),
    ("CMB3-O4", "a channel model under H-Z-PER-SESSION (a fixed z per act of intention, not per pair)",
     "a computed pricing", "docket68/cmb/BIAS.md"),
    ("CMB3-O5", "z* beyond its agreement and the low-ell anisotropy with the integrated Sachs-Wolfe term",
     "helium recombination, the matter temperature equation and an ISW term, computed", "docket68/cmb/support.py"),
]


#: WHAT DOCKET 68 WAVE 3 AND STEP 1b LEAVE OPEN (docstring section 8c), as
#: their owners' records state it (step1b/BALANCE.md, docket68/wave3/WAVE3.md):
#: (id, what is open, what would answer it, owner).  Named, not ranked (section
#: 3: this file does not rank the open questions).  No board row is opened for
#: them: none moves a requirement or a grade a row reads (H-NO-W3S1B-ROW).
W3S1B_OPEN = [
    ("S1B-O1", "H-WHICH-COUNT: which of the four counts is the object's information (M-D68-33: "
     "keep all four)", "a ruling or a measurement that singles one out", "balance.py"),
    ("S1B-O2", "H-STOCK-FORM: whether A's residue and B's stock share a form, which fixes the "
     "retire energy's sign and the chemical deficit at B", "the residue's and the stock's "
     "composition, stated", "openterms.py, balance.py"),
    ("S1B-O3", "H-STOCK-ENTROPY: B's stock is not a blank; ordering it exports T_B dS, local to B",
     "the stock's entropy before and after assembly, measured or bounded", "placement.py"),
    ("S1B-O4", "any ceiling on placement at B", "a bound on the work to place each atom, beyond "
     "the returned loan of the trap's zero-point energy", "placement.py"),
    ("S1B-O5", "the collector at B (H-COLLECT, H-AT-ORBIT, H-STEADY)", "a collector's area and "
     "efficiency at Proxima b, with its flares and atmosphere", "bsupply.py"),
    ("S1B-O6", "the Faria-Boyajian luminosity discrepancy (0.0016 +- 0.0006 against 0.00155 +- "
     "0.00002 L_sun)", "recorded, not adjudicated: a primary-source reading of Faria's spread",
     "bsupply.py"),
    ("S1B-O7", "H-READ-BEFORE-DAMAGE: an absorbed read destroys the object while reading it",
     "a read that completes before the damage it causes, or a near-field read (H-NEAR-FIELD)",
     "openterms.py"),
    ("W3-O1", "the speed-free coupling: each route (direct, long-range with alpha < d, "
     "unbounded J) clashes with H-LOCALITY", "a coupling that is speed-free and microcausal, "
     "shown", "corridor.py"),
    ("W3-O2", "H-12-CARRIER for alpha_s, G and v: no READ bound excludes a state-dependent "
     "constant", "a READ bound, or a measurement, on each", "criteria12.py"),
    ("W3-O3", "the stock gate at Proxima: P, the binder, is unmeasured there", "a measurement of "
     "P in a Proxima-system star or body", "criteria12.py, seat.py"),
    ("W3-O4", "whether the seat quasi-distribution is a Wigner function (H-WIGNER-SEATS) or "
     "belongs to a known family (H-CONSTRAINED-FAMILY)", "the seat distribution, defined",
     "seatrank.py"),
    ("W3-O5", "complex binary (M-D68-25): not addressed in W3C; the board's reading of complex "
     "values is signed.py's Im H = pi N", "M's meaning, asked, or a computation on it",
     "seatrank.py, signed.py"),
    ("W3-O6", "spatial bounds on the seven constants with none READ here", "READ bounds at "
     "source", "criteria12.py"),
]


D68_RULED = [
    ("M-D68-1",
     "Clash (d), H-INFO-S against B-RECV (the question as M-RULINGS-2026-10-03.md item 1 "
     "heads it): does information at the destination suffice to constitute the matter, "
     "against the board's holding that the arriving state needs a receiver already there?",
     "measure.py graded H-INFO-S a CLASH with B-RECV; transit.CARRIES_SUBSTANCE = %s"
     % transit.CARRIES_SUBSTANCE,
     _d68_rule("THE READING H-INFO-SHAPE", "M-D68-1",
               "carried as H-INFO-SHAPE (combine's SHAPE; measure.GRADES grades it %s): what "
               "arrives is the defining information, not substance (transit.CARRIES_SUBSTANCE "
               "= %s).  The clash is dissolved by relocation, not removed by assertion: M's "
               "ruling, encoded, and z3 shows only that the encoding is consistent.  H-INFO-S "
               "is kept as the alternative reading and as history"
               % (measure.GRADES[combine.SHAPE_GRADE_KEY]["verdict"], transit.CARRIES_SUBSTANCE)),
     "O-MATTER's relocation (M-D68-5) and O9's O-SEAT reading"),
    ("M-D68-2",
     "Weighting in the mean-value axiom (M-RULINGS-2026-10-03.md item 2): signed w, which "
     "selects Re H, or |w|, which selects signed Renyi?",
     "signed.py computes both and the axioms each satisfies",
     _d68_rule("CARRY BOTH", "M-D68-2",
               "both are carried, each with the axioms it satisfies (signed.py section (8), "
               "Q1s-signed.md section 9; the |w| family at orders %s, signed.WEIGHTING_ALPHAS); "
               "they are separated only conditionally, under the named H-BFL-BINDS (M-D68-8)"
               % (signed.WEIGHTING_ALPHAS,)),
     "Q-1s carries both until a computation or M separates them"),
    ("M-D68-3",
     "'All its inverses and reflections' (M-RULINGS-2026-10-03.md item 3): which of the log "
     "branches, the conjugate and reciprocal, the fold to |p|, and the Radon inverse?",
     "M's own words on Q-1s (CHARTER.md, M-D68-C8) name inverses and reflections",
     _d68_rule("ALL FOUR, CENTRED AT THE GROUND STATE", "M-D68-3",
               "all four on one multi-axis table centred at the ground state (signed.py "
               "section (9), Q1s-signed.md section 10); a signed weight reads as a deviation "
               "from the ground state (H-ZERO's reading).  Which ground-state quantities was "
               "asked of M and is M-D68-6"),
     "Q-1s's reflections table; the calibration question, answered by M-D68-6"),
    ("M-D68-4",
     "DOCKET 67's held OPEN rows at (0,-1,0) in index3.py (M-RULINGS-2026-10-03.md item 4): "
     "move them to the null cell, or keep them held?",
     "index3.py holds them under OPEN-AT-NULL-HELD, for M: the move would seat them on the "
     "null cell its own rule says is not a finding",
     _d68_rule("KEEP HELD, NOTED", "M-D68-4",
               "they stay as they are, each text saying its -1 is not a bound: %s "
               "(index3.OPEN_AT_NULL_HELD, asked)" % ", ".join(_d68_index3_held())),
     "nothing moves; index3.py's pins stand"),
    ("M-D68-5",
     "Is what arrives the defining information that shapes the geometry at the seat, with "
     "the physical substance supplied by the seat itself? (asked as "
     "M-RULINGS-2026-10-03.md item 5 records it)",
     "M-D68-1's reading left open where the substance comes from",
     _d68_rule("YES -- THE SUBSTANCE FROM THE SEAT", "M-D68-5",
               "O-MATTER is relocated to O-SEAT, the supply at the seat, in every variant "
               "combine screens; O-SEAT reads %s (O9) -- an obstruction until the seat's "
               "supply is shown, graded against S13, S10 and, on M-D68-7, S5 with its D25 "
               "gate" % _SEAT),
     "O9's O-SEAT reading; the notes on S5, S10, S13, D23 and D25"),
    ("M-D68-6",
     "Calibration of the origin (M-RULINGS-2026-10-03.md item 6): which ground-state "
     "quantities?",
     "M-D68-3 calibrated the graph's origin at ground-state values and left which ones open",
     _d68_rule("MASS/BINDING BY DEFAULT, PER QUESTION OTHERWISE", "M-D68-6",
               "the default calibration is %s (signed.CAL_DEFAULT); %s are selectable "
               "(signed.CALIBRATIONS), every use naming its calibration (signed.calibrate); "
               "POPULATE-AXES is %s (signed.CALIBRATIONS_OPEN: not implemented); an element "
               "is centred on one nuclide (H-NUCLIDE-GROUND), the periodic table's isotope "
               "mean carried as PT-AVERAGE (H-PT-WEIGHT); no verdict moves on the choice"
               % (signed.CAL_DEFAULT, ", ".join(signed.CALIBRATIONS),
                  signed.CALIBRATIONS_OPEN["POPULATE-AXES"].split(":")[0])),
     "every signed use names its calibration"),
    ("M-D68-7",
     "Seat-route reading (M-RULINGS-2026-10-03.md item 7): does S5, reconstruction from "
     "destination stock with its D25 gate, count as the seat's supply (H-SEAT-S5), or is the "
     "supply restricted to S10 and S13 (H-SEAT-ROUTES)?",
     "combine.py computes O-SEAT under both readings",
     _d68_rule("S5 COUNTS: H-SEAT-S5", "M-D68-7",
               "H-SEAT-S5 adopted: O-SEAT reads %s; H-SEAT-ROUTES kept as the alternative on "
               "record (O-SEAT %s under it)" % (_SEAT, d68_verdict(D68_SEAT_ROUTES))),
     "O9's O-SEAT reading; D68 wave 2's S5 seat route"),
    ("M-D68-8",
     "Does Baez-Fritz-Leinster convex linearity bind The Method (M-RULINGS-2026-10-03.md "
     "item 8)?  If it does, only signed w survives",
     "signed.py separates the weightings conditionally, under H-BFL-BINDS",
     _d68_rule("KEEP BOTH", "M-D68-8",
               "both weightings stay carried; the conditional separation H-BFL-BINDS stays "
               "named and unruled"),
     "Q-1s keeps both weightings"),
    ("M-D68-9",
     "The paper session on the complex and negative entropy findings "
     "(M-RULINGS-2026-10-03.md item 9; brief: PAPER-BRIEF-Q1s.md): start it?",
     "M asked for such instructions if Q-1s proved useful (M-D68-C8)",
     _d68_rule("WAIT", "M-D68-9",
               "PAPER-BRIEF-Q1s.md stays in the tree (present: %s); no session is started"
               % d68_paper_brief_present()),
     "nothing until M starts the session -- and then a paper only if the prior-art search "
     "shows a theorem or proof not previously published, M's novelty gate (M-D68-11)"),
    ("M-D68-10",
     "Order of work after wave 1 (M-RULINGS-2026-10-03.md item 10): (1) seat D68 wave 1 into "
     "the ledger and index3; (2) D68 wave 2 -- the Weinberg-family limits read at source, "
     "vacuum entanglement as pair supply, the S5 seat route; (3) the D67 per-source comments; "
     "(4) DOCKET 66",
     "four items were open after wave 1 closed",
     _d68_rule("IN THAT ORDER", "M-D68-10",
               "(1) is the wave 1 seating -- O9, these rows, the notes on S5, S10, S13, D23 "
               "and D25, and index3.py's DOCKET 68 rows; (2) D68 wave 2 is RUN, verified both "
               "ways and seated (docstring section 7b: O9's support-1 windows on the READ "
               "limits, O-MAKE-DIST from vacuum.py and O-SEAT from seat.py, the D23, D25 and "
               "S5 notes, M-D68-15 and M-D68-16, index3.py's DOCKET 68 rows re-typed); (3) the "
               "D67 per-source comments are written and kept as drafts "
               "(docket67-raw/COMMENTS-INDEX.md present: %s; M's ruling on them, "
               "M-RULINGS-2026-10-03.md item 17, is not seated on this board); (4) DOCKET 66 "
               "wave 1 is RUN, verified both ways, fixed and seated (docstring section 8: O9's "
               "DOCKET 66 part, the S5 and S13 notes, M-S1A-P3's and M-D65-1's cells, the "
               "TURN question for M in O9's answer; no index3.py row).  SEATED AT D68 WAVE 2 (kept): (3) and (4) "
               "are NOT YET RUN.  FIRST APPLIED (wave 1, kept): (2), (3) and (4) are NOT YET "
               "RUN" % d67_comments_present()),
     "nothing further in this order -- all four have run; the charter's order names Step 1b "
     "next (M-D68-C1).  The wave-2 seat said: the D67 per-source comments next; then DOCKET "
     "66 (wave 1 first said: D68 wave 2 next; then the D67 per-source comments; then DOCKET "
     "66)"),
    ("M-D68-11",
     "The paper's priority (M-RULINGS-2026-10-03.md item 11, 2026-10-04, as the file heads it; "
     "it records M's words and no question put): the standing of the Q-1s paper of M-D68-9 "
     "(PAPER-BRIEF-Q1s.md)",
     "M-D68-9 had the session wait; the brief made the prior-art search its first task",
     _d68_rule("THE PAPER IS CONDITIONAL ON NOVELTY", "M-D68-11",
               "the paper is written only if the prior-art search shows a theorem or proof not "
               "previously published; PAPER-BRIEF-Q1s.md carries M's condition verbatim "
               "(asked: %s) and makes that search, its section 3 step 1, the gate -- if every "
               "item is already published the session reports to M and writes no paper.  No "
               "session is started (M-D68-9); no novelty is claimed here" % d68_brief_has_gate()),
     "the Q-1s paper session, when M starts it: prior-art search first, paper only on novelty"),
    # ADDED: items 12 and 13, M's rulings on the paper (2026-10-04).  What was
    # applied is the paper's marked line, READ back by paper_d68_marker()
    # from M's words in its head -- never typed here.
    ("M-D68-12",
     "Paper, CLAIMS.md 4647-4648 (M-RULINGS-2026-10-03.md item 12, 2026-10-04, as the file "
     "records it): \"%s\"" % D68_PAPER_QUESTIONS["M-D68-12"],
     "M-D68-7 adopted H-SEAT-S5: O-SEAT is OPEN via S5, reconstruction from stock at the seat, "
     "so a sentence requiring an identical, travelled stock said more than the board holds",
     _d68_rule("CORRECT IT", "M-D68-12",
               "the paper's marked line, READ back: paper/CLAIMS.md:%s carries %s -- an "
               "identical, travelled stock is one route; reconstruction from local stock (S5) "
               "is another, open and not shown.  No board status moves" % paper_d68_marker(
                   D68_M_WORDS["M-D68-12"][0])),
     "the paper's S5 sentence; nothing on this board"),
    ("M-D68-13",
     "Paper, H62d (M-RULINGS-2026-10-03.md item 13, 2026-10-04, as the file records it): "
     "\"%s\"" % D68_PAPER_QUESTIONS["M-D68-13"],
     "DOCKET 68 computed routes outside linear quantum mechanics that would remove the two "
     "classical bits only on premises not shown (O9's member routes: W2 x F1, and clause 2b's "
     "D-CTC), none shown to exist; the paper's no-communication statements were unscoped",
     _d68_rule("SCOPE IT", "M-D68-13",
               "the paper's marked line, READ back: paper/CLAIMS.md:%s carries %s -- the "
               "statements scoped to linear quantum mechanics; O9's verdicts do not move"
               % paper_d68_marker(D68_M_WORDS["M-D68-13"][0])),
     "the paper's H62d scope; nothing on this board"),
    # ADDED (DOCKET 68 wave 2): items 15 and 16, M's rulings on the retrieval
    # route.  Item 15 is SUPERSEDED by item 16 and kept as history, as the
    # rulings file keeps it; what 16 applied is ASKED of the owners' recorded
    # routes (d68_w2_routes), never typed.
    ("M-D68-15",
     "Retrieval route for wave 2 (M-RULINGS-2026-10-03.md item 15, 2026-10-04, as the file "
     "heads it): which instruments obtain outside art; asked which, M chose the option "
     "'Corpus instruments'",
     "wave 2 had to read the Weinberg-family limits at source, which the board held only as "
     "NAMED-NOT-READ",
     _d68_rule("CORPUS INSTRUMENTS -- SUPERSEDED BY M-D68-16", "M-D68-15",
               "first read as the repository's own tools (tools/coverage.py, tools/recover.py, "
               "the sharded chat export drive/chats with its INDEX.tsv, the Drive mirror's "
               "MANIFEST.tsv, extracted/LEDGER.tsv and recovered/LEDGER.tsv), to find whether "
               "outside papers or their numbers were already in the corpus, with no paywall or "
               "host block circumvented.  SUPERSEDED the same day by item 16, M's correction "
               "(M-D68-16); kept as history, as the rulings file keeps it"),
     "nothing now: superseded by M-D68-16"),
    ("M-D68-16",
     "Correction to item 15 (M-RULINGS-2026-10-03.md item 16, 2026-10-04, as the file heads "
     "it): which instruments M meant for outside art",
     "M-D68-15 had been read as the corpus instruments only",
     _d68_rule("WEB-RETRIEVAL INSTRUMENTS, OPEN CONTENT ONLY", "M-D68-16",
               "item 15's reading is superseded: the instruments are the session's "
               "web-retrieval connectors, Firecrawl beside alphaXiv, used for openly available "
               "content only (public abstract pages, open-access copies, indexed full text), "
               "never a paywalled full text or a login wall circumvented, the route recorded "
               "with each reading.  Wave 2's recorded routes, asked of the owners: %s.  A full "
               "text behind a login wall was not read and stays a named hypothesis (H-MAP); an "
               "erratum page with no abstract stays NAMED-NOT-READ (H-ERRATUM)" % d68_w2_routes()),
     "every wave-2 reading of outside art that an owner records with a route (settle, "
     "vacuum, seat -- W2-fix's own reads included since the W2 reproduction), each with "
     "its route; H-MAP and H-ERRATUM stay named.  The wave-2 seat first said 'every "
     "wave-2 reading of outside art, each with its route' while its census left W2-fix's "
     "own reads out"),
    ("M-D68-C1",
     "When does DOCKET 68 open? (CHARTER.md: chartered 2026-10-02)",
     "DOCKET 67 was running when the docket was chartered",
     _d68_rule("AFTER DOCKET 67", "M-D68-C1",
               "DOCKET 67's close record is in the tree (docket67-raw/CLOSE.md present, its "
               "head '%s': %s), and DOCKET 68 ran after it; M-D67-1 and M-D67-2 are on this "
               "board (%s), which shows only that DOCKET 67's rulings are seated, not by itself "
               "that it closed.  CHARTER.md's own header still reads 'CHARTER, NOT YET "
               "OPENED', as first written and not updated.  The order D67, D68, D66, Step 1b, "
               "Step 1c is the charter's"
               % (d67_close_head(), d67_close_present(),
                  all(any(r[0] == k for r in RULED_BY_M) for k in ("M-D67-1", "M-D67-2")))),
     "DOCKET 68"),
    ("M-D68-C2",
     "Which is the '12 vertex trajectory model' M named in replying to %s? (CHARTER.md, "
     "M's answers to the follow-up questions, 2026-10-02)" % d68_route("M-D68-C2"),
     "M named the model in replying to the three routes put to M",
     _d68_rule("THE 12-VECTOR", "M-D68-C2",
               "as CHARTER.md carries M's answer (the charter's words, not M's): the "
               "12-vector of multiverse_12_vector_taxonomy_v2.pdf.  Carried as the "
               "hypothesis H-12, its parameters as carriers (settle.H12: %d rows, asked; %s "
               "carry no READ bound of any kind, settle.H12_UNBOUNDED); load-bearing on the "
               "drift's window only (N_H12W)" % (len(settle.H12), ", ".join(settle.H12_UNBOUNDED))),
     "H-12 in every combination"),
    ("M-D68-C3",
     "M replied to %s; asked what 'quantum easing / quantum settling' is (CHARTER.md, "
     "M's answers to the follow-up questions, 2026-10-02)" % d68_route("M-D68-C3"),
     "the term appears nowhere in the tree, corpus or chat export (CHARTER.md, searched)",
     _d68_rule("DETERMINISTIC DRIFT", "M-D68-C3",
               "as CHARTER.md carries M's answer (the charter's words, not M's): the state's "
               "own value steers its evolution, smoothly and the same every time.  Carried as "
               "the hypothesis H-SETTLE in readings %s (asked).  Its W2 reading (convention C2, "
               "a named hypothesis, not M's words) alone gives O-BITS %s, and with H-FRAME "
               "clause 1 (W2 x F1) O-BITS %s -- one of the two member routes O9 shows, clause "
               "2b's D-CTC the other.  Its other readings remove nothing: W1 x F1 gives O-BITS "
               "%s and KR x F1 O-BITS %s; KR alone gives O-HOLD %s (an OPEN pathway, not a "
               "removal; all asked)"
               % (", ".join(combine.SUBREADINGS["H-SETTLE"]),
                  d68_asked("H-SETTLE alone (W2)", "O-BITS"), d68_asked("W2 x F1", "O-BITS"),
                  d68_asked("W1 x F1", "O-BITS"), d68_asked("KR x F1", "O-BITS"),
                  d68_asked("H-SETTLE-KR alone (KR)", "O-HOLD"))),
     "H-SETTLE in every combination"),
    ("M-D68-C5",
     "What does 'supplied by probability in the citation/seating' mean: (1) the probability "
     "of a cell in The Method's closed index, or (2) probability in the quantum sense? "
     "(CHARTER.md, the two readings put to M)",
     "M's reply on holding the corridor open named a probability supply",
     _d68_rule("CONSIDER BOTH", "M-D68-C5",
               "both carried as readings in every combination: %s (combine.READINGS)"
               % ", ".join(v.split(":")[0] for v in combine.READINGS.values())),
     "R-INDEX and R-QUANTUM in every combination"),
    ("M-D68-C8",
     "Negative probabilities strain Q-1: Shannon's term p log p is undefined at p < 0 "
     "(CHARTER.md, 2026-10-03).  Define it, and build it?",
     "Q-1 is defined on probability measures only",
     _d68_rule("DEFINE IT, PLOT IT, BUILD IT", "M-D68-C8",
               "and, when asked to build it, %s.  Q-1s is built (signed.py) and wired into "
               "Q-1 (measure.py); the triangulation is computed as an inverse Radon "
               "reconstruction with a control (Q1s-signed.md section 5); the paper "
               "instructions are written (PAPER-BRIEF-Q1s.md) and the session waits (M-D68-9); "
               "the paper itself is written only if the prior-art search shows a theorem or "
               "proof not previously published (M-D68-11, the novelty gate)"
               % d68_words("M-D68-C8b")),
     "Q-1s; the paper brief, gated on novelty (M-D68-11)"),
    # CONVERTED FROM PENDING (M-D68-P1): M answered before DOCKET 68 opened
    # and the answer was applied the same day; the row first read the
    # charter, which predates the answer.  M's words and the question are
    # held from M-RULINGS-2026-10-03.md item 14; the values are asked.
    ("M-D68-C12",
     "The question put to M (M-RULINGS-2026-10-03.md item 14; answered 2026-10-02, before "
     "DOCKET 68 opened): \"%s\"" % D68_C12_QUESTION,
     "emtension.py's ENTANGLED_BRIDGE_IS_TRAVERSABLE = False cited no source, and "
     "1306.0533v2 had been read at source that day; CHARTER.md, written before the answer, "
     "records the question as asked of M and unanswered",
     _d68_rule("RECORD IT", "M-D68-C12",
               "emtension.py carries ER_EPR_SOURCE = %s, ER_EPR_SOURCE_STATUS = %s, "
               "ER_EPR_NONTRAVERSABLE_IS_ASSUMED = %s, ER_EPR_FOOTNOTE_1 (the source's "
               "footnote 1, held whole: %s) and ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION = %s, "
               "each checked by emtension.py's own selftest; the flag itself, "
               "ENTANGLED_BRIDGE_IS_TRAVERSABLE = %s, is unchanged and no grade moves -- only "
               "its citation changed.  All asked of emtension.  FIRST RECORDED AS PENDING "
               "(M-D68-P1), stale when written, as it stood: %s || %s || proposed: %s || "
               "waiting on it: %s"
               % (tuple(_emtension_record()[k] for k in (
                   "ER_EPR_SOURCE", "ER_EPR_SOURCE_STATUS", "ER_EPR_NONTRAVERSABLE_IS_ASSUMED",
                   "ER_EPR_FOOTNOTE_1 whole", "ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION",
                   "ENTANGLED_BRIDGE_IS_TRAVERSABLE")) + D68_P1_AS_FIRST_RECORDED)),
     "emtension.py's citation; combine.py's board flag reads the same value, unchanged"),
    # ADDED (R-seat): M's DOCKET 66 rulings, items 26-28 of the rulings file,
    # each with M's words verbatim (D68_M_WORDS), the question as the file
    # records it (D66_RULING_QUESTIONS) and what was applied ASKED of the
    # owner -- item 26 the paper's marked line READ back from M's words in
    # its DOCKET 66 head, as M-D68-12 and M-D68-13 read theirs.
    ("M-D68-26",
     "Paper, CLAIMS.md 1630-1631, the Gott pair bound (M-RULINGS-2026-10-03.md item 26, one of "
     "M's DOCKET 66 rulings, 2026-10-04, as the file records it): \"%s\""
     % D66_RULING_QUESTIONS["M-D68-26"],
     "DOCKET 66's A1 READ the Planck 2013 bound at source (defects.SOURCES['PLANCK13'], %s; "
     "route: %s): G mu/c^2 < %s for Nambu-Goto strings and %s for Abelian-Higgs, where Gott's "
     "pair needs gamma > 1/sin(4 pi G mu) = %s and %s (defects.gott_gamma_needed, CFG94 "
     "eq.(32), asked); the paper printed a looser bound than the one read and a lower gamma"
     % (defects.SOURCES["PLANCK13"][0], defects.SOURCES["PLANCK13"][1],
        D66_GOTT["NG"][0], D66_GOTT["AH"][0], _d68_g2(D66_GOTT["NG"][1]),
        _d68_g2(D66_GOTT["AH"][1])),
     _d68_rule("CORRECT IT", "M-D68-26",
               "the paper's marked line, READ back: paper/CLAIMS.md:%s carries %s -- the "
               "line prints defects.py's figures, each looked for (%s), its first figures kept "
               "under the marker; the rulings file records it as \"%s\"  No board status moves"
               % (paper_d66_marker(D68_M_WORDS["M-D68-26"][0])
                  + ("; ".join("%s: %s" % fx for fx in d66_paper_gott_figures()),
                     D66_RULING_CARRIED["M-D68-26"]))),
     "the paper's Gott pair bound; nothing on this board"),
    ("M-D68-27",
     "spec.py's TURN (M-RULINGS-2026-10-03.md item 27, one of M's DOCKET 66 rulings, "
     "2026-10-04, as the file records it): \"%s\".  FIRST RECORDED AS A QUESTION FOR M, kept "
     "(O9's DOCKET 66 answer since D66 wave 1, as A1 put it): %s"
     % (D66_RULING_QUESTIONS["M-D68-27"], d66_turn_question()[0]),
     d66_turn_question()[1],
     _d68_rule("ANY CROSSING: H-TURN-CROSSING", "M-D68-27",
               "applied in docket66/defects.py (defects.TURN_RULING, asked: adopted %s, %s kept "
               "as the alternative on record; the two readings' definitions unchanged).  The "
               "straight string TURNs: two rays at b = R_sun on opposite sides of a string at "
               "the Planck Nambu-Goto bound cross at L = b/tan(4 pi G mu) = %.0f AU "
               "(defects.string_turn, asked; under %s the string has %s -- no conjugate point); "
               "the global and gauge monopoles TURN under either reading, as before.  spec.py "
               "carries the ruling as a note in its PART 2 (READ: %s), no constant or check "
               "changed.  No specthm class verdict moves: its seat classes are defined by the "
               "literals %s only (READ from specthm.py's source), none naming a turn, so a "
               "string seat stays a candidate of the class it was, now with a TURN at a "
               "computed range; specthm.py is not edited.  The rulings file records: \"%s\"  "
               "No board status moves"
               % (D66_TURN["ruling"]["adopted"], D66_TURN["ruling"]["alternative on record"],
                  D66_TURN["L AU"], D66_TURN["ruling"]["alternative on record"],
                  D66_TURN["string"][D66_TURN["ruling"]["alternative on record"]][0],
                  spec_turn_note(),
                  ", ".join(sorted(set(x for v in specthm_seat_class_literals().values()
                                       for x in v))),
                  D66_RULING_CARRIED["M-D68-27"])),
     "A1's string grade (a TURN at a computed range); nothing on this board.  FIRST SAID, as "
     "the question stood: %s" % d66_turn_question()[3]),
    ("M-D68-28",
     "Re-grading D68 on the singular-throat ruling (M-RULINGS-2026-10-03.md item 28, one of "
     "M's DOCKET 66 rulings, 2026-10-04, as the file records it): \"%s\""
     % D66_RULING_QUESTIONS["M-D68-28"],
     "DOCKET 66's combine66 applied M-S1A-P3 to every D66 geometric throat; read as a board "
     "ruling (its reading singok-board) it moved D68's O-MAKE-TOPO LEFT -> OPEN via N_WNCC in "
     "%s variants, %s of them context-only (B-combine66.md, READ: combine's history encoding "
     "d68w2-topo now moves back exactly those) -- the contexts D68's own census names as %s "
     "(B-combine.md, READ); combine66 could not change D68's rows (its conservative-extension "
     "rule), so the board printed both"
     % (D66_TOPO_READ["d68w2-topo"][0], D66_TOPO_READ["d68w2-topo"][1],
        D68_TOPO_CENSUS["contexts"][2]),
     _d68_rule("RE-GRADE D68", "M-D68-28",
               "applied in docket68/combine.py (R-apply): DEF-TOPO gains THROAT & N_WNCC, "
               "N_WNCC an OPEN pathway never assumed in a removal (in combine.OPEN_NAMED: %s).  "
               "Asked of combine.Screen: O-MAKE-TOPO on the board alone %s; with RQ %s; under "
               "ITJ %s; ITB with RQ %s; under ITB %s -- never removed.  The census over every "
               "consistent variant is combine's own run (B-combine.md section 0, READ): %s of %s "
               "at 1 ly and %s of %s at 1 AU move LEFT -> OPEN via N_WNCC, and N_WNCC joins the "
               "removal's via list in the %s / %s NOT-BOUND-IF rows; of combine66's 32 "
               "contexts the same %s move (%s); drift %s of %s agree.  combine66's singok-board "
               "now moves %s rows (B-combine66.md, READ) and agrees with combine.py on the board "
               "alone (%s) and with RQ (%s), asked.  "
               "HISTORY KEPT: D68 wave 2's encoding is combine's history mutation d68w2-topo, "
               "asked: the board alone %s, RQ %s, ITJ %s (wave 2 printed ITJ's as LEFT, "
               "Geroch binding).  "
               "The rulings file records: \"%s\"  No headline, clash, support, account or "
               "survivor moves"
               % ("N_WNCC" in combine.OPEN_NAMED,
                  d68_asked("the board alone", "O-MAKE-TOPO"),
                  d68_asked("R-QUANTUM alone (RQ)", "O-MAKE-TOPO"),
                  d68_asked("H-IT as Jacobson emergent gravity (ITJ)", "O-MAKE-TOPO"),
                  d68_asked("ITB with R-QUANTUM (ITB+RQ)", "O-MAKE-TOPO"),
                  d68_asked("H-IT as an information layer (ITB)", "O-MAKE-TOPO"),
                  D68_TOPO_CENSUS["moved"][0], D68_TOPO_CENSUS["moved"][1],
                  D68_TOPO_CENSUS["moved"][2], D68_TOPO_CENSUS["moved"][3],
                  D68_TOPO_CENSUS["moved"][4], D68_TOPO_CENSUS["moved"][5],
                  D68_TOPO_CENSUS["contexts"][0], D68_TOPO_CENSUS["contexts"][2],
                  D68_TOPO_CENSUS["drift"][0], D68_TOPO_CENSUS["drift"][1],
                  D66_TOPO_READ["singok-board"][0],
                  d66_asked("singok-board on the board alone", "O-MAKE-TOPO", reading=True),
                  d66_asked("singok-board with RQ", "O-MAKE-TOPO", reading=True),
                  d68_verdict(D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]),
                  d68_verdict(D68_TOPO_W2_ASKED["R-QUANTUM alone (RQ)"]["per"]["O-MAKE-TOPO"]),
                  d68_verdict(D68_TOPO_W2_ASKED["H-IT as Jacobson emergent gravity (ITJ)"]
                              ["per"]["O-MAKE-TOPO"]),
                  D66_RULING_CARRIED["M-D68-28"])),
     "O9's O-MAKE-TOPO in D68's variants: what would answer it is N_WNCC, specthm's throat-"
     "creation class W-create-ncc shown nonempty (combine.OPEN_NAMED); nothing else on this "
     "board"),
    # ----- ADDED (W3S1B-seat, docstring section 8c): M's answers to questions
    # put on the corridor (items 22, 24; 2026-10-04) and on Step 1b (items 29,
    # 30, 33, 34; 2026-10-05).  Every figure ASKED of its owner
    # (W3S1B_ASKED); the questions are the file's, paraphrased as put, never
    # quoted.  No board status moves.
    ("M-D68-22",
     "The corridor on the board (M-RULINGS-2026-10-03.md item 22, 2026-10-04, as the file "
     "records it): when the work opens, carry the corridor as the A-B coupling -- a "
     "two-position system |A>, |B> rotated by a coupling term?",
     "M-D68-21 (carried below) says the object is at the beginning or the end, never in "
     "between; the file recorded the answer and built nothing until wave 3 (M-D68-34)",
     _d68_rule("CARRY THE CORRIDOR AS THE A-B COUPLING", "M-D68-22",
               "docket68/wave3/corridor.py, H = J(|A><B| + |B><A|), Christandl et al.'s N = 2 "
               "chain (quant-ph/0309131v2, READ).  Asked: the mid-transfer state's mode "
               "concurrence %s (under H-MODE-ENTANGLEMENT, a contested reading of one "
               "excitation); on/off keying through the coupling moves the far side's "
               "statistics by %s -- a coupling is a channel; never-in-between holds for two "
               "sites only (H-DIRECT-COUPLING, STRUCTURAL in the owner): on relayed engineered "
               "chains the object is found strictly between A and B at half the transfer time "
               "with probability %s at N = 3, %s at N = 4, %s at N = 8 and %s at N = 16.  It "
               "beats light across L = %s m iff hbar J > %s eV per qubit in parallel (serially "
               "%s to %s keV over the four counts).  The owner's grade is PROPOSED, NOT "
               "screened by combine.py (not edited): O-BITS REMOVED-IF one of H-DIRECT-COUPLING, "
               "H-LONG-RANGE (alpha < d) or unbounded J, with J > pi c/2L and H-STATE-AS-BITS, "
               "each speed-free route clashing with H-LOCALITY.  O9 does not move"
               % (_g(W3S1B_ASKED["conc"], 4), _g(W3S1B_ASKED["sig"], 3),
                  _g(W3S1B_ASKED["interior"]["engineered N=3"], 2),
                  _g(W3S1B_ASKED["interior"]["engineered N=4"], 2),
                  _g(W3S1B_ASKED["interior"]["engineered N=8"], 2),
                  _g(W3S1B_ASKED["interior"]["engineered N=16"], 4),
                  _g(W3S1B_ASKED["bl"]["L_m"], 4), _g(W3S1B_ASKED["bl"]["hbarJ_min_eV_per_qubit"], 2),
                  _g(min(W3S1B_ASKED["bl"]["serial_hbarJ_min_eV"].values()) / 1e3, 2),
                  _g(max(W3S1B_ASKED["bl"]["serial_hbarJ_min_eV"].values()) / 1e3, 3))),
     "wave 3's W3A and its proposed O-BITS grade, for combine.py if M rules it screened; "
     "nothing on this board moves"),
    ("M-D68-24",
     "What entanglement at 12 criteria means (M-RULINGS-2026-10-03.md item 24, 2026-10-04, as "
     "the file records it): are the twelve matched as shared values, or literally "
     "quantum-correlated between the two positions?  M added: \"%s\""
     % D68_CARRIED_WORDS["M-D68-24b"][0],
     "M-D68-23 (carried below) names the twelve as settle.H12 holds them; the file carries "
     "the answer as the hypothesis H-12Q",
     _d68_rule("LITERALLY QUANTUM-CORRELATED: H-12Q", "M-D68-24",
               "carried as H-12Q, a hypothesis and never a result, in docket68/wave3/"
               "criteria12.py.  Three cases asked: definite values at both seats carry %s bits "
               "of mutual information; a shared but uncertain value %s bit and no entanglement "
               "(the reading M set aside); a Bell pair quantum mutual information %s and "
               "entanglement %s -- so H-12Q needs criteria that are quantum observables.  Of "
               "settle.H12's twelve, %s are marked field carriers and %s conditional; settle's "
               "H-12-CARRIER (a constant whose value depends on the state) has no READ bound for "
               "%s and is NOT excluded.  Compatibility is reconstructibility from the seat's "
               "stock, not habitability (M's added sentence): with H-12-CARRIER false and four "
               "named hypotheses the predetermination reduces to the stock gate, %s kg of CI "
               "stock, binder %s, OPEN at Proxima (P unmeasured there); with it true the branch "
               "is OPEN"
               % (_g(W3S1B_ASKED["dvb"]["definite_classical_MI"]),
                  _g(W3S1B_ASKED["dvb"]["shared_classical_MI"]),
                  _g(W3S1B_ASKED["dvb"]["bell_QMI_ent"][0]), _g(W3S1B_ASKED["dvb"]["bell_QMI_ent"][1]),
                  ", ".join(W3S1B_ASKED["carrier"]["field_carriers_yes"]),
                  ", ".join(W3S1B_ASKED["carrier"]["conditional"]),
                  ", ".join(W3S1B_ASKED["carrier"]["unbounded"]),
                  "%.1f" % W3S1B_ASKED["pred"]["ci_stock_needed_kg"],
                  max(W3S1B_ASKED["pred"]["ci_stock_by_element_kg"].items(),
                      key=lambda kv: kv[1])[0])),
     "wave 3's W3B; H-12-CARRIER for alpha_s, G and v, OPEN; the stock gate at Proxima, OPEN"),
    ("M-D68-29",
     "The balanced equation (M-RULINGS-2026-10-03.md item 29, 2026-10-05, as the file records "
     "it): which two sides does Step 1b's balanced equation set against each other -- demand "
     "against supply, theory against measurement, both nested, or the corridor first?",
     "Step 1b's first pass needed its two sides; M answered in M's own words, not an option",
     _d68_rule("THE DEFINITION OF STEP 1b", "M-D68-29",
               "step1b/balance.py sets I(A, before) = I(B, after) and makes every matter and "
               "energy term an input or an output row.  Asked of balance.equation on R-QUANTUM: "
               "%d rows, none unaccounted (balance.unaccounted: %s); OPEN rows %s; the energy total "
               "refused (balance.energy_total: %s).  "
               "The accounting is a bookkeeping of declared links, NOT a balance of quantities "
               "(STRUCTURAL in the owner).  The value balances on the teleportation reading: "
               "B's fidelity with the two bits is 1 to within %s over %d random states, and with them "
               "withheld %s, a blind guess's -- B then holds no information about the state"
               % (len(W3S1B_ASKED["eq_ids"]), W3S1B_ASKED["eq_unaccounted"],
                  ", ".join(W3S1B_ASKED["eq_open"]), W3S1B_ASKED["eq_energy_total"],
                  _g(1.0 - W3S1B_ASKED["qvb"]["fid_min_with_bits"], 2), W3S1B_ASKED["qvb"]["trials"],
                  _g(W3S1B_ASKED["qvb"]["fid_mean_bits_withheld"]))),
     "Step 1b's equation; M-D68-30 fixes what the value is"),
    ("M-D68-30",
     "What the value of the object is (M-RULINGS-2026-10-03.md item 30, 2026-10-05, as the file "
     "records it): the 12-vector and the conserved quantities; the conserved quantities with "
     "Q-1 / Q-1s; the 12 trajectories; or information only?",
     "M-D68-29 left open which quantities make up the value that must be equal at the two "
     "positions",
     _d68_rule("INFORMATION ONLY", "M-D68-30",
               "the equated value is the object's definable condition information; matter and "
               "energy sit in the input and output rows.  The conserved quantities close site by "
               "site with zero transfer from A to B (balance.conserved_closure, asked: A to B "
               "%s for each of %s; STRUCTURAL in the owner); at B the closure is D25's stock "
               "gate, %s kg of CI feedstock, binder %s, measured in the Proxima system: %s"
               % (sorted(set(r["A_to_B"] for r in W3S1B_ASKED["closure"].values())),
                  ", ".join(W3S1B_ASKED["closure"]),
                  "%.1f" % W3S1B_ASKED["stock"]["ci_feedstock_kg"], W3S1B_ASKED["stock"]["ci_binder"][0],
                  W3S1B_ASKED["stock"]["P_measured_in_proxima_system"])),
     "Step 1b's value column (information) and its matter and energy columns"),
    ("M-D68-33",
     "Which of the board's four counts -- species sequence, 1 A grid, 0.1 A grid, thermal "
     "entropy -- is the object's definable condition information (M-RULINGS-2026-10-03.md "
     "item 33, 2026-10-05, as the file records it)?",
     "M-D68-30 fixed the value as information; the board holds four counts of it",
     _d68_rule("KEEP ALL FOUR", "M-D68-33",
               "H-WHICH-COUNT stays OPEN and every Step 1b and wave-3 figure is printed for each "
               "count (balance.counts, asked): %s"
               % "; ".join("%s %s bits" % (n, _g(v, 4)) for n, v in W3S1B_ASKED["counts"])),
     "every Step 1b and wave-3 table, four columns"),
    ("M-D68-34",
     "What next after Step 1b's first pass -- close 1b and go to 1c, more on 1b, or the "
     "corridor (M-RULINGS-2026-10-03.md item 34, 2026-10-05, as the file records it)?",
     "Step 1b's first pass stood with its OPEN list (step1b/BALANCE.md)",
     _d68_rule("THE CORRIDOR, D68 WAVE 3", "M-D68-34",
               "wave 3 opened on the corridor as the A-B coupling, the twelve criteria, H-12Q and "
               "H-SEATRANK (items 22-25): docket68/wave3/ corridor.py, criteria12.py, "
               "seatrank.py and aperture.py (M's question, M-D68-35), WAVE3.md.  Step 1b went "
               "on by necessity to its open terms, B's supply and placement (openterms.py, "
               "bsupply.py, placement.py, compensate.py on M-D68-31).  Both were verified "
               "adversarially in both directions and corrected, and both are seated here "
               "(docstring section 8c) -- %d owners loaded, all asked.  Step 1c is not begun"
               % (len(W3S1B))),
     "wave 3 and Step 1b, seated; Step 1c next"),
    ("M-D68-36",
     "Seating wave 3 and Step 1b, both verified and corrected (M-RULINGS-2026-10-03.md item "
     "36, 2026-10-05, as the file records it): seat both, wave 3 only, Step 1b only, or not "
     "yet?",
     "wave 3 and Step 1b had run, been verified both ways and corrected, and were not seated",
     _d68_rule("SEAT BOTH", "M-D68-36",
               "this seating (docstring section 8c): M's words for items 21-25 and 29-36 held in "
               "D68_M_WORDS and D68_CARRIED_WORDS and checked against the rulings file; items "
               "22, 24, 29, 30, 33, 34 and 36 on RULED_BY_M; items 21, 23, 25, 31, 32 and 35 in "
               "D68_FILE_CARRIED, not rulings; %d OPEN items named (W3S1B_OPEN); every figure "
               "asked of the %d owners (W3S1B_ASKED).  No board status moves, no index3 row is "
               "added (H-NO-W3S1B-ROW), and paper/CLAIMS.md is not edited"
               % (len(W3S1B_OPEN), len(W3S1B))),
     "the board's record of wave 3 and Step 1b; Step 1c next"),
    # ----- ADDED (S1C-seat, docstring section 8d): M's answers on Step 1c,
    # items 37-39 (2026-10-05).  Every figure ASKED of step1c's owners
    # (S1C_ASKED).  No board status moves.
    ("M-D68-37",
     "Step 1c, the supply side (M-RULINGS-2026-10-03.md item 37, 2026-10-05, as the file records it): which device "
     "subsystem's present-day supply to read at source first -- all three, assembly at B first, reading at A first, "
     "or the channel first?",
     "step1c/demand.py had priced each subsystem's demand from the balanced equation; no supply was read",
     _d68_rule("ALL THREE", "M-D68-37",
               "step1c/supply.py, every supply figure READ at source with its route (open content only; paywalls and "
               "a reCAPTCHA reported, not routed around).  Asked, at a 1 yr transfer, for one instrument: reading at "
               "A falls short by %s (atom probe tomography, %s atoms read per s, which removes 60%% of atoms unread); "
               "assembly at B by %s (optical tweezers, %s atoms per s at most, into vacuum, not a bonded solid); the "
               "channel by %s (DSOC's farthest measured rate carried to L under 1/d^2 at fixed hardware, %s bits per "
               "s -- the measured pair departs from 1/d^2 by %sx near and holds to %sx far).  Linear closure of the "
               "channel is excluded: received power must rise by at least %s (seat.channel_floor, any carrier).  "
               "The gaps are on different quantities and are not ranked or added"
               % (_g(S1C_ASKED["gap_1yr"]["READ-A"], 2), _g(S1C_ASKED["best"]["READ-A atoms/s"]),
                  _g(S1C_ASKED["gap_1yr"]["ASSEMBLE-B"], 2), _g(S1C_ASKED["best"]["ASSEMBLE-B atoms/s"]),
                  _g(S1C_ASKED["gap_1yr"]["CHANNEL"], 2), _g(S1C_ASKED["best"]["CHANNEL bits/s at Proxima"], 2),
                  "%.2f" % S1C_ASKED["dsoc_law"], "%.2f" % S1C_ASKED["dsoc_long"],
                  _g(S1C_ASKED["link_power_rise_1yr"], 2))),
     "Step 1c's supply side; the OPEN items S1C-O1..O3, O8"),
    ("M-D68-38",
     "Step 1c after its verification (M-RULINGS-2026-10-03.md item 38, 2026-10-05, as the file records it): seat Step "
     "1c, pursue one gap further, take the coupling route, or not yet?",
     "Step 1c's demand and supply were verified both ways and corrected",
     _d68_rule("THE COUPLING ROUTE", "M-D68-38",
               "step1c/coupling.py prices the wave-3 coupling as the device's link.  Locality bounds TIME, not J: an "
               "instantaneous coupling at the century J already gives B %s by L/c, so H-LOCALITY excludes it at every "
               "J; a retarded coupling completes at L/c or later and is photon exchange, the channel.  The direct "
               "couplings measured are near-field 1/R^3, valid only below lambda/2pi -- %s m (Rydberg, 9.131 GHz) and "
               "%s m (Kotler's ions) -- beyond which the retarded far-field term at L is %s rad/s, %s short of the "
               "century demand per pair; a near-field coupling at L would need a dipole of charge e separated by %s L.  "
               "corridor.before_light's threshold is where an instantaneous coupling would complete before light, "
               "not a ceiling on J (FIRST SAID as a ceiling, withdrawn on verification)"
               % (_g(S1C_ASKED["inst_signal_century"], 2), _g(S1C_ASKED["near_field_m"][0], 2),
                  _g(S1C_ASKED["near_field_m"][1], 2), _g(S1C_ASKED["J_far"], 2),
                  _g(S1C_ASKED["J_century"] / S1C_ASKED["J_far"], 2), "%.1f" % S1C_ASKED["dipole_over_L"])),
     "the coupling route, priced; wave 3's proposed O-BITS grade unchanged (its J > pi c/2L is the before-light "
     "condition of the instantaneous coupling that grade names)"),
    ("M-D68-39",
     "Order after the coupling route (M-RULINGS-2026-10-03.md item 39, 2026-10-05, as the file records it): 1 seat "
     "Step 1c, 2 price coherence, 3 revisit H-LOCALITY, or 4 not yet?",
     "the coupling route was priced and verified; H-COHERENCE was named and priced nowhere",
     _d68_rule("H-LOCALITY, THEN COHERENCE, THEN SEAT STEP 1c", "M-D68-39",
               "(3) step1c/nonlocal.py carries H-NONLOCAL-COUPLING as M's hypothesis, never dismissed: loops close iff "
               "no common simultaneity frame (latticectc, asked: witnesses %s, spacelike-span pair %s), so it needs "
               "H-FRAME; present spacelike no-signalling checks (READ) allow J up to %s rad/s (%s) -- %s x the day "
               "demand (reading C: %s x) -- so they do not exclude it under H-J-DISTANCE-FREE, H-SETTING-DEPENDENCE "
               "and H-UNIVERSAL-COUPLING; if J falls as r^-alpha they do for alpha > %s (day) / %s (century).  "
               "(2) step1c/coherence.py: Bob's stored hold is 2x/c -- %s s at the midpoint, 0 with the source at "
               "Alice or for a bit payload; at the midpoint the best measured T2 (%s s) falls short by %s at overhead "
               "2 and %s at 1e27.  (1) this seating (docstring section 8d)"
               % (S1C_ASKED["frame"]["witness_loop"], S1C_ASKED["frame"]["pair_loop"],
                  _g(S1C_ASKED["tightest"][1], 2), S1C_ASKED["tightest"][0],
                  _g(S1C_ASKED["tightest"][1] / S1C_ASKED["day_J"], 2),
                  _g(S1C_ASKED["tightest_C"] / S1C_ASKED["day_J"], 2),
                  "%.2f" % S1C_ASKED["falloff_alpha"]["1 day"], "%.2f" % S1C_ASKED["falloff_alpha"]["1 century"],
                  _g(S1C_ASKED["hold_by_source"]["x = L/2 (midpoint)"]), _g(S1C_ASKED["best_T2_s"]),
                  _g(S1C_ASKED["shortfall_by_overhead"][2.0], 2), _g(S1C_ASKED["shortfall_by_overhead"][1e27], 2))),
     "the non-local branch and coherence, priced; the OPEN items S1C-O4..O7"),
    # ----- ADDED (D68-close, docstring section 8e): M's answer after Step 1c,
    # item 40 (2026-10-05).  Every figure ASKED of wave 4's owners (W4_ASKED).
    ("M-D68-40",
     "After Step 1c (M-RULINGS-2026-10-03.md item 40, 2026-10-05, as the file records it): 1 close D68, then the Q-1s "
     "prior-art gate; 2 a D68 wave 4 first, pricing what Step 1c left OPEN; 3 close D68 only; or 4 pause?",
     "every item in the charter's order had run and been seated; Step 1c left S1C-O8 and H-FT-MEMORY OPEN",
     _d68_rule("WAVE 4, THEN THE CLOSE AND THE GATE", "M-D68-40",
               "(2) docket68/wave4/linkbudget.py: at the 1 yr floor quantum (%s keV) a single-mode link needs equal "
               "apertures of %s m; figure-limited with the optics READ at source (no mirror optic reaches that "
               "quantum) the transmitted power is %s to %s solar luminosities -- fragile: a beam under %s arcsec onto "
               "7 m^2 would need less, and no coherent source there is READ.  docket68/wave4/ftmemory.py: a "
               "fault-tolerant memory for a stored quantum payload on measured surface-code figures needs distance %s "
               "(%s at half the payload lost), %s physical qubits -- %s per atom of the object -- and %s J at one "
               "erasure per syndrome bit; with the burst floor measured on one device it fails (%s expected logical "
               "failures).  (1) docket68/CLOSE.md, READ (%d sections: %s); the Q-1s prior-art gate runs next and no "
               "paper is written before M sees it"
               % (_g(W4_ASKED["kT_keV"]), _g(W4_ASKED["single_mode_D_m"]), _g(W4_ASKED["fig_min_Lsun"], 2),
                  _g(W4_ASKED["fig_max_Lsun"], 2), _g(W4_ASKED["sun_width_arcsec"], 2), W4_ASKED["d"],
                  W4_ASKED["d_half"], _g(W4_ASKED["phys"], 2), _g(W4_ASKED["per_atom"], 2),
                  _g(W4_ASKED["landauer_J"], 2), _g(W4_ASKED["failures_at_floor"], 2),
                  len(d68_close_sections()), "; ".join(d68_close_sections()))),
     "DOCKET 68 closed; the Q-1s prior-art gate (M-D68-11, M-D68-C8b) next; the OPEN items W4-O1..O6"),
    # ----- ADDED (CMB-seat, docstring section 8f): M's answers after the close,
    # items 42, 43 and 45 (2026-10-05).  Reading 1's figures ASKED (CMB_ASKED).
    ("M-D68-42",
     "After M's question on the background radiation (item 41), with the Q-1s prior-art gate mid-search "
     "(M-RULINGS-2026-10-03.md item 42, 2026-10-05, as the file records it): 1 CMB as the frame first; 2 all four "
     "readings; 3 finish the gate first; or 4 carry only?",
     "M asked item 41 after DOCKET 68's close; the gate (M-D68-11's condition, M-D68-C8b) had not reported",
     _d68_rule("THE GATE FIRST, THEN THE CMB AS THE FRAME", "M-D68-42",
               "(3) docket68/Q1s-PRIORART.md, READ (%d sections: %s): not every item of the brief is published -- "
               "candidates survive in items 1 to 5, item 6 is published, and Im-Khovanov (2409.08462v2) narrows item "
               "2.  (1) docket68/cmb/cmbframe.py, the background's rest frame as H-FRAME's frame, seated with "
               "M-D68-45" % (len(q1s_gate_sections()), "; ".join(q1s_gate_sections()))),
     "the gate reported (M-D68-43); H-CMB-CORRIDOR reading 1 (M-D68-45)"),
    ("M-D68-43",
     "Shown the Q-1s prior-art gate (M-RULINGS-2026-10-03.md item 43, 2026-10-05, as the file records it): should a "
     "paper be written, and in what form -- not now, CMB next; a short mathematical note; a longer paper with D_s; "
     "or no paper?",
     "M-D68-11's condition: a paper only if the concept is novel; the gate found candidates in items 1 to 5",
     _d68_rule("NO PAPER", "M-D68-43",
               "no paper is written and no paper session starts; docket68/PAPER-BRIEF-Q1s.md is kept as a record "
               "(its section 7 closes it) and Q1s-PRIORART.md's grades stand (its section 6 records this ruling); "
               "signed.py and Q1s-signed.md are unchanged; paper/CLAIMS.md is not edited"),
     "the Q-1s paper question closed"),
    ("M-D68-45",
     "After H-CMB-CORRIDOR reading 1 was verified and corrected (M-RULINGS-2026-10-03.md item 45, 2026-10-05, as the "
     "file records it): seat it, then the background as medium; seat it only; medium and register first; or not "
     "yet?",
     "reading 1 (docket68/cmb/) stood, verified once in both directions",
     _d68_rule("SEAT READING 1, THEN THE BACKGROUND AS MEDIUM", "M-D68-45",
               "docket68/cmb/cmbframe.py, seated here (docstring section 8f): the CMB rest frame as H-FRAME's frame. "
               " The dipole READ at source (Planck 2018 I, 1807.06205v2); beta = amplitude / T0 = %s across two READ "
               "papers.  Proxima lies %s deg from the apex; a CMB-simultaneous link reaches it at barycentre "
               "coordinate time %s h (clause 2a: spacelike, no loop), moving by +- %s s over a year in Earth's "
               "momentary rest frame; the dipole-precision term alone is %s s.  With the frame named, H-LAB-FRAME "
               "holds for all %d of nonlocal.py's tests (%s): their J bounds apply to within a factor %s, the "
               "tightest %s rad/s.  The one CMB-frame speed bound printed (Scarani 2000) is %s c, a lower bound.  "
               "The matter dipole leaves two readings: intrinsic anisotropy (the CMB frame stands) or kinematic (the "
               "quasar frame shifts the Proxima lead by 0 to %s h, the Local Group's by %s h).  The background cools "
               "as 1/a (T(z) beta within %s sigma of 0 in every READ fit): equal temperature is equal cosmic time, but "
               "T0 is %s orders short of a one-second slicing and resolving the lead by temperature would need dT/T "
               "of %s; the dipole with light signals synchronises the ends.  The multi-spacetime clause stays OPEN"
               % (_g(CMB_ASKED["beta_amp"], 7), _cmb_fig(CMB_ASKED)["theta"], _cmb_fig(CMB_ASKED)["lead_h"],
                  "%.0f" % CMB_ASKED["annual_s"], _cmb_fig(CMB_ASKED)["sigma"], CMB_ASKED["n_tests"],
                  CMB_ASKED["lab_all"], "%.5f" % CMB_ASKED["J_factor_max"], _cmb_fig(CMB_ASKED)["J"],
                  _g(CMB_ASKED["scarani"], 2), _cmb_fig(CMB_ASKED)["qmax"], "%.1f" % CMB_ASKED["lg_shift_h"],
                  "%.2f" % CMB_ASKED["tz_max_sigma"], "%.1f" % CMB_ASKED["gap_orders"],
                  _g(CMB_ASKED["dTT_lead"], 2))),
     "H-CMB-CORRIDOR's medium reading next; the OPEN items CMB-O1..O4"),
    # ----- ADDED (CMB2-seat, docstring section 8g): M's answers on readings 2
    # and 3 and the local clocks, items 47, 49, 51, 53 and 54 (2026-10-05).
    # Their figures ASKED (CMB2_ASKED).
    ("M-D68-47",
     "Asked how to take up item 46 while the medium reading was in progress (M-RULINGS-2026-10-03.md item 47, "
     "2026-10-05, as the file records it): 1 fold into the medium reading; 2 READ the status first; 3 separate, after "
     "the medium reading; or 4 carry only?",
     "M asked item 46 (H-CONTRACT) during H-CMB-CORRIDOR reading 2",
     _d68_rule("READ THE STATUS, THEN FOLD INTO THE MEDIUM READING", "M-D68-47",
               "the status of future contraction READ at source first (docket68/cmb/MEDIUM.md), then "
               "docket68/cmb/medium.py's contraction(): frame.py's lemma needs only a(t) > 0 (z3: its negation "
               "%s), so a nonsingular bounce keeps H-FRAME's frame; in loop quantum cosmology the background peaks "
               "at %s of the Planck temperature and recouples at %s K on the way down; slow contraction reaches "
               "only %s K" % (CMB2_ASKED["lemma"], "%.3f" % CMB2_ASKED["lqc_ratio"], "%.0f" % CMB2_ASKED["T_dec"],
                              "%.0f" % CMB2_ASKED["slow_T"])),
     "H-CONTRACT carried (M-D68-46); the OPEN item CMB2-O1"),
    ("M-D68-49",
     "Asked how to take up item 48 (M-RULINGS-2026-10-03.md item 49, 2026-10-05, as the file records it): 1 READ, "
     "then a model; 2 READ only; 3 fold into the medium reading; or 4 carry only?",
     "M carried item 48 (H-UNOBSERVED-MEDIUM) on reading 2",
     _d68_rule("READ, THEN A MODEL; MATTER OBSERVES, A DIFFERENT TYPE", "M-D68-49",
               "the relational-time, quantum-cosmology and observation literature READ; docket68/cmb/unobserved.py, "
               "rebuilt against two verifications, gives the whole a history-state Hamiltonian whose medium starts "
               "in the coupled ground state, stationary while coupled: from it the traced history and M-SUPPORT "
               "differ by trace distance %s with decoupling (uniform ticks) and %s without; matter's records leave "
               "the medium's own state unchanged, every probability kept; H-TWO-OBSERVERS carried, and which type "
               "of observation decoupling needs is not assumed"
               % ("%.3f" % CMB2_ASKED["td_ground"][0], _g(CMB2_ASKED["td_control"], 2))),
     "H-UNOBSERVED-MEDIUM (M-D68-48); the OPEN items CMB2-O2, CMB2-O3, CMB2-O6"),
    ("M-D68-51",
     "Asked how to take up item 50 (M-RULINGS-2026-10-03.md item 51, 2026-10-05, as the file records it): 1 into the "
     "model and O9; 2 READ first; 3 both, READ, then model; or 4 carry only?",
     "M carried item 50 (H-CONSCIOUS-SELECTS)",
     _d68_rule("READ, THEN MODEL; MANY OBSERVERS", "M-D68-51",
               "the eraser, consciousness-collapse and relative-facts sources READ; in docket68/cmb/unobserved.py "
               "Born selection after records changes no later statistic, while selection before them moves an "
               "interference statistic by %s; two observers disagree by sin^2(theta/2) and agree again through a "
               "record (computed, %s); Earth and Proxima see skies differing by a %s mK dipole, the one rebuilt from "
               "the other by a Lorentz boost; under Born selection Bob's marginal spread is %s, no channel; "
               "H-MANY-PERSPECTIVES carried"
               % ("%.4f" % CMB2_ASKED["sel_diff"], "%.6f" % CMB2_ASKED["agree_link"], "%.3f" % CMB2_ASKED["sky_mK"],
                  _g(CMB2_ASKED["o9_a"], 2))),
     "H-CONSCIOUS-SELECTS (M-D68-50), O9; the OPEN item CMB2-O4"),
    ("M-D68-53",
     "Asked how to take up item 52 (M-RULINGS-2026-10-03.md item 53, 2026-10-05, as the file records it): READ, then "
     "model; model now; READ only; or carry only?",
     "M stated item 52 (H-LOCAL-CLOCK) as an answer to what introduces the clock",
     _d68_rule("READ, THEN MODEL", "M-D68-53",
               "the quantum-clock literature and Page's sensible quantum mechanics READ; docket68/cmb/localclock.py, "
               "verified once: Proxima b's orbital clock runs %s +- %s s per year slower than Earth's orbital clock, "
               "each against its own star (the law matches IAU L_C to %s); the CMB frame reckons Proxima's clock %s "
               "s per year slower than the Sun's and the Sun's frame adds %s s per year -- each frame lawful, none "
               "privileged; a qubit shared across both carries a fixed, calibratable phase, coherent uncalibrated "
               "only below %s Hz"
               % ("%.3f" % CMB2_ASKED["clock_s"], "%.3f" % CMB2_ASKED["clock_sigma"], _g(abs(CMB2_ASKED["lc_vs_iau"]), 2),
                  "%.3f" % CMB2_ASKED["cmb_frame_s"], "%.3f" % CMB2_ASKED["sun_frame_s"],
                  "%.1f" % CMB2_ASKED["f_1rad"])),
     "H-LOCAL-CLOCK (M-D68-52); the OPEN item CMB2-O5"),
    ("M-D68-54",
     "After localclock.py's verification and unobserved.py's third build (M-RULINGS-2026-10-03.md item 54, "
     "2026-10-05, as the file records it): 1 seat all three; 2 READ the RNG effect size and price reading (b) first; "
     "3 model M-SUPPORT's dynamics first; or 4 seat, then price?",
     "medium.py, unobserved.py and localclock.py stood verified, none seated",
     _d68_rule("M-SUPPORT'S DYNAMICS, THEN THE BIAS PRICED, THEN SEAT", "M-D68-54",
               "(3) docket68/cmb/support.py, verified once, NOT seated: on H-SUPPORT-IS-RECORDS the support grows at "
               "Gamma/H records per photon per e-fold, and its edge is where the coupling ends.  (2) "
               "docket68/cmb/bias.py, verified once, NOT seated: reading (b) priced at the READ bias sizes, none "
               "established.  (1) medium.py, unobserved.py and localclock.py seated here (docstring section 8g): "
               "the background is collisionless today (mean free path 10^%s Hubble lengths) and was a true medium "
               "before decoupling (sound at %s c); the observation model's decoupling distance is %s; the local "
               "clocks differ by %s s per year; the CMB frame reckons %s s per year"
               % (_cmb2_fig(CMB2_ASKED)["mfp"], _cmb2_fig(CMB2_ASKED)["cs"], _cmb2_fig(CMB2_ASKED)["td"],
                  _cmb2_fig(CMB2_ASKED)["clock"], _cmb2_fig(CMB2_ASKED)["cmbf"])),
     "the OPEN items CMB2-O1..O6; support.py and bias.py await M's ruling"),
    # ----- ADDED (CMB3-seat, docstring section 8h): item 55 (2026-10-05).
    ("M-D68-55",
     "After item 54's three steps (M-RULINGS-2026-10-03.md item 55, 2026-10-05, as the file records it): seat both "
     "support.py and bias.py; seat support.py only; model H-Z-PER-SESSION first; or hold both?",
     "support.py and bias.py stood verified once and corrected, not seated",
     _d68_rule("SEAT BOTH", "M-D68-55",
               "docket68/cmb/support.py and bias.py, seated here (docstring section 8h).  support.py: recombination "
               "and reionisation computed from READ sources put z* at %s (Planck 1089.92); on H-SUPPORT-IS-RECORDS "
               "the support grows at Gamma/H records per photon per e-fold, below the expansion rate from z %s, the "
               "last record peaking at z %s; %s of today's light was last recorded after reionisation; in the toy "
               "the record weighting matches M-SUPPORT to %s, but a record-free weighting does too (%s, inside the "
               "%s ambiguity) -- consistency, not proof -- while without recombination the records miss by %s; the "
               "Sachs-Wolfe rms offset of local decoupling is %s yr in the Newtonian frame.  bias.py: Bosch 2006 "
               "(secondary) gives eps %s (random effects, %s bits per pair) or %s (fixed effect, %s bits per pair); "
               "Maier 2018's Bayes factor recomputes to %s at their prior and %s at Bosch's size; under Born "
               "selection Bob's marginal spread is %s"
               % (_cmb3_fig(CMB3_ASKED)["z_star"], _cmb3_fig(CMB3_ASKED)["z_gH"], "%.0f" % CMB3_ASKED["z_peak"],
                  "%.4f" % CMB3_ASKED["reion_share"], _g(CMB3_ASKED["toy_rec"], 2), _g(CMB3_ASKED["toy_free"], 2),
                  _g(CMB3_ASKED["toy_amb"], 2), _cmb3_fig(CMB3_ASKED)["norec"], "%.1f" % CMB3_ASKED["sw_rms_yr"],
                  _g(CMB3_ASKED["eps_re"], 2), _cmb3_fig(CMB3_ASKED)["bits_re"], _g(CMB3_ASKED["eps_fe"], 2),
                  _g(CMB3_ASKED["bits_fe"], 2), _cmb3_fig(CMB3_ASKED)["bf"], "%.2f" % CMB3_ASKED["bf_point"],
                  _g(CMB3_ASKED["reading_a"], 2))),
     "the OPEN items CMB3-O1..O5; O9 stays OPEN"),
]

RULED_BY_M += D68_RULED

#: The charter's own words on M's flatness question (CHARTER.md), quoted in
#: M-D68-C10's cell -- the charter's, not M's; checked like M's words.
D68_CHARTER_STRIKE = "M is right to strike it"


def _d68_carry(kind, rid, carried):
    """A carried-item cell: what M's words are (a proposal, a statement, an
    instruction), M's words verbatim, and how the charter carries them --
    never 'RULED BY M'."""
    return "M'S %s, CARRIED BY THE CHARTER (not a ruling) -- %s.  CARRIED: %s" % (
        kind, d68_words(rid), carried)


#: WHAT THE CHARTER CARRIES FROM M WITHOUT A RULING: M's proposals,
#: statements and instructions, each carried as a named hypothesis or a
#: standing instruction (id, M's words in context, the carrying, what it
#: feeds).  NOT ON RULED_BY_M AND NOT COUNTED AS RULINGS.  MOVED (DOCKET 68
#: residuals): M-D68-C4, C6 and C7 were first seated on RULED_BY_M; C9-C11
#: ADDED so that H-IT, H-FRAME and H-INFO/Q-1 are carried as H-ZERO and
#: H-NULL are.  H-SETTLE and H-12 are carried through M-D68-C3 and M-D68-C2,
#: where M answered a question put; the readings R-INDEX and R-QUANTUM
#: through M-D68-C5.
D68_CARRIED = [
    ("M-D68-C4",
     "M's standing instruction for the docket (CHARTER.md, 2026-10-02); no question was put",
     _d68_carry("INSTRUCTION", "M-D68-C4",
                "TEST IN COMBINATION -- each hypothesis tested alone first, a failure alone "
                "retiring nothing; every combination in every reading screened (combine.py "
                "builds %s variants, asked); joint results tested by instrument"
                % format(D68_VARIANT_COUNT, ",")),
     "combine.py and O9"),
    ("M-D68-C6",
     "M's proposal (CHARTER.md, 2026-10-02); no question was put",
     _d68_carry("PROPOSAL", "M-D68-C6",
                "as H-ZERO, a hypothesis and not a result: moving the zero changes the NEC "
                "combination by exactly 0 (zero.py), so it relabels a WEC violation and not a "
                "throat's NEC violation; in the screen it is inert (in combine.INERT: %s)"
                % ("ZERO" in combine.INERT)),
     "H-ZERO in every combination"),
    ("M-D68-C7",
     "M on the null condition (CHARTER.md, 2026-10-02); no question was put",
     _d68_carry("STATEMENT", "M-D68-C7",
                "as H-NULL, a hypothesis and not a result: the QNEC prices a throat's null "
                "deficit in bits only outside its proven scope (nullinfo.py); in the screen it "
                "is inert (in combine.INERT: %s)" % ("NULL" in combine.INERT)),
     "H-NULL in every combination"),
    ("M-D68-C9",
     "M replied to %s (CHARTER.md, 2026-10-02)" % d68_route("M-D68-C9"),
     _d68_carry("INSTRUCTION TO ASSUME", "M-D68-C9",
                "as H-IT, a hypothesis and never a result: an instruction to assume a premise "
                "is not a finding that it holds.  Read three ways (%s, combine.SUBREADINGS, "
                "asked).  ITB: O-MAKE-TOPO %s; O-HOLD %s -- not removals.  ITE: O-MAKE-TOPO "
                "%s.  ITJ: O-HOLD %s.  With R-QUANTUM beside ITB (ITB+RQ): O-MAKE-TOPO %s, "
                "O-HOLD %s -- R-QUANTUM's throat undoes ITB's non-binding (B-combine.md "
                "section 5: ITB+RQ under N_QTOPO is a premise clash, ITB's no-geometric-throat "
                "premise against R-QUANTUM's throat).  All asked of combine.Screen"
                % (", ".join(combine.SUBREADINGS["H-IT"]),
                   d68_asked("H-IT as an information layer (ITB)", "O-MAKE-TOPO"),
                   d68_asked("H-IT as an information layer (ITB)", "O-HOLD"),
                   d68_asked("H-IT as ER=EPR (ITE)", "O-MAKE-TOPO"),
                   d68_asked("H-IT as Jacobson emergent gravity (ITJ)", "O-HOLD"),
                   d68_asked("ITB with R-QUANTUM (ITB+RQ)", "O-MAKE-TOPO"),
                   d68_asked("ITB with R-QUANTUM (ITB+RQ)", "O-HOLD"))),
     "H-IT in every combination; O9's NOT-BOUND-IF entries"),
    ("M-D68-C10",
     "M replied to %s (CHARTER.md, 2026-10-02).  Replying on the corridor to %s, %s"
     % (d68_route("M-D68-C10"), d68_route("M-D68-C10b"), d68_words("M-D68-C10b")),
     _d68_carry("STATEMENT", "M-D68-C10",
                "as H-FRAME, a hypothesis and not a result, in two clauses (combine's F1, F2b).  "
                "F1 alone: O-BITS %s, corridor O-LOOP %s -- an alternative member support "
                "beside the geometry's, not a removal of its own; with W2, O-BITS REMOVED-IF "
                "(M-D68-C3, O9).  F2b's D-CTC: O-BITS %s, O-LOOP reintroduced, no CTC shown.  "
                "M's question on flatness struck a hypothesis of corridors.py (latticectc's H1; "
                "the charter's words, not M's: \"%s\") and prompted the computation: in "
                "frw_frame.py and frame.py exact FRW admits only equal-cosmic-time corridors "
                "(frame.frw_time_function_lemma: the claim %s, its vacuity guard %s), so on "
                "the board alone corridor O-LOOP reads %s -- the removal credited to the "
                "geometry and to no hypothesis, M's question credited with prompting it "
                "(index3's D68-EXACT-FRW-ADMITS-ONLY-EQUAL-COSMIC-TIME-CORRIDORS).  All asked"
                % (d68_asked("H-FRAME clause 1 alone (F1)", "O-BITS"),
                   d68_asked("H-FRAME clause 1 alone (F1)", "O-LOOP-C"),
                   d68_asked("clause 2b's D-CTC (F2b)", "O-BITS"),
                   D68_CHARTER_STRIKE, frame.frw_time_function_lemma()["claim"],
                   frame.frw_time_function_lemma()["vacuity"],
                   d68_asked("the board alone", "O-LOOP-C"))),
     "H-FRAME in every combination; O9's member routes; the FRW corridor finding"),
    ("M-D68-C11",
     "M's premise and request (CHARTER.md, 2026-10-02); no question was put",
     _d68_carry("PREMISE AND REQUEST", "M-D68-C11",
                "the premise as H-INFO, a hypothesis and not a result (necessity, combine's "
                "INFO, inert in the screen: %s; measure.GRADES['H-INFO'] %s); the request as "
                "the work item Q-1, the substrate-free measure: delivered (measure.py, BFL "
                "Theorem 2 verified on finite spaces), log2 %d = %.6f bits per cell of Lambda, "
                "measure.GRADES['Q-1'] %s -- a measure counts and removes nothing, so it gets "
                "no row of its own and is carried on O9 with Q-1s (M-D68-C8).  What arrives is "
                "read as H-INFO-SHAPE on M's ruling (M-D68-1, M-D68-5); H-INFO-S stays the "
                "alternative reading.  All asked"
                % ("INFO" in combine.INERT, measure.GRADES["H-INFO"]["verdict"],
                   measure.method_bits()["cells"], measure.method_bits()["bits_per_cell"],
                   measure.GRADES["Q-1"]["verdict"])),
     "H-INFO in every combination; Q-1 and Q-1s on O9"),
]


def _d68_carry_file(kind, rid, carried):
    """A carried-item cell for M's words the RULINGS FILE carries without a
    ruling (docstring section 8c): what they are, M's words verbatim, and how
    the file and the owners carry them -- never 'RULED BY M'."""
    return "M'S %s, CARRIED BY THE RULINGS FILE (not a ruling) -- %s.  CARRIED: %s" % (
        kind, d68_words(rid), carried)


#: WHAT M-RULINGS-2026-10-03.md CARRIES FROM M WITHOUT A RULING (W3S1B-seat,
#: docstring section 8c): statements, an instruction, a hypothesis given in
#: answer to a question ("I suspect") and a question -- each carried as a named
#: hypothesis or answered by computation, with the wave-3 or Step 1b owner
#: that does it.  (id, M's words in context, the carrying, what it feeds).
#: NOT ON RULED_BY_M, NOT COUNTED AS RULINGS, and kept apart from D68_CARRIED
#: because the carrier is the rulings file, not the charter.
D68_FILE_CARRIED = [
    ("M-D68-21",
     "M on speed and position (M-RULINGS-2026-10-03.md item 21, 2026-10-04); no question was put",
     _d68_carry_file("STATEMENT", "M-D68-21",
                     "as the reading docket68/wave3/corridor.py tests (with M-D68-22's coupling).  "
                     "Never in between holds in the two-site model only, which is H-DIRECT-COUPLING "
                     "(by construction, STRUCTURAL in the owner); relayed, it fails -- found between "
                     "A and B at half the transfer time with probability up to %s (engineered, "
                     "N = 16) -- and distance returns: a uniform chain's arrival time is linear in "
                     "N, an engineered chain's bounded-coupling time doubles as N doubles, and the "
                     "short-range Lieb-Robinson bound holds (Nachtergaele and Sims "
                     "arXiv:1004.2086v1, READ).  No speed holds iff one of H-DIRECT-COUPLING, "
                     "H-LONG-RANGE with alpha < d (Eldredge et al. arXiv:1612.02442v2, READ; its "
                     "fn. 45 volume prefactor named) or unbounded J holds; each clashes with "
                     "H-LOCALITY at the fundamental level.  The mean position passes between A and "
                     "B even in the two-site model.  A hypothesis tested, not a result"
                     % _g(W3S1B_ASKED["interior"]["engineered N=16"], 4)),
     "wave 3's W3A; the speed-free set, OPEN (each route clashes with H-LOCALITY)"),
    ("M-D68-23",
     "M on the twelve trajectories (M-RULINGS-2026-10-03.md item 23, 2026-10-04); no question "
     "was put",
     _d68_carry_file("STATEMENT", "M-D68-23",
                     "as the twelve settle.H12 holds, by kind (criteria12.kinds, asked): emergent "
                     "%s; material %s; the other %d %s, not independent.  The only READ spatial "
                     "bound between Earth and Proxima b is alpha's coupling to the potential: under "
                     "H-LINEAR-PHI (about %s times the measured lever arm) |dalpha/alpha| <= %s at "
                     "the 1 sigma upper end, %s at 2 sigma; the other seven are equal under "
                     "H-UNIFORM-CONSTANTS, with no READ bound.  The predetermination is M-D68-24's "
                     "stock gate"
                     % (", ".join(W3S1B_ASKED["kinds"]["emergent"]),
                        ", ".join(W3S1B_ASKED["kinds"]["material"]),
                        len(W3S1B_ASKED["kinds"]["constant"]),
                        ", ".join(W3S1B_ASKED["kinds"]["constant"]),
                        "%.0f" % (abs(W3S1B_ASKED["alpha"]["dPhi_over_c2"][0]) / 1.65e-10),
                        _g(W3S1B_ASKED["alpha"]["max_abs_dalpha_over_alpha"], 2),
                        _g(W3S1B_ASKED["alpha"]["max_abs_2sigma"], 2))),
     "wave 3's W3B; spatial bounds on seven constants, OPEN"),
    ("M-D68-25",
     "M on weak correlations and the ranking of seats (M-RULINGS-2026-10-03.md item 25, "
     "2026-10-04); no question was put",
     _d68_carry_file("STATEMENT", "M-D68-25",
                     "as the hypothesis H-SEATRANK, in docket68/wave3/seatrank.py.  P = 1 + N "
                     "holds by normalisation of every signed measure (STRUCTURAL; it neither tests "
                     "nor supports the per-seat claim).  Unconstrained, the negatives fix only the "
                     "total: %s and %s share their negatives and rank opposite seats first.  In a "
                     "physical family (H-CONSTRAINED-FAMILY, %d qubit states) the negative minimum "
                     "locates the positive peak to a median %s against a random pairing's %s -- a "
                     "literal triangulation given knowledge of the family, not the negatives "
                     "deciding alone.  Projections recover peak and negatives together (argmin "
                     "error %s at K = 4, argmax error %s at K = 8): tomography, not M's mechanism.  "
                     "Resolving seats 0.30 against 0.25 by sampling the quasi-distribution "
                     "(H-QUASI-SAMPLING) costs typically %s samples at M = 1 and %s at M = 21, "
                     "about linear in M; measured seats carry no M factor.  Complex binary is not "
                     "addressed (OPEN).  No obstruction grade moves"
                     % (W3S1B["seatrank"].COUNTEREXAMPLE[0], W3S1B["seatrank"].COUNTEREXAMPLE[1],
                        W3S1B_ASKED["family"]["n_states"],
                        _g(W3S1B_ASKED["family"]["median_err"], 2),
                        _g(W3S1B_ASKED["family"]["median_ctrl"], 3),
                        _g([t for t in W3S1B_ASKED["tri"] if t["K"] == 4][0]["min_err"]),
                        _g([t for t in W3S1B_ASKED["tri"] if t["K"] == 8][0]["max_err"]),
                        "%.0f" % [c for c in W3S1B_ASKED["cost"] if c["M"] == 1][0]["typical"],
                        "%.0f" % [c for c in W3S1B_ASKED["cost"] if c["M"] == 21][0]["typical"])),
     "wave 3's W3C; the seat family and complex binary, OPEN"),
    ("M-D68-31",
     "M after Step 1b's first pass (M-RULINGS-2026-10-03.md item 31, 2026-10-05); no question "
     "was put",
     _d68_carry_file("INSTRUCTION", "M-D68-31",
                     "as H-COMPENSATION in step1b/compensate.py, each clause computed.  (C1) the "
                     "frame defect of the 70 kg body between Earth and Proxima b, %s to %s J "
                     "(H-SUN-FRAME), is AVOIDED when the object is built from B's stock (transfer "
                     "%s J) -- avoidance, not an opposite discrepancy.  (C2) a negative-energy "
                     "defect is compensated by quantum interest (Ford and Roman gr-qc/9901074v1, "
                     "READ), which always overcompensates.  (C3) bit errors are dissolved by "
                     "redundancy, I/(1 - h2(p)).  (C4) energy and bits compensate each other (%s "
                     "bits/s at 1 kW, %s at 4 kW; a bit buys up to kT ln 2), but baryon number, "
                     "lepton number and charge only themselves: baryons from energy cost %s times "
                     "the payload's rest energy (the antibaryons too)"
                     % (_g(W3S1B_ASKED["frame"]["defect_J_range"][0]),
                        _g(W3S1B_ASKED["frame"]["defect_J_range"][1]),
                        _g(W3S1B_ASKED["frame"]["built_from_B_stock_transfer_J"]),
                        _g(W3S1B_ASKED["ebb"][0], 2), _g(W3S1B_ASKED["ebb"][1], 2),
                        "%.3f" % (W3S1B_ASKED["bbf"][0] / W3S1B_ASKED["bbf"][1]))),
     "Step 1b's compensation column; nothing on this board"),
    ("M-D68-32",
     "M answered whether the original at A is retired into stock, so the object exists only at "
     "B (M-RULINGS-2026-10-03.md item 32, 2026-10-05) -- with a suspicion, which the file "
     "carries as M's hypothesis",
     _d68_carry_file("HYPOTHESIS", "M-D68-32",
                     "as H-RETIRE-A, a hypothesis and not a result: A's instance retired into stock "
                     "at A, the output row OUT-A-RESIDUE (balance.equation, asked: present %s).  "
                     "No-cloning computed both ways: the Buzek-Hillery cloner gives each copy "
                     "fidelity %s < 1 for every input (its optimality NAMED-NOT-READ), and CNOT "
                     "copies basis states perfectly (%s).  So H-RETIRE-A reaches the classical "
                     "description only: the Bell measurement already leaves no state at A without "
                     "taking the matter apart; retiring A's matter keeps the description at one "
                     "position.  The retire energy is OPEN (IN-A-RETIRE-E, within the chemical "
                     "ceiling +-%s J, openterms.py); an absorbed photon read at 1 A deposits about "
                     "%s Gy, which needs H-READ-BEFORE-DAMAGE"
                     % ("OUT-A-RESIDUE" in W3S1B_ASKED["eq_ids"],
                        "%.4f" % W3S1B_ASKED["nc"]["cloner_fid_max"],
                        all(W3S1B_ASKED["nc"]["cnot_copies_basis_states"]),
                        _g(W3S1B_ASKED["chem"]),
                        _g([r for r in W3S1B_ASKED["retire"]["compensation_by_read"]
                            if r["delta_m"] == 1e-10 and r["carrier"] == "photon"][0]
                           ["dose_Gy_if_absorbed"], 2))),
     "Step 1b's OUT-A-RESIDUE; H-STOCK-FORM and H-READ-BEFORE-DAMAGE, OPEN"),
    ("M-D68-35",
     "M's question on the corridor's size (M-RULINGS-2026-10-03.md item 35, 2026-10-05), "
     "answered by computation",
     _d68_carry_file("QUESTION", "M-D68-35",
                     "answered in docket68/wave3/aperture.py with the smallest opening each "
                     "reading permits (the 1 m throat, sized for a body, costs %s kg).  (A) the "
                     "whole description held at once: r = %s to %s m over the four counts "
                     "(throatbits.r_fit, a capacity ceiling, not an encoding).  (B) streamed over "
                     "one mode at the board's energy floor: about half the channel quantum's "
                     "wavelength, %s m in a year and %s m in a century for the species count; at "
                     "that width %s of the entropy flux lies below the cutoff (more width or power "
                     "needed), a TEM line has no cutoff, a circular guide's radius is about 0.59 "
                     "of it (H-HALF-WAVE, H-TEM-LINE, H-TE11).  (C) as a coupling: no "
                     "cross-section, hbar J = hbar I pi/2T, %s keV at one year.  As a geometric "
                     "throat these sizes lower the throat mass %s to %s times; the board's other "
                     "limits on small throats stand as graded"
                     % (_g(W3S1B_ASKED["ap"]["one_metre_throat_mass_kg"]),
                        _g(min(r["r_m"] for r in W3S1B_ASKED["ap"]["all_at_once"]), 2),
                        _g(max(r["r_m"] for r in W3S1B_ASKED["ap"]["all_at_once"]), 2),
                        _g(_w3_streamed("species", 3.15576e7)["width_m"], 2),
                        _g(_w3_streamed("species", 3.15576e9)["width_m"], 2),
                        "%.0f%%" % (100 * W3S1B["aperture"].below_cutoff_fractions()[0]),
                        "%.0f" % ([r for r in W3S1B_ASKED["ap"]["coupling"]
                                   if r["count"].startswith("species") and r["T_s"] == 3.15576e7][0]
                                  ["hbarJ_eV"] / 1e3),
                        _g(w3_throat_factors()[0], 2), _g(w3_throat_factors()[1], 2))),
     "the corridor's size on each reading; nothing on this board moves"),
    # ----- ADDED (CMB-seat, docstring section 8f): items 41 and 44.
    ("M-D68-41",
     "M's question on the background radiation (M-RULINGS-2026-10-03.md item 41, 2026-10-05, after DOCKET 68's "
     "close); no question was put",
     _d68_carry_file("QUESTION, CARRYING TWO HYPOTHESES", "M-D68-41",
                     "as H-CMB-CORRIDOR (the background builds the corridor) and H-CMB-UNIVERSAL (a "
                     "multi-spacetime constant), never as results.  Reading 1, the background's rest frame as "
                     "H-FRAME's frame, is answered in docket68/cmb/cmbframe.py (seated, M-D68-45): a lawful, "
                     "physical, measurable frame, read by each end locally and loop-free.  The background is "
                     "constant in frame and spectral form, not in temperature: T(z) beta lies within %s sigma of 0 "
                     "in every READ fit.  The multi-spacetime clause has no measurement and stays OPEN (CMB-O2); "
                     "the medium, register and carrier readings stay OPEN (CMB-O3)" % ("%.2f" % CMB_ASKED["tz_max_sigma"])),
     "H-FRAME (M-D68-C10), O9; the OPEN items CMB-O1..O4"),
    ("M-D68-44",
     "M's instruction on the background (M-RULINGS-2026-10-03.md item 44, 2026-10-05), answering an offer to READ the "
     "etymology of the word",
     _d68_carry_file("INSTRUCTION", "M-D68-44",
                     "in docket68/cmb/cmbframe.py's physics(): the photon gas has one rest frame; the dipole "
                     "amplitude over T0 is the observer's beta (%s), so an observer at that beta reads %s K ahead and "
                     "%s K behind; in FRW equal temperature is equal cosmic time"
                     % (_g(CMB_ASKED["beta_amp"], 7), "%.5f" % CMB_ASKED["T"][0], "%.5f" % CMB_ASKED["T"][180])),
     "H-CMB-CORRIDOR reading 1"),
    # ----- ADDED (CMB2-seat, docstring section 8g): items 46, 48, 50 and 52.
    ("M-D68-46",
     "M's question during H-CMB-CORRIDOR reading 2 (M-RULINGS-2026-10-03.md item 46, 2026-10-05); no question was put",
     _d68_carry_file("QUESTION, CARRYING A HYPOTHESIS", "M-D68-46",
                     "as H-CONTRACT (the universe contracts as well as expands), never as a result; answered in "
                     "docket68/cmb/medium.py's contraction() on M-D68-47: a nonsingular bounce keeps H-FRAME's frame, "
                     "since frame.py's lemma needs only a(t) > 0; whether the universe contracts stays OPEN (CMB2-O1)"),
     "H-FRAME (M-D68-C10); the OPEN item CMB2-O1"),
    ("M-D68-48",
     "M's statement on reading 2 (M-RULINGS-2026-10-03.md item 48, 2026-10-05); no question was put",
     _d68_carry_file("STATEMENT, CARRYING A HYPOTHESIS", "M-D68-48",
                     "as H-UNOBSERVED-MEDIUM, never as a result: modelled in docket68/cmb/unobserved.py on M-D68-49, "
                     "where the static global state is constant and, from the coupled ground state, M-SUPPORT is pure "
                     "and stationary while coupled"),
     "H-CMB-UNIVERSAL (M-D68-41); the OPEN items CMB2-O2, CMB2-O3"),
    ("M-D68-50",
     "M's statement after item 49 (M-RULINGS-2026-10-03.md item 50, 2026-10-05); no question was put",
     _d68_carry_file("STATEMENT, CARRYING A HYPOTHESIS", "M-D68-50",
                     "as H-CONSCIOUS-SELECTS, never as a result, in two readings: Born selection, under which Bob's "
                     "marginal spread is %s and there is no channel, and biased selection, priced in "
                     "docket68/cmb/bias.py (not seated)" % _g(CMB2_ASKED["o9_a"], 2)),
     "O9; the OPEN item CMB2-O4"),
    ("M-D68-52",
     "M's statement on what introduces the clock (M-RULINGS-2026-10-03.md item 52, 2026-10-05); no question was put",
     _d68_carry_file("STATEMENT, CARRYING A HYPOTHESIS", "M-D68-52",
                     "as H-LOCAL-CLOCK, never as a result, and as M's answer to H-M-SUPPORT's open dynamics: modelled "
                     "in docket68/cmb/localclock.py on M-D68-53 (Proxima b's orbital clock %s s per year slower than "
                     "Earth's); in Page's sensible quantum mechanics a conscious perception is a perception of a "
                     "present matter record" % ("%.3f" % CMB2_ASKED["clock_s"])),
     "H-M-SUPPORT; the OPEN items CMB2-O2, CMB2-O5"),
]

#: DOCKET 68's one pending question, M-D68-P1 (emtension.py's ER = EPR
#: citation), is NO LONGER PENDING: M had answered it before DOCKET 68 opened
#: ("Record it (Recommended)", applied the same day), and it is on RULED_BY_M
#: as M-D68-C12, its first text kept there as history
#: (D68_P1_AS_FIRST_RECORDED).  Nothing from DOCKET 68 is pending M.


# ----- index3.py's DOCKET 68 rows, checked against their owners -------------
# index3.py is stdlib-only, so it TYPES its owners' values; this file imports
# the owners and checks every typed value against what they compute now.

# _d68_e (a float as index3.py types it) is defined with the wave-2 helpers
# above, which print with it before this point.


def d68_index3_needles():
    """{index3 row id: [(what, the owner's value as the row must type it)]},
    built NOW from the owners -- never typed here."""
    from fractions import Fraction
    w2f1 = D68_ASKED["W2 x F1"]["per"]["O-BITS"]
    sup = ["{%s; %s}" % (", ".join(sp["members"]), ", ".join(sp["named"]))
           for sp in w2f1["supports"]]
    win = [sp.get("window", "").split(":")[0] for sp in w2f1["supports"]]
    alone = sorted(set(D68_ASKED[k]["per"]["O-BITS"]["verdict"]
                       for k in ("H-SETTLE alone (W2)", "H-FRAME clause 1 alone (F1)")))
    dctc = D68_ASKED["clause 2b's D-CTC (F2b)"]["per"]["O-BITS"]["supports"][0]
    pairs = [v for k, v in D68_FIRST["pairs_per_qubit"].items() if "W2 class without" in k][0]
    board_c = D68_ASKED["the board alone"]["per"]["O-LOOP-C"]
    lem = frame.frw_time_function_lemma()
    feed = _d68_feed()
    return {
        "D68-ONE-MEMBER-REMOVAL-AND-IT-IS-CONDITIONAL": [
            ("the variant count", "%s variants" % format(D68_VARIANT_COUNT, ",")),
            ("W2 x F1's verdict word", "only %s" % w2f1["verdict"]),
            ("support 1", sup[0]), ("support 2", sup[1]),
            ("support 1's window", win[0].split(" (")[0].replace(
                "ADMISSIBLE GIVEN", "admissible given")),
            # ADDED (DOCKET 68 wave 2): support 1 on the READ limits, asked of
            # settle.window_read (the cells' words) -- the 1 AU, N = 7 cell and
            # the reading at 1 AU, N = 1e3 that also needs H-SAME-EPS.
            ("support 1 at 1 AU, N = 7", "%s given W_W2R at 1 AU, N = 7"
             % dict(((L, N), w) for L, N, w, _p in d68_w2_window_cells())[("1 AU", 7)]),
            ("the H-SAME-EPS reading", "at 1 AU, N = 1e3 under reading %s also given H-SAME-EPS"
             % "/".join(r["reading"][:1] for r in D68_WINDOW_READ["rows"]
                        if (r["L"], r["N"]) == ("1 AU", 1000)
                        and not r["robust_across_READ_bounds"])),
            ("the limit's status", "at the READ limit" if all(
                v.startswith("READ") for v in D68_WINDOW_READ["statuses"].values())
             else "at the unread limit"),
            ("support 2's window", win[1]),
            ("W2 alone and F1 alone", "alone, each gives %s" % "/".join(alone)),
            ("the D-CTC support", "{%s; %s}" % (", ".join(dctc["members"]),
                                               ", ".join(dctc["named"]))),
            ("the class's pairs per qubit", ", ".join(
                str(Fraction(x).limit_denominator(64)) for x in pairs)),
            ("the midpoint first read", "%.5f of the light time"
             % (D68_FIRST["first_transit_midpoint"]["t_read"] / D68_FIRST["light_time_s"]))],
        "D68-EXACT-FRW-ADMITS-ONLY-EQUAL-COSMIC-TIME-CORRIDORS": [
            ("the lemma", "the claim %s" % lem["claim"]),
            ("its vacuity guard", "the vacuity guard %s" % lem["vacuity"]),
            ("its control", "the control a >= 0 %s" % lem["control_a_ge_0"]),
            ("the board's corridor O-LOOP", "%s {%s}" % (
                board_c["verdict"], ", ".join(board_c["supports"][0]["named"])))],
        # REMOVED (DOCKET 68 residuals): the row
        # D68-SIGNED-ENTROPY-IS-RE-H-PLUS-N-OVER-SEPARABLE-FUNCTIONALS, whose
        # Z = +1 had no numeric requirement stated by an owner; at Z = 0 it
        # sits on the null cell, so Q-1 and Q-1s are carried on O9 only
        # (index3.D68_ROW_REMOVED keeps it, and its needles, as history).
        "D68-O-SEAT-OPEN-VIA-S5-AND-THE-D25-GATE": [
            ("O-SEAT under H-SEAT-S5", "O-SEAT is %s" % d68_asked("the board alone", "O-SEAT")),
            ("O-SEAT given H-SEAT-ROUTES", "it is %s" % d68_verdict(D68_SEAT_ROUTES)),
            ("S13's named hypothesis, as combine's B-S13 states it", _d68_s13_phrase()),
            ("the first-order share", "about %.5f" % _d68_s13_share()),
            ("CI chondrite", "%.1f kg of CI chondrite" % feed["CI chondrite"]),
            ("stellar photosphere", "%s kg of stellar photosphere"
             % _d68_e(feed["stellar photosphere"])),
            # ADDED (DOCKET 68 wave 2): seat.py's binder and whether it is
            # measured in the Proxima system, asked.
            ("seat.py's binder", "binder at a CI-like body is %s, %.2f kg per kg of payload"
             % D68_SEAT["binder"]),
            ("the binder unmeasured", "measured in no Proxima-system star or body in the "
             "sources read" if D68_SEAT["P in the system"] is False
             else "measured in the Proxima system")],
    }


def d68_index3_faults(findings=None):
    """[(row, what)] where index3.py's DOCKET 68 row does not type its owner's
    current value (or the row is missing, or off (0,0,+1))."""
    import index3
    rows = dict((f[0], f) for f in (index3.FINDINGS if findings is None else findings))
    bad = []
    for rid, needles in d68_index3_needles().items():
        f = rows.get(rid)
        if f is None:
            bad.append((rid, "missing"))
            continue
        if tuple(f[1:4]) != (0, 0, 1):
            bad.append((rid, "cell %s" % (tuple(f[1:4]),)))
        bad += [(rid, what) for what, v in needles if v not in f[5]]
    return bad

# ---------------------------------------------------------------------------
# RIGHT SIDE -- THE SUPPLY.  What is actually available, and its ceiling.
#
# `gap_orders` is None where the row is REFUSED rather than expensive: the sign
# inverts, or the mechanism fails, BEFORE the magnitude is reached, and a gap
# would imply a ladder that is not there.
# ---------------------------------------------------------------------------

def _s5_docket65_append():
    """massform's "S5 (note)" row is an instruction -- 'APPEND to S5's note:
    <text>' -- so what is appended is the text after that prefix, asked.  The
    row must leave S5's status as it is (its status reads 'OPEN (unchanged)')."""
    prefix = "APPEND to S5's note: "
    row = PROPOSED["S5 (note)"]
    if not row[2].startswith(prefix) or row[3].split(" (")[0] != OPEN:
        raise ValueError("massform's S5 note is no longer an append to an OPEN "
                         "S5 -- ledger row S5 is stale")
    return row[2][len(prefix):]


#: The SUPPLY rows' names for DOCKET 65's priced remainders are massform's own
#: (massform.SURVIVES); S10's is a label for M's mechanism, not a result.
S10_NAME = "M's mechanism: atomic mass formed at the seat by the triggered Higgs field"


def s10_name_faults(name=None):
    """[fault] where S10's label is not a label for M's mechanism: it must
    begin "M's mechanism" and name 'by the triggered Higgs field', or it reads
    as a refusal of what S12 and S13 price."""
    name = S10_NAME if name is None else name
    bad = []
    if not name.startswith("M's mechanism"):
        bad.append("does not begin \"M's mechanism\"")
    if "by the triggered Higgs field" not in name:
        bad.append("does not name 'by the triggered Higgs field'")
    return bad


def _survives_name(word):
    """The one massform.SURVIVES name containing `word`, asked; raises if the
    owner no longer names exactly one such route."""
    hits = [n for n, _t in massform.SURVIVES if word in n]
    if len(hits) != 1:
        raise ValueError("massform.SURVIVES no longer names one %r route" % word)
    return hits[0]


def _s10_open_item():
    """massform's item "S10 (open)" -- the FINITE Higgs share -- as S10's note
    carries it on M's ruling M-D65-2 ('Fold into S10 (Recommended)'): an OPEN
    item inside S10's note, not a row.  Its text and movers are asked; it must
    still be an OPEN item on the SUPPLY side owned by FINITE_HIGGS_SHARE_STATUS,
    and that status must still read OPEN, or this raises rather than carrying
    a closed item as open."""
    r = PROPOSED["S10 (open)"]
    if (r[1], r[3], r[4]) != ("SUPPLY", OPEN, ("massform", "FINITE_HIGGS_SHARE_STATUS")) \
            or getattr(massform, r[4][1]) != OPEN:
        raise ValueError("massform's S10 (open) is no longer an OPEN item of S10 "
                         "-- ledger row S10's note is stale")
    return ("S10 (open), an OPEN item inside this note and not a row (M-D65-2): "
            + r[2] + ".  WHAT WOULD MOVE IT: " + r[5])


def _proposed_supply(rid, name):
    """A DOCKET 65 SUPPLY row: (id, name, status, owner, note).  A SUPPLY row has
    ONE note, so it carries the proposed claim and then what would move it, both
    asked of massform.PROPOSED_ROWS."""
    r = PROPOSED[rid]
    return (rid, name, _proposed_status(rid), r[4],
            r[2] + ".  WHAT WOULD MOVE IT: " + r[5])


SUPPLY = [
    ("S1", "negative effective mass (band curvature)", REFUSED, None,
     "STRUCK on KIND: m* is a dispersion curvature, not T_00.  It does not "
     "gravitate and will not source a metric -- m* as a quantity; the "
     "quasiparticle's energy does gravitate, as E/c^2, whatever the sign of "
     "m* (CORRECTED, DOCKET 67: the qualifier was dropped; KIND is "
     "unaffected)"),

    ("S2", "Casimir: ideal plates, and real curved mirrors", REFUSED, None,
     "STRUCK three ways by DOCKET 54 and once more by DOCKET 53.  The sign "
     "INVERTS for any real mirror at a_c = 0.480 x skin depth, "
     "materials-independent; 2G|m|/(ac^2) is a-INDEPENDENT so building it "
     "bigger buys nothing; and the plate outweighs its own Casimir energy for "
     "every material that exists.  CORRECTED (DOCKET 67): the row was named "
     "'Casimir between ideal plates' while this note argues real curved "
     "mirrors.  The inversion is a near-wall statement, eps <~ the plasma "
     "wavelength, inside the sphere (outside, the plasma term has the "
     "opposite sign); it rests on a RECONSTRUCTED spherical plasma prefactor "
     "(tolman.py, sign and order only) under a sharp boundary, the plasma "
     "model, T = 0 and omega_p eps/c << 1; its SIGN holds for every passive, "
     "local, sharp-boundary medium, but the NUMBER 0.480 is the plasma "
     "model's (Drude damping moves it -0.17%), and the two asymptotes it "
     "equates hold in disjoint ranges of eps, so a_c is not a physical "
     "threshold.  'Every material that exists' holds for ordinary atomic "
     "matter: the ratio is 2.72e-8 for hydrogen, 1.25e-5 for positronium, "
     + NUCLEAR_SHEET_RATIO_TEXT + " at nuclear density (address.RHO_NUCLEAR; "
     "DOCKET 67 follow-ups: first 7.43e-4, at the recalled 2.3e17), all "
     "below 1"),

    ("S3", "squeezed vacuum", MEASURED, ("candidates", "REQUIREMENT_SCALES_AS"),
     "THE LEAST-DEAD ROUTE and the only survivor of the four.  Passes KIND and "
     "DEADLINE, fails MAGNITUDE.  Untouched by DOCKET 54, because the parity "
     "argument bites boundary conditions and squeezing is a state.  DOCKET "
     "67: what experiments MEASURE is a quadrature variance below shot "
     "noise, which equals <:T00:> < 0 only in the single-mode plane-wave "
     "idealisation; and the MAGNITUDE failure is computed under flat space "
     "(H_flat) with the sampling time set to t0 = R/c, the spatial-length-as-"
     "time move DOCKET 55 withdrew in achievable.py -- flat space alone "
     "excludes a static negative density at every t0, so the failure "
     "holds a fortiori there"),

    ("S4", "non-minimal coupling", REFUSED, None,
     "STRUCK on the EFT field cutoff -- and see O1, which is the same field "
     "from the other side and is STRUCK THERE TOO, at the same inequality.  "
     "The draft of this row ended 'and is OPEN rather than struck', four "
     "words that counted one refusal as an opening and inflated the open "
     "count by one.  DOCKET 67 (2309.10848-eft-breakdown, NARROWED; the reopen "
     "adjudicated REOPENS-NARROWER; recorded on M's ruling of 2026-10-02) finds "
     "ONE WINDOW this refusal does not reach, and it is recorded inside this "
     "row, not counted as an open row (the inflation just named): in the "
     "xi < 0 sub-class -- in FFKP eq. (109)'s convention, shared by "
     "Fewster-Osterbrink and Barcelo-Visser, where xi < 0 is the "
     "Higgs-inflation sign; candidates.py's literal 'delta L = xi R phi^2' "
     "reads the same sub-class as xi_tree > 0 (candidates.XI_SIGN_CONVENTION) "
     "-- the window %g <= 8 pi G|xi| phi_max^2 < %.6f (l_UV >= %.6f l_P, "
     "candidates.xi_negative_window()) is %s: there the only ground against "
     "closure is FFKP's Einstein-frame tower, an order-of-magnitude argument "
     "with its Jacobian uncomputed.  OPEN, not supplied.  xi > 0 stays STRUCK "
     "(the exact constrained-saddle breakdown at eps = 1, the "
     "Planckian-momentum premise, O1); xi < 0 with eps < 1 stays excluded "
     "(every such closure point has l_UV < %.6f l_P, and the premise that a "
     "cutoff at a few Planck lengths is not an EFT carries no sign); S8 is not "
     "widened (it stays REFUSED on its own GUT-scale ground, which reaches the "
     "window: there phi_max is within a factor 1.140442 of the Barcelo-Visser "
     "gate field).  The window's edges rest on the sibling audit's Gaussian "
     "coefficient (candidates.NMC_GAUSSIAN_K, %s) and on the closure algebra "
     "sibling key 2309.10848 narrowed.  Recorded, not repaired: in the window "
     "specthm R6's 'S4 = O1 (one refusal, counted once)' and S8's 'the xi != 0 "
     "case is S4 and O1, both refused' do not hold, since O1 does not reach "
     "xi < 0" % (candidates.xi_negative_window()[0],
                 candidates.xi_negative_window()[1],
                 candidates.xi_negative_window()[2],
                 candidates.XI_NEGATIVE_WINDOW_STATUS,
                 candidates.xi_negative_window()[2],
                 candidates.NMC_GAUSSIAN_K_STATUS)),

    ("S5", "the reconstruction route: specification, not mass", OPEN,
     ("branelink", "S5_FIGURES_MEASURED"),
     # "THE ONLY ROW" until DOCKET 65: S11-S13 are priced OPEN rows too.
     "THE FIRST ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL, AND THE "
     "ONLY ONE UNTIL DOCKET 65 SEATED S11-S13.  No mass "
     "traverses, so the demand rows D1-D4 and D7 are not instantiated and go "
     "silent.  Bounded by D13 FOR A BRANE-CONFINED CARRIER and therefore not a "
     "shortcut ON THE BRANE; a bulk carrier is not bounded by it, which is O6. "
     " STATUS DOWNGRADED FROM MEASURED, AND THE REASON IS THIS FILE'S OWN "
     "DISCIPLINE TURNED ON ITSELF: the figures this row was seated on -- "
     "8.041537e23 s.J, 6.000728e15 J, 4.870712e59 J, 43.909 orders -- OCCUR IN "
     "NO FILE IN THIS TREE.  Measured by grep this pass, all four absent.  "
     "They came from a docket's scratch computation, the scratch died with a "
     "container restart, and no instrument can re-derive or check them.  A "
     "number nobody can re-run is not MEASURED however carefully it was once "
     "computed, and seating it here was the exact fault section 0 of this file "
     "says it exists to prevent.  Re-seating it needs an instrument, not a "
     "citation.  DOCKET 62, UNCHANGED AND SHARPENED: re-grepped, the four "
     "occur in this note and in no other file.  The O6/O7 pass's apparent "
     "reproduction of them is %s.  Owed: %s.  READ WITH D23 (DOCKET 62): "
     "the fabricator, the stock survey and the receiver all had to reach "
     "the destination at <= c first, so this row is an AMORTISATION SCHEME "
     "with a minimum setup of %.4g years at Proxima, not a transport route; "
     "and D25's stock gate must hold at the destination"
     % (branelink.S5_FIGURES_STATUS, branelink.S5_OWED, PROXIMA_LY)
     # DOCKET 65 appends (massform "S5 (note)"); nothing above is replaced.
     + ".  " + _s5_docket65_append()),

    # ----- DOCKET 63: the Higgs as supply.  All REFUSED, all gap None. ------
    ("S6", "Higgs displacement as an ADDRESS", REFUSED,
     ("excite", "ROLE1_DOMINATED_BY_OWN_SOURCE"),
     "The source is a better address than the displacement it creates: its "
     "gravity reads the region farther (address.py section 9, the "
     "domination theorem), and its own interior redshift beats the vev "
     "signal beyond %.2g cm (m proportional to phi), %.2g cm (H1) or %.2g cm "
     "(H2).  Consistent with D14"
     % tuple(100.0 * excite.COURIER_CROSSOVER_M[k]
             for k in ("m propto phi", "H1", "H2"))),

    ("S7", "Higgs displacement as a BINDER", REFUSED,
     ("excite", "ROLE2_REBINDS"),
     "The m_e mechanism is exactly null (D18).  What remains is O(eps) "
     "through m_p/m_e, and it needs D20's filling source: a small, computable "
     "shift, inside matter denser than any object, and never a rebinding"),

    ("S8", "Higgs as an NEC-violating source at the endpoint", REFUSED,
     ("higgs", "MINIMAL_SCALAR_SATISFIES_NEC"),
     "Minimal coupling is D17.  The xi != 0 case is S4 and O1, both refused; "
     "it needs phi at the GUT scale, xi_req = %.4g, a field %.0e (upper "
     "edge) to %.0e (lower edge) times Degrassi's instability scale "
     "10^(%g +- %g) GeV, %.0e at the centre, where the quartic is negative "
     "-- not an excitation of our vacuum.  CORRECTED (DOCKET 67): the row "
     "was named 'a negative-energy source', but D17 is an NEC statement; "
     "'needs phi at the GUT scale' holds under a cap xi <~ 1.5e4 (a field "
     "below Degrassi's band needs xi >= 5.93e12) and takes the MSSM-"
     "conditional 2e16 GeV; 'where the quartic is negative' holds at the "
     "central top mass with SM running up to that scale, and 2e16 GeV is "
     "122x above M_red/xi, where Degrassi call the shape uncontrolled; the "
     "band is a ~1 sigma, Landau-gauge band, not hard edges.  The refusal "
     "rests on D17 and S4/O1, not on the sign.  DOCKET 63's printed '%s to %s' is "
     "the upper edge to the centre (excite.py: %s), %.0f%% of the band in "
     "log10; nothing turns on it"
     % (excite.XI_REQUIRED_AT_GUT,
        excite.XI_FIELD_OVER_INSTABILITY_UPPER_EDGE,
        excite.XI_FIELD_OVER_INSTABILITY_LOWER_EDGE,
        endpoint.DEGRASSI_LOG10_LI, endpoint.DEGRASSI_LOG10_LI_ERR,
        excite.XI_FIELD_OVER_INSTABILITY_CENTRE,
        excite.RULING_S8_PRINTED_RANGE[0], excite.RULING_S8_PRINTED_RANGE[1],
        " and ".join("/".join(m) for m in excite.RULING_S8_MATCHES),
        100.0 * excite.RULING_S8_COVERS_FRACTION_OF_BAND)),

    # ----- DOCKET 62: warpfolder.py's adjudication, the principle applied. --
    ("S9", "the Drive folder's device specification (warpfolder.py)", REFUSED,
     ("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM"),
     "The only complete device specification written for this project, "
     "REFUSED AS A SUPPLY on two independent counts.  Its own printed "
     "hardware stores %.0f J against the %.4g J its own premise needs at "
     "%.0f kg -- short by %.1f orders ON ITS OWN NUMBERS, the energy budget "
     "never connected to the chain (ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN "
     "= %s).  CORRECTED (DOCKET 67): that store is the PULSED-ignition "
     "subsystem (the Marx bank and laser); the folder also energises a 20 T "
     "stator, 85,000 RPM rotors it names as kinetic storage, and a muCF "
     "cell, none quantified, and bounded by the printed dimensions the "
     "whole device is at least 5.7 orders short, not 15.8.  And its "
     "reconstruction mechanism "
     "is INVERTED: heating to the electroweak scale restores the symmetry "
     "(HEATING_TO_EW_SCALE_RESTORES_SYMMETRY = %s) and un-generates the masses it was to template -- in the one-doublet "
     "SM, where this is a crossover near 160 GeV above which <phi> is "
     "approximately zero and the tree-level vev masses go with it "
     "(CORRECTED, DOCKET 67: 'restores' labels a crossover).  That shortfall is "
     "the specification against itself, not a gap against this board's demand, "
     "so the row carries none.  NOT ADJUDICATED, and not to be quoted either "
     "way: %s -- the first is the only folder claim that touches this "
     "column"
     % (warpfolder.stored_joules(),
        warpfolder.rest_energy_j(warpfolder.PAYLOADS_KG[0]),
        warpfolder.PAYLOADS_KG[0],
        math.log10(warpfolder.shortfall(warpfolder.PAYLOADS_KG[0])),
        warpfolder.ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN,
        warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY,
        "; ".join(warpfolder.NOT_ADJUDICATED))),

    # ----- DOCKET 65: massform.py, seated on M's ruling.  S10 REFUSED (gap
    # None); S11-S13 the priced remainders, OPEN.  All asked. ---------------
    # S10's note carries the item S10 (open) on M's ruling M-D65-2.
    _proposed_supply("S10", S10_NAME)[:4]
    + (_proposed_supply("S10", S10_NAME)[4] + ".  " + _s10_open_item(),),
    _proposed_supply("S11", _survives_name("anomaly")),
    _proposed_supply("S12", _survives_name("pair")),
    _proposed_supply("S13", _survives_name("held-seat")),
]

# DOCKET 68 NOTES on the supply rows O-SEAT touches (docstring section 7): a
# note appended to each, asked, with NO status change.
D68_NOTES.update({
    "S5": (
        "  DOCKET 68 (a note; no status change): this is the board's "
        "supply-from-the-seat route by which O-SEAT -- O-MATTER relocated to "
        "the supply at the seat on M's ruling M-D68-5 -- could be removed.  "
        "Under H-SEAT-S5, which M adopted (M-D68-7), O-SEAT reads %s (combine, "
        "O9's variants); given H-SEAT-ROUTES, the alternative on "
        "record, it reads %s.  Removed only if this route's supply is shown and "
        "D25 holds; neither is.  WAVE 2 (seat.py, W2C-seat) itemised DOCKET 56's "
        "owed instrument for this route at Proxima (seat.DOCKET56_OWED, asked): %s; "
        "and seat.grade_o_seat on today's board state is %s (D25's note carries "
        "the gate's binder)"
        % (d68_uniform("O-SEAT"), d68_verdict(D68_SEAT_ROUTES), d68_s5_owed(),
           D68_SEAT["grade"])),
    "S10": (
        "  DOCKET 68 (a note; no status change): combine.py encodes this row "
        "as B-S10 in O-SEAT's screen -- on M's reading of what arrives "
        "(M-D68-1, M-D68-5) the substance is supplied at the seat, and this row "
        "gives no such supply -- so no "
        "variant O9 asks removes O-SEAT through it (O-SEAT: %s)"
        % d68_uniform("O-SEAT")),
    "S13": (
        "  DOCKET 68 (a note; no status change): on M's reading of what "
        "arrives (M-D68-1, M-D68-5) the substance is supplied at the seat, and this "
        "route is not that supply because it forms no baryons (C3, under H-C3), "
        "so every baryon must already be at the seat; the share of the "
        "payload's mass already there is about %.5f at first order (H-LINEAR: "
        "an estimate, and as a bound OPEN), as measure.py computes it from "
        "massform's figures" % _d68_s13_share()),
})
SUPPLY = [r[:4] + (r[4] + _d68_note(r[0]),) for r in SUPPLY]


# DOCKET 66 NOTES (docstring section 8): appended AFTER each row's DOCKET 68
# note, asked, with NO status change -- no owner's computed status moved.  S5
# carries the O-SEAT pathways a defect seat or QET adds; S13 the defect-core
# link (A1's answer item 7, combine66's ground).
def _d66_defb_read():
    """combine66's N_DEFB text, READ: its READ clause, and D66 wave 1's words
    it keeps ('Wave 1 first said ...')."""
    t = combine66.D66_OPEN["N_DEFB"]
    read = t.split("READ (HK pp.63-65): ")[1].split(".  Wave 1 first said")[0]
    first = re.search(r"Wave 1 first said '([^']+)'", t).group(1)
    return read, first


def _d66_massform_link():
    """The defect-core link's massform values, asked of massform (the owner of
    TEMPLATE and S13) exactly as combine66's grounds ask them: TEMPLATE on C1
    alone, TEMPLATE with C1's link holding, TEMPLATE's C3 reason, whether the
    held-seat route forms baryons, and its stable range."""
    vals = massform.mechanism_values()
    v1 = dict(vals)
    v1["C1"] = True
    return {"TEMPLATE": massform.derive_readings(vals)["TEMPLATE"][0],
            "TEMPLATE, C1 holding": massform.derive_readings(v1)["TEMPLATE"][0],
            "C3 reason": massform.READING_REASONS[("TEMPLATE", "C3")][1],
            "forms baryons": massform.HELD_SEAT_ROUTE["forms baryons"],
            "stable range": massform.STABLE_RANGE}


D66_NOTES = {
    "S5": (
        "  DOCKET 66 (a note; no status change): a topological defect AT THE SEAT "
        "(H-DEFECT-SEAT, M's hypothesis, M-S1A-P3 (ii)) supplies no matter.  O-SEAT reads "
        "%s (combine66, asked) -- N_DEFB beside this row's N_S5, READ (HK pp.63-65): %s "
        "(D66 wave 1 first said: %s) -- and %s; given H-SEAT-ROUTES, %s.  QET is no supply "
        "of substance: qet.grades reads O-SEAT %s -- QET relocates at most E_A (supremum "
        "E_B/E_A = %.4f in the minimal model, approached as k/h grows), and the 70 kg "
        "payload's rest energy, %s J, would need more than %s J injected at the source "
        "under H-MINIMAL.  The seat condition M-S1A-P3 (i): %s (combine66; the wall under "
        "H-VIS-MINKOWSKI, defects.vis_time_function); under H-SM-ONLY no stable defect "
        "seat exists (A1).  combine66's full screen lifts O-SEAT in no consistent variant "
        "(B-combine66.md, READ)"
        % ((d66_group(D66_DEFECT_SEATS, "O-SEAT"),) + _d66_defb_read()
           + (d66_group(("H-THROAT-BITS: R-HOLO (TBHOLO)", "H-THROAT-BITS: R-TELEPORT (TBTEL)",
                         "H-QET-EXOTIC: R-QET (QET)", "H-DEFECT-SEAT: string-supported throat (DTHR)"),
                        "O-SEAT"),
              d66_asked("H-SEAT-ROUTES on DSTR", "O-SEAT", reading=True),
              D66_FIG["R-QET O-SEAT head"], D66_FIG["QET sup E_B/E_A"],
              _d66_e(D66_FIG["QET payload rest J, injection J"][0], 4),
              _d66_e(D66_FIG["QET payload rest J, injection J"][1], 4),
              d66_group(D66_DEFECT_SEATS, "SEAT")))),
    "S13": (
        "  DOCKET 66 (a note; no status change): the defect-core link (A1-defects.md answer "
        "item 7; combine66's ground, asked here of massform, the owner, as combine66 asks "
        "it).  A defect core holds |phi| = 0 with no local source, by topology, below this "
        "route's stable range (massform.STABLE_RANGE = %s); the same topology forbids a "
        "local release -- only annihilating the defect ends the hold -- so this route's "
        "H-RELEASE cannot apply there.  massform.derive_readings gives TEMPLATE %s on C1 "
        "alone and %s with C1's link holding: at a defect core the GROUND of the refusal "
        "moves from P-UNIFORM to topology, and the grade does not -- for TEMPLATE, %s, and "
        "this route forms baryons: %s -- so a defect-core TEMPLATE is no supply of "
        "substance, and O-SEAT does not move (combine66: %s)"
        % (_d66_massform_link()["stable range"], _d66_massform_link()["TEMPLATE"],
           _d66_massform_link()["TEMPLATE, C1 holding"], _d66_massform_link()["C3 reason"],
           _d66_massform_link()["forms baryons"], d66_group(D66_DEFECT_SEATS, "O-SEAT"))),
}


def _d66_note(rid):
    """The DOCKET 66 note a row carries, or ''."""
    return D66_NOTES.get(rid, "")


SUPPLY = [r[:4] + (r[4] + _d66_note(r[0]),) for r in SUPPLY]

# ---------------------------------------------------------------------------
# WHAT IS OPEN.  (row id, claim, what would answer it, owner)
#
# The count is statuses()'s, never typed.  `owner` names the instrument that
# seated the row's latest narrowing and an attribute that says whether the row
# CLOSED; the selftest asks it, and an owner answering True fails the ledger,
# because a row cannot be open here and closed there.  DOCKET 62 narrowed all
# five and closed none; the wording each narrowing replaced is kept below in
# SUPERSEDED_WORDING.
# ---------------------------------------------------------------------------

#: O5 AS DOCKET 62 WROTE IT (claim, answer), still computed from throatmass.py
#: so the kept wording is the wording the board printed.  DOCKET 64 replaced
#: it; SUPERSEDED_WORDING keeps it.
#: CORRECTED (DOCKET 67), recorded against this kept wording and not edited
#: into it (it is what the board said): "The largest ever built" is the
#: tree's survey-completeness hypothesis -- HPS p.8 call the 300 l_P throats
#: 'local' solutions with horizons far from the throat, not shown, and say
#: throats can be arbitrarily large; "EXPELLED rather than refuted ... an
#: expulsion names no hypothesis to attack" is wrong of AMM, whose failure
#: names a growing gauge-invariant mode, and Flanagan-Wald place eps ~ 1
#: outside their theorem, not outside semiclassical gravity.  The superseded
#: row's why cell carries this into LEDGER.md.
O5_DOCKET62 = (
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "at all?  NARROWED BY DOCKET 62 (throatmass.py), status unchanged.  %d "
     "self-consistent families are in print, %d of them with m < 0: in the "
     "proper-distance gauge a throat has m = %s, and all the non-perturbative "
     "constructions are throats; the new content is the series result, %s.  "
     "The largest ever built is %.4g m, %.2f orders short of one metre.  No "
     "no-go forbids m < 0 -- %s, not NO, with a control that fires.  "
     "Flanagan-Wald and Sanders 5.1 are NOT applied, their hypotheses failing "
     "at the corridor; and if eps ~ 1 lies outside semiclassical gravity the "
     "corridor is EXPELLED rather than refuted, which is worse, because an "
     "expulsion names no hypothesis to attack.  The claim that no QEI can "
     "bound rho_ren is %s, so O5 is NOT separated from O2 permanently"
     % (throatmass.SELF_CONSISTENT_FAMILIES_RETURNED,
        throatmass.FAMILIES_WITH_NEGATIVE_MASS, throatmass.THROAT_MASS,
        throatmass.SERIES_RESULT, throatmass.LARGEST_THROAT_M,
        throatmass.ORDERS_SHORT_OF_ONE_METRE,
        throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND,
        throatmass.NARROWING_3_STATUS),
     throatmass.O5_ANSWERED_BY + ".  Read Anderson-Hiscock-Samuel PRD 51 4337 "
     "first")


#: THE FIVE O ROWS DOCKET 62 NARROWED (docstring section 4).  Named, so the
#: checks on narrowed rows ask for them by name and a later O row cannot be
#: mistaken for one of them.
DOCKET62_NARROWED = ("O2", "O3", "O5", "O6", "O7")


def _hps_ll_denominator(power):
    """HPS's ll-log denominator written as qeihps.py writes it, from
    hpscentre.py's integer power -- so the two instruments' repairs can be
    compared as strings rather than retyped."""
    return "/(f^2 r)" if power == 1 else "/(f^2 r^%d)" % power


OPEN_ROWS = [
    ("O5",
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "INSIDE THE DOMAIN ITS <T> IS ESTABLISHED FOR?  NARROWED BY DOCKET 64 "
     "(hpscentre.py, qeihps.py), status unchanged.  HPS's system has %d "
     "disagreements with Popov; conservation decides them uniquely (tt-log "
     "coefficient %d, th %d, ll-log denominator %s), and qeihps.py's "
     "independent single-change scan finds the same two HPS repairs (%s: %d "
     "-> %d; %s: %s -> %s).  In that conserved system HPS's own throat data "
     "have m < 0 in the flare, first at %.4f l_P (MEASURED; the %s reading "
     "only).  A regular centre has %s (THEOREM, formal series; %s).  Every "
     "non-flat analytic regular-centre solution of %s changes the sign of m "
     "and is "
     "not asymptotically flat (THEOREM, 3L0 + 4 > 0, L0 != -1); for the "
     "nonlinear solutions non-flatness is %s, and their asymptotics are %s.  "
     "m < 0 FOUND IN HPS'S SYSTEM (%s reading) = %s; FOUND INSIDE THE ESTABLISHED DOMAIN "
     "= %s -- %s.  Which system HPS integrated: %s.  Kontou's requested "
     "test: %s.  Fewster-Smith on HPS: %s.  On the throat geodesic: %s.  "
     "CORRECTED (DOCKET 67): HPS's m < 0 solutions are built from modes "
     "non-perturbative in hbar (omega_1 ~ hbar^(-1/2), ripple wavelength "
     "0.187 l_P), which the order-reduction literature holds non-physical, "
     "naming HPS; 'derived or established' holds on its 'established' half, "
     "the 'derived' half being contested (HPS p.3, Arrechea App. B); and "
     "FO's and FFKP's theorems are REFUSED on HPS's state as published -- "
     "both hold only for Hadamard states, and that clause is NOT-ESTABLISHED "
     "(qeihps.py; OPEN were the state Hadamard, FO's global hyperbolicity "
     "then met locally), and FFKP's printed Ricci term needs R_ll = 0 or "
     "xi = 0 (CORRECTED, DOCKET 67 follow-ups: this read 'FO's and FFKP's "
     "theorems apply in form only where their hypotheses do -- FO needs "
     "global hyperbolicity', before M's ruling added the Hadamard "
     "hypothesis).  %d of the %d families ONE literature pass "
     "returned as self-consistent REPORT m < 0 (throatmass.py, READ) -- "
     "true of what was reported, and no longer the tree's finding (DOCKET "
     "67: other families are cited, 2607.07583v1 p.1, and KS, Garattini and "
     "APT are not fixed-point self-consistent solutions; Garattini's m > 0 "
     "is fixed by its ansatz)"
     % (hpscentre.PRINTED_DISAGREEMENTS,
        hpscentre.CONSERVED["a_tt"], hpscentre.CONSERVED["a_th"],
        _hps_ll_denominator(hpscentre.CONSERVED["ll_pow"]),
        qeihps.REPAIR_CONSERVATION[0], qeihps.REPAIR_CONSERVATION[2],
        qeihps.REPAIR_CONSERVATION[3], qeihps.REPAIR_DIMENSION[0],
        qeihps.REPAIR_DIMENSION[2], qeihps.REPAIR_DIMENSION[3],
        hpscentre.FIRST_NEGATIVE_M_THROAT_LP,
        hpscentre.THROAT_M_NEGATIVE_READING, hpscentre.CENTRE_M_LEADING,
        hpscentre.RECURSION_DIRECTION,
        hpscentre.LINEAR_CENTRE_THEOREM_SCOPE,
        hpscentre.NONLINEAR_CENTRE_NONFLATNESS,
        hpscentre.NONLINEAR_CENTRE_ASYMPTOTICS,
        hpscentre.THROAT_M_NEGATIVE_READING.lower(),
        hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
        hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN, hpscentre.DOMAIN_WORD,
        hpscentre.HPS_INTEGRATED_THE_PRINTED_SYSTEM,
        qeihps.KONTOU_REQUESTED_TEST_ON_HPS, qeihps.FEWSTER_SMITH_ON_HPS,
        qeihps.VERDICT_THROAT_GEODESIC,
        throatmass.FAMILIES_WITH_NEGATIVE_MASS,
        throatmass.SELF_CONSISTENT_FAMILIES_RETURNED),
     hpscentre.O5_ANSWERED_BY,
     ("hpscentre", "O5_CLOSED")),

    ("O6",
     "THE BRANE-BULK TRANSDUCER.  NARROWED BY DOCKET 62 (branelink.py), NOT "
     "CLOSED.  The row's stated cause of death -- no coupling in print -- is "
     "REFUTED: %s.  Eot-Wash bounds %s.  The throughput the closure called "
     "decisive, recomputed at omega_GW = %d Omega, is h = %.4e and %.4e "
     "bits/s/W; the pass used Omega and its figures were %.0fx and %.0fx too "
     "large, kept as withdrawn values in branelink.py.  It does not close: "
     "the closing premise, a %s, is %s; the closure runs through O7's "
     "UNTESTED B = 0, where the %.1f ns saving is evaluated; and the honest "
     "shape is a dichotomy -- %s -- so the row is settled %s"
     % (branelink.COUPLING_SOURCE, branelink.EOTWASH_BOUNDS,
        branelink.OMEGA_GW_OVER_OMEGA, branelink.STRAIN_H,
        branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.WITHDRAWN_STRAIN_H / branelink.STRAIN_H,
        branelink.WITHDRAWN_THROUGHPUT / branelink.THROUGHPUT_BITS_PER_S_PER_W,
        branelink.CLOSING_PREMISE, branelink.CLOSING_PREMISE_STATUS,
        branelink.SAVING_AT_B0_NS,
        "; ".join("if the %s: %s" % b for b in branelink.O6_DICHOTOMY),
        branelink.O6_SETTLED),
     "whether the graviton is a bulk degree of freedom -- on that branch the "
     "row settles, on the other it reverts -- together with the closing "
     "premise derived for a bulk carrier.  Still conceded: no moving-brane "
     "emission rate is in print, and the non-zero-winding amplitude has "
     "never been computed by anyone",
     ("branelink", "O6_CLOSED")),

    ("O7",
     "OUR OWN BOOST B RELATIVE TO THE PREFERRED BRANE FRAME.  The bulk saving "
     "is Delta_tau = (L/Gamma^2)[1/(1-B) - 1/(gamma-B)], THE FULL LIGHT TIME "
     "as B approaches 1/beta, and B cannot be purchased, because buying it "
     "means boosting the fabricator out of the destination's rest frame and "
     "forfeiting the destination-supplied atoms that are the premise.  "
     "NARROWED BY "
     "DOCKET 62 (branelink.py), NOT CLOSED: GW170817 bounds %s -- beta <= "
     "%.6e, CONDITIONAL on %s, and on the GW and light leaving together "
     "along one line of sight (GW170817's simultaneous emission; the "
     "source's -100 s case gives "
     "beta <= 2.757e-7) -- so at B = 0 the saving is %.4f ns, a fraction "
     "%.1e of the light time.  The provenance of that figure is %s; the "
     "dipole's Gamma - 1 = %.4e is a candidate for B and enters only through "
     "the anisotropy (that figure is barycentric arithmetic on a two-figure "
     "370 km/s; Earth's own runs 6.5e-7 to 8.9e-7 over a year, and reading "
     "the dipole as a velocity assumes it is kinematic).  B IS UNMEASURED, "
     "and the escape is priced: B >= %.9f buys one second over the Proxima "
     "span -- a necessary floor for antipodal propagation with the boost "
     "direction fixed, not a sufficient price (0.9994645711 on the real "
     "sky), and at such B GKLM's beta bound, derived at B = 0, is 57.1x "
     "looser.  The loop-induced SME route is a null %.0f orders short (at "
     "beta = 1 and r = 38.6 um on the bulk-graviton branch; 57 orders at "
     "that branch's beta bound).  CORRECTED (DOCKET 67): the emission, "
     "reference-frame, floor and SME conditions were unstated.  The proposed "
     "R-1 row is this row renamed and is not opened"
     % (branelink.GW170817_BOUNDS, branelink.BETA_MAX,
        branelink.BETA_BOUND_CONDITIONAL_ON, branelink.SAVING_AT_B0_NS,
        branelink.SAVING_FRACTION, branelink.PROVENANCE_94NS,
        branelink.CMB_GAMMA_MINUS_1, branelink.B_FOR_ONE_SECOND,
        branelink.SME_ORDERS_SHORT),
     branelink.O7_ANSWERED_BY,
     ("branelink", "O7_CLOSED")),

    ("O2",
     "Fewster & Teo's exact static-spacetime QEI on the corridor.  NARROWED BY "
     "DOCKET 62 (fewsterteo.py), NOT CLOSED.  Its prefactor is %s as "
     "printed (READ, pi glyph restored, fixed by four in-paper routes), and "
     "both sympy routes solve for it from the pi-restored (2.10) and (3.2) "
     "(CORRECTED, DOCKET 67 follow-ups: this read 'exactly 1, two routes in "
     "sympy -- in the tree's reading'; on the text-layer -1/2 readings, each "
     "missing the same pi, both routes return 1 = pi x 1/pi; it feeds no "
     "figure).  Its %d/%d against Ford-Roman is exact and MUST NOT be "
     "applied to C_F, which already IS that family's constant at the optimal "
     "compactly supported sampler (the Parseval route is new; the agreement "
     "of two evaluations of one closed form is not a check).  Its Sec. 7 does "
     "not transplant to M < 0, the horizon being its mode-defining surface.  "
     "The corridor's own mode functions are %s (DOCKET 67: that class is "
     "the constant-M vacuum segment's, not the regular-centre corridor's "
     "globally, and a convergent Frobenius series determines them; they are "
     "uncomputed).  The proposed curvature "
     "tightening came entirely from the witness's H^3 spectral gap, and the "
     "corridor has none (%s: gap %g), so the persistence refusal stays at "
     "%.3f orders, unmoved in either direction"
     % (fewsterteo.PREFACTOR_212_PRINTED, fewsterteo.NINE_64[0], fewsterteo.NINE_64[1],
        fewsterteo.CORRIDOR_MODE_FUNCTIONS, fewsterteo.GAP_HYPOTHESIS,
        fewsterteo.CORRIDOR_SPECTRAL_GAP, fewsterteo.FLAT_SHORTFALL_ORDERS),
     fewsterteo.O2_ANSWERED_BY + ".  The right instrument is " +
     fewsterteo.RIGHT_INSTRUMENT + " (for Hadamard states on a small enough "
     "sampling domain -- DOCKET 67) -- not Fewster & Teo's difference QEI"
     # DOCKET 64 appends (ruling C, O2), worded as noise.py states it: the
     # spectrum is bounded BELOW by the QEI bound, not equal to it.
     + ".  It also decides D22's distribution question on the corridor "
     "(noise.CURVED_PART_CARRIED_BY = %s): by FFR 1004.0179 note [18] every "
     "measurement distribution is supported in the spectrum of the sampled "
     "operator, which an absolute QEI bounds below -- deciding it where the "
     "evaluated bound is below the demanded magnitude and holds on the whole "
     "domain of a self-adjoint realisation (a curved H3); CORRECTED, DOCKET "
     "67: 'decides' was unconditional"
     % noise.CURVED_PART_CARRIED_BY,
     ("fewsterteo", "O2_CLOSED")),

    ("O3",
     "Whether ANY braneworld shortcut yields a closed timelike curve -- with "
     "the NEC satisfied everywhere, the clause FOLDED IN rather than opened as "
     "a row.  NARROWED AND SPLIT BY DOCKET 62 (latticectc.py), NOT CLOSED.  "
     "The flat-bulk quotient is SETTLED by D21, where GKLP's 'no' is forced.  "
     "The proposed codimension-one 'yes' is REFUSED as an answer: %s"
     % latticectc.CODIM1_CTC_REFUSAL,
     latticectc.O3_ANSWERED_BY + " (for an Einstein(+Lambda) bulk, for "
     "which the Israel form is the junction condition; a Gauss-Bonnet bulk "
     "takes Davis's -- DOCKET 67)",
     ("latticectc", "O3_CLOSED")),

    # DOCKET 65 opens no O row: the finite Higgs share, first seated here as
    # O8, is an OPEN item inside S10's note on M's ruling M-D65-2.
]

#: M's thesis, verbatim from CHARTER.md.  CORRECTED (DOCKET 68 residuals):
#: this comment first said the selftest checked it, and none did; it is now in
#: d68_words_faults() (_d68_held_texts), with D68_QUESTION.
D68_THESIS = ("My idea is that warp travel costs little because we are only relying on "
              "the communication of information between two entangled locations in "
              "spacetime")
#: The docket's question, as one sentence, verbatim from CHARTER.md.
D68_QUESTION = ("Is there a channel, beyond linear quantum mechanics or beneath geometry, "
                "in which Bob's statistics depend on Alice's choice?")
#: Q-1s's worked example, the charter's own: p = (1.5, -0.5).
D68_Q1S_P = (1.5, -0.5)

#: INLINE QUOTATIONS of the tree's words in DOCKET 68 cells (here and in
#: index3.py's DOCKET 68 rows), each with the file it must occur in verbatim.
#: ADDED (DOCKET 68 residuals): the D23 note printed M's words emended ('it
#: already exists everywhere', inherited from combine.py) and no check saw it,
#: because d68_words_faults covered D68_M_WORDS alone.  d68_quote_faults()
#: also requires every double-quoted span in a DOCKET 68 ledger cell, and
#: every single-quoted span in index3's DOCKET 68 rows, to be one of these
#: held texts or a declared non-quotation (D68_NOT_QUOTES).
D68_INLINE_QUOTES = {
    "D23 note: M's words on information": ("because is already exists everywhere",
                                           D68_CHARTER_FILE),
    "O9: M-D68-7, shortened": ("S5 counts", D68_RULINGS_FILE),
    "index3 O-SEAT row: M-D68-5": ("from the seat", D68_RULINGS_FILE),
    "index3 O-SEAT row: M-D68-7": ("S5 counts (Recommended)", D68_RULINGS_FILE),
    "M-D68-3's question, as the file heads it": ("All its inverses and reflections",
                                                 D68_RULINGS_FILE),
    "M-D68-C10: the charter on flatness": (D68_CHARTER_STRIKE, D68_CHARTER_FILE),
    "M-D68-C1: the charter's header": ("CHARTER, NOT YET OPENED", D68_CHARTER_FILE),
    "M-D68-C12: the question put, as item 14 records it": (D68_C12_QUESTION, D68_RULINGS_FILE),
    "M-D68-12: the question, as item 12 records it": (D68_PAPER_QUESTIONS["M-D68-12"],
                                                      D68_RULINGS_FILE),
    "M-D68-13: the question, as item 13 records it": (D68_PAPER_QUESTIONS["M-D68-13"],
                                                      D68_RULINGS_FILE),
    "M-D68-12: the paper's first wording, as item 12 quotes it": (D68_PAPER_FIRST_WORDING,
                                                                  D68_RULINGS_FILE),
    # ADDED (R-seat): M's DOCKET 66 rulings, items 26-28 -- the questions and
    # what the file records as applied (the file's words, not M's), and the
    # paper's first wording, as item 26 quotes it and as the paper prints it.
    "M-D68-26: the question, as item 26 records it": (D66_RULING_QUESTIONS["M-D68-26"],
                                                      D68_RULINGS_FILE),
    "M-D68-27: the question, as item 27 records it": (D66_RULING_QUESTIONS["M-D68-27"],
                                                      D68_RULINGS_FILE),
    "M-D68-28: the question, as item 28 records it": (D66_RULING_QUESTIONS["M-D68-28"],
                                                      D68_RULINGS_FILE),
    "M-D68-26: what the file records as applied": (D66_RULING_CARRIED["M-D68-26"],
                                                   D68_RULINGS_FILE),
    "M-D68-27: what the file records as applied": (D66_RULING_CARRIED["M-D68-27"],
                                                   D68_RULINGS_FILE),
    "M-D68-28: what the file records as applied": (D66_RULING_CARRIED["M-D68-28"],
                                                   D68_RULINGS_FILE),
    "M-D68-26: the paper's first wording, as item 26 quotes it": (D66_PAPER_FIRST_WORDING,
                                                                  D68_RULINGS_FILE),
    "M-D68-26: the paper's first wording, as its DOCKET 66 marker prints it": (
        D66_PAPER_FIRST_WORDING_AS_PRINTED, PAPER_FILE),
}


#: QUOTED SPANS IN DOCKET 68 CELLS THAT ARE NOT THE TREE'S WORDS, declared:
#: {span: why}.  Each is printed with its disclaimer beside it.
D68_NOT_QUOTES = {
    "it already exists everywhere": "combine.py's emended gloss of M's words (D23 note), "
                                    "printed as not M's",
    # ADDED (the W2 reproduction): the wave-2 seat's own superseded wording,
    # quoted as history beside 'first said'; neither is M's nor the charter's.
    "relocated to the probes and to two-way messages": "the wave-2 seat's own wording "
                                                       "(D23 note, O9), printed as history",
    "every wave-2 reading of outside art, each with its route": "the wave-2 seat's own "
                                                                "wording (M-D68-16), "
                                                                "printed as history",
    # ADDED (R-seat): the paper's first wording inside its DOCKET 66 marker,
    # which M-D68-26's cell prints READ back -- the paper's words (held and
    # checked against paper/CLAIMS.md), not the charter's or the rulings file's.
    D66_PAPER_FIRST_WORDING_AS_PRINTED: "the paper's own first wording inside its DOCKET 66 "
                                        "marker (M-D68-26), READ back from paper/CLAIMS.md",
}


def _d68_cells():
    """{site: text} -- every DOCKET 68 cell this file prints: O9, the notes,
    the rulings, the carried items and the pending question."""
    out = {"O9 claim": o9_claim(), "O9 answer": O9_ANSWERED_BY}
    out.update(("note " + k, v) for k, v in D68_NOTES.items())
    for r in (D68_RULED + D68_CARRIED + D68_FILE_CARRIED
              + [p for p in PENDING_RULINGS if p[0].startswith("M-D68")]):
        out.update(("%s col %d" % (r[0], i), c) for i, c in enumerate(r[1:], 1))
    # ADDED (W3S1B-seat): the OPEN list of section 8c.
    out.update(("W3S1B-OPEN %s col %d" % (r[0], i), c) for r in W3S1B_OPEN
               for i, c in enumerate(r[1:], 1))
    # ADDED (S1C-seat): the OPEN list of section 8d.
    out.update(("S1C-OPEN %s col %d" % (r[0], i), c) for r in S1C_OPEN for i, c in enumerate(r[1:], 1))
    out.update(("W4-OPEN %s col %d" % (r[0], i), c) for r in W4_OPEN for i, c in enumerate(r[1:], 1))
    out.update(("CMB-OPEN %s col %d" % (r[0], i), c) for r in CMB_OPEN for i, c in enumerate(r[1:], 1))
    out.update(("CMB2-OPEN %s col %d" % (r[0], i), c) for r in CMB2_OPEN for i, c in enumerate(r[1:], 1))
    out.update(("CMB3-OPEN %s col %d" % (r[0], i), c) for r in CMB3_OPEN for i, c in enumerate(r[1:], 1))
    return out


def d68_quote_faults(cells=None, rows=None):
    """[(site, span)] -- a quotation in a DOCKET 68 cell that is not the
    tree's own words: a double-quoted span in a ledger cell that is not EXACTLY
    a held text (_d68_held_texts), or any quoted span (double or single, with a
    space in it -- not a code token like 'Q-1') in a ledger cell or in
    index3.py's DOCKET 68 rows that does not occur verbatim in CHARTER.md or
    M-RULINGS-2026-10-03.md, unless D68_NOT_QUOTES declares it."""
    import index3
    cells = _d68_cells() if cells is None else cells
    rows = ([f for f in index3.FINDINGS if f[0].startswith("D68-")]
            if rows is None else rows)
    held = set(" ".join(v[0].split()) for v in _d68_held_texts().values())
    tree = ""
    for path in (D68_CHARTER_FILE, D68_RULINGS_FILE):
        with open(path, encoding="utf-8") as fh:
            tree += " " + _d68_norm(fh.read())
    dq = re.compile(r'"([^"]+)"')
    sq = re.compile(r"(?<![A-Za-z])'([^']+ [^']+)'(?![A-Za-z])")
    bad = []
    texts = [(k, " ".join(v.split())) for k, v in cells.items()]
    texts += [("index3 " + f[0], " ".join(f[5].split())) for f in rows]
    for site, t in texts:
        if not site.startswith("index3 "):
            bad += [(site, m) for m in dq.findall(t) if m not in held]
        for m in dq.findall(t) + sq.findall(t):
            if m not in tree and m not in D68_NOT_QUOTES:
                bad.append((site, m))
    return bad


def _d68_q1():
    """Q-1 and Q-1s as the instruments compute them: (measure.method_bits(),
    signed values at D68_Q1S_P, signed.separable_nullspace -- COMPUTED
    corroboration, signed.py's own word -- and signed.z3_obligations(), the
    machine-checked algebraic steps of signed.py section (4b))."""
    import random
    return (measure.method_bits(),
            (signed.re_h(D68_Q1S_P), signed.im_h(D68_Q1S_P), signed.neg(D68_Q1S_P),
             signed.mana(D68_Q1S_P)),
            signed.separable_nullspace(random.Random(5)),
            signed.z3_obligations())


D68_Q1 = _d68_q1()


def o9_claim():
    """O9's cell: the obstruction table, every verdict asked of combine.Screen;
    member-attributed removals first."""
    mb, (reh, imh, nneg, mana), sep, z3s = D68_Q1
    return (
        "THE TWO CLASSICAL BITS, AND WHAT ELSE STANDS (DOCKET 68: information "
        "without transit; combine.py, asked).  M's thesis, verbatim: \"%s\".  The "
        "question: %s  THE OBSTRUCTION TABLE, asked of combine.Screen at %s (z3; "
        "combine builds %s variants of M's seven hypotheses in every reading and "
        "screens them all in its own run, which this board does not repeat -- "
        "H-LEDGER-ASKS-REPRESENTATIVES).  MEMBER-ATTRIBUTED REMOVALS FIRST.  "
        "O-BITS under H-SETTLE W2 x H-FRAME F1: %s -- joint: alone, W2 gives %s "
        "and F1 gives %s.  At %s: W2 x F1 gives %s -- support 2 carries it; with "
        "H-12, %s.  SUPPORT 1 (N_EPS) ON THE READ LIMITS (wave 2, W2A-limits: the "
        "four Weinberg-family limits READ (abstract) at the publisher's public "
        "pages, each route recorded in settle.BOUNDS_WEINBERG, M-D68-16; "
        "settle.window_read, asked; window premises W_W2R = {%s}, named hypotheses "
        "only): %s.  combine's z3 support-1 route alone (its mutation "
        "support1-only) reads %s at 1 AU, N = 7 and %s at 1 AU, N = 1e3; its "
        "exact-rational window against settle's, disagreements at its four "
        "screened cells: %s.  An ADMISSIBLE window is not evidence of a drift: each limit "
        "is an upper bound measured consistent with zero.  WAVE 1 FIRST SAID "
        "(kept): support 1's window is empty from the NAMED-NOT-READ "
        "Weinberg-family value -- combine.cell_window_open = %s -- so it is OPEN "
        "via N_WREAD there, not LEFT; combine's HISTORY encoding wave6-WREAD "
        "reproduces it (%s).  "
        "O-BITS under clause 2b's D-CTC: %s, and there O-LOOP is reintroduced -- "
        "corridor O-LOOP %s, signal O-LOOP %s, where the board alone gives %s and "
        "%s.  A CTC is not shown to exist.  NOT-BOUND-IF, NOT REMOVALS, under "
        "H-IT as an information layer (ITB): O-MAKE-TOPO %s; O-HOLD %s; corridor "
        "O-LOOP %s; with R-INDEX, O-HOLD %s.  OPEN PATHWAYS AND NOT-BOUND-IF FROM "
        "THE OTHER READINGS, NONE A REMOVAL (B-combine.md section 5): H-SETTLE-KR "
        "(KR) O-HOLD %s; W1 x F1 O-BITS %s and KR x F1 O-BITS %s; H-IT as "
        "Jacobson emergent gravity (ITJ) O-HOLD %s; H-IT as ER=EPR (ITE) "
        "O-MAKE-TOPO %s; R-QUANTUM (RQ, M-D68-C5's second reading, beside "
        "R-INDEX's above) O-HOLD %s; and with ITB (ITB+RQ) O-MAKE-TOPO %s and "
        "O-HOLD %s -- R-QUANTUM's throat undoes ITB's non-binding (a premise "
        "clash on N_QTOPO, B-combine.md).  THE GEOMETRY'S O-LOOP, credited to "
        "no hypothesis: corridor O-LOOP %s on the board alone (exact FRW: "
        "frame.frw_time_function_lemma); with H-FRAME clause 1 alone (F1) %s, a "
        "member support beside the geometry's.  O-SEAT, the supply at the seat "
        "(O-MATTER relocated by M's ruling, M-D68-5): %s, under H-SEAT-S5, which "
        "M adopted (M-D68-7: \"S5 counts\"); given H-SEAT-ROUTES (S10 and S13 "
        "only, kept as the alternative on record) %s -- an obstruction until the "
        "seat's supply is shown, never removed by assertion.  Wave 2 asked it at "
        "Proxima (seat.py, W2C-seat): seat.grade_o_seat = %s; the D25 gate's binder "
        "at a CI-like body is %s, measured in no Proxima-system star or body in the "
        "sources read (seat.P_MEASURED_IN_PROXIMA_SYSTEM = %s), so the gate cannot "
        "be evaluated at its binder; N, the runner-up: %s (seat.proxima_measured's "
        "own words, as D25's note carries them; the wave-2 seat first printed only "
        "the clause before the first parenthesis, without the status).  O-MAKE in its "
        "distribution form (wave 2, vacuum.py, W2B-vacuum: N_VAC split, and retired "
        "to combine's history): vacuum.GRADES grades it LEFT-IF {%s} and OPEN "
        "outside that set via %s, none computed; combine screens it %s; given "
        "H-VAC-LEFTIF (the nine taken together) %s.  The distribution is relocated "
        "to the probes and to at least one classical message, not removed -- "
        "two-way (R9) in the two computed families; for R2's windows only >= 1 "
        "message is shown: the vacuum route's "
        "window-free floor is %.2f / %.2f L/c (midpoint / one end), against a "
        "midpoint pair source at %.2f L/c (D23's note).  The wave-2 seat first "
        "said 'relocated to the probes and to two-way messages', unscoped.  "
        "WAVE 1 FIRST SAID (kept): "
        "%s (as-of: combine's HISTORY encoding wave6-NVAC).  M's H-INFO-SHAPE "
        "removes nothing (O-SEAT %s "
        "under it: the board's pathway, not the hypothesis's).  THE MEASURE "
        "R-INDEX USES, computed.  Q-1 (measure.py): Baez-Fritz-Leinster's "
        "Theorem 2 verified on finite spaces; on The Method's closed index "
        "log2 %d = %.6f bits per cell of Lambda; measure.GRADES['Q-1'] = %s -- a "
        "measure counts and removes nothing.  Q-1s (signed.py), for a "
        "quasi-probability (sum p = 1, some p < 0): Re H = -sum p ln|p| "
        "(branch-free), Im H = pi N on the principal branch (N the total "
        "negative weight), M = ln sum|p| (product-additive, 0 exactly when no "
        "entry is negative); at p = %s, Re H = %.6f nats (negative, read and not "
        "explained away), Im H = %.6f = pi x %.1f, M = %.6f.  THE SEPARABLE "
        "CLAIM IS signed.py's SECTION (4b): over every continuous SEPARABLE "
        "functional X = sum g(p_i), BFL's functoriality, convex linearity and "
        "continuity carried to signed measures give X = c Re H + b N, under "
        "H-SEPARABLE, H-FINSIGNED and H-CONT-G.  Its algebraic steps are "
        "machine-checked by z3 (signed.z3_obligations, asked; 'unsat' = proved): "
        "g(0) = 0 %s, the Cauchy step %s (its control, one instance dropped, %s), "
        "the codomain consequence c = 0, b >= 0 %s; the solution identity and "
        "the product step by sympy; its analytic steps -- Cauchy under "
        "continuity and the log solution, signed.py's steps (4)-(6) -- are "
        "DERIVED by hand and READ as cited, not machine-checked.  "
        "signed.separable_nullspace CORROBORATES it and does not prove it (a "
        "null space of dimension %d in a %d-function basis, %d without the "
        "convex-linearity rows, the control).  Uniqueness over NON-separable "
        "functionals is OPEN (H-SEPARABLE names the gap); both weightings stay "
        "carried (M-D68-2, M-D68-8)"
        % (D68_THESIS, D68_QUESTION, combine.CELL_MAIN,
           format(D68_VARIANT_COUNT, ","),
           d68_asked("W2 x F1", "O-BITS"), d68_asked("H-SETTLE alone (W2)", "O-BITS"),
           d68_asked("H-FRAME clause 1 alone (F1)", "O-BITS"), combine.CELL_AU,
           d68_asked("W2 x F1", "O-BITS", au=True),
           d68_asked("W2 x F1 x H-12", "O-BITS", au=True),
           ", ".join(settle.W_W2R), "; ".join(c[3] for c in d68_w2_window_cells()),
           d68_verdict(D68_AU_SUPPORT1_ONLY), d68_verdict(D68_AU3_SUPPORT1_ONLY),
           d68_w2_windows_agree() or "none",
           combine.cell_window_open(combine.CELL_AU), d68_verdict(D68_AU_WAVE6_WREAD),
           d68_asked("clause 2b's D-CTC (F2b)", "O-BITS"),
           d68_asked("clause 2b's D-CTC (F2b)", "O-LOOP-C"),
           d68_asked("clause 2b's D-CTC (F2b)", "O-LOOP-S"),
           d68_asked("the board alone", "O-LOOP-C"), d68_asked("the board alone", "O-LOOP-S"),
           d68_asked("H-IT as an information layer (ITB)", "O-MAKE-TOPO"),
           d68_asked("H-IT as an information layer (ITB)", "O-HOLD"),
           d68_asked("H-IT as an information layer (ITB)", "O-LOOP-C"),
           d68_asked("ITB with R-INDEX", "O-HOLD"),
           d68_asked("H-SETTLE-KR alone (KR)", "O-HOLD"), d68_asked("W1 x F1", "O-BITS"),
           d68_asked("KR x F1", "O-BITS"),
           d68_asked("H-IT as Jacobson emergent gravity (ITJ)", "O-HOLD"),
           d68_asked("H-IT as ER=EPR (ITE)", "O-MAKE-TOPO"),
           d68_asked("R-QUANTUM alone (RQ)", "O-HOLD"),
           d68_asked("ITB with R-QUANTUM (ITB+RQ)", "O-MAKE-TOPO"),
           d68_asked("ITB with R-QUANTUM (ITB+RQ)", "O-HOLD"),
           d68_asked("the board alone", "O-LOOP-C"),
           d68_asked("H-FRAME clause 1 alone (F1)", "O-LOOP-C"),
           d68_uniform("O-SEAT"), d68_verdict(D68_SEAT_ROUTES),
           D68_SEAT["grade"], D68_SEAT["binder"][0], D68_SEAT["P in the system"],
           D68_SEAT["N alpha Cen"],
           ", ".join(d68_vac_grade()[0]), ", ".join(d68_vac_grade()[1]),
           d68_grouped("O-MAKE-DIST"), d68_grouped("O-MAKE-DIST", D68_VACLEFT_ASKED),
           D68_VAC["floor midpoint, one end (L/c)"][0], D68_VAC["floor midpoint, one end (L/c)"][1],
           D68_VAC["midpoint pair source (L/c)"], d68_grouped("O-MAKE-DIST", D68_NVAC_ASKED),
           d68_asked("H-INFO-SHAPE (SHAPE)", "O-SEAT"),
           mb["cells"], mb["bits_per_cell"], measure.GRADES["Q-1"]["verdict"],
           D68_Q1S_P, reh, imh, nneg, mana,
           z3s["z3_g0"], z3s["z3_cauchy"], z3s["z3_cauchy_control_drop_instance_b"],
           z3s["z3_codomain"],
           sep["null_dim"], len(sep["basis"]), sep["control_null_dim_without_CL_rows"]))


#: O9's answer AS WAVE 1 SEATED IT, kept as history and printed after wave 2's.
O9_ANSWERED_BY_AS_WAVE1 = (
    "D68 wave 2, in M's order (M-D68-10: \"1 then 2 then 3 then 4\"): the "
    "Weinberg-family limits READ at source (settles N_WREAD and the W_W2 flag on "
    "support 1); vacuum entanglement as pair supply (N_VAC); the S5 seat route "
    "(N_S5: S5's supply shown and the D25 gate holding at a destination).  "
    "Beyond wave 2: a measured state-dependent drift with a preferred slicing "
    "(W2 x F1's premises shown or refuted, support 2's field included); a CTC at "
    "Bob shown (N_DCTC); a READ source for what a non-geometric corridor costs "
    "(N_QTOPO, N_ILFREE).  O9 CLOSES only if a member removes O-BITS with no "
    "named premise (OPEN_ROW_READINGS)")

O9_ANSWERED_BY = (
    "D68 wave 2 (step 2 of M-D68-10) is RUN and seated (docstring section 7b): it "
    "READ the Weinberg-family limits (N_WREAD retired: %s), split N_VAC (retired: "
    "%s) and asked the S5 seat route at Proxima -- and closed nothing.  What "
    "would still answer: on support 1, H-MAP from the full texts of the papers "
    "(login wall, not read), H-SAME-EPS, H-ERRATUM and H-BEFRAC; support 2's window "
    "(N_W2ANC, UNEVALUATED); for O-MAKE-DIST, any of %s computed; for O-SEAT at "
    "a destination, the gate's binder (%s) measured in a body of the arrival "
    "aperture, accessible mass and the aperture, E_fab and m_set (S5's supply).  "
    "Beyond: a measured state-dependent drift with a preferred slicing (W2 x F1's "
    "premises shown or refuted); a CTC at Bob shown (N_DCTC); a READ source for "
    "what a non-geometric corridor costs (N_QTOPO, N_ILFREE).  ON M'S DOCKET 66 "
    "RULINGS: O-MAKE-TOPO is re-graded on M-D68-28 (%s) -- on the board alone %s, "
    "with RQ %s, under ITJ %s, and under ITB %s, never removed (combine.py, asked); "
    "what would answer it is N_WNCC, specthm's throat-creation class W-create-ncc "
    "shown nonempty (combine.OPEN_NAMED), and D68 wave 2's LEFT is combine's history "
    "encoding d68w2-topo (the board alone %s, asked).  spec.py's TURN reads any "
    "crossing on M-D68-27 (%s: %s adopted, defects.TURN_RULING, asked); it moves no "
    "D68 obstruction.  O9 CLOSES only if "
    "a member removes O-BITS with no named premise (OPEN_ROW_READINGS).  WAVE 1 "
    "FIRST SAID (kept): %s"
    % ("N_WREAD" in combine.HISTORY_OPEN, "N_VAC" in combine.HISTORY_OPEN,
       ", ".join(d68_vac_grade()[1]), D68_SEAT["binder"][0],
       d68_words("M-D68-28"), d68_asked("the board alone", "O-MAKE-TOPO"),
       d68_asked("R-QUANTUM alone (RQ)", "O-MAKE-TOPO"),
       d68_asked("H-IT as Jacobson emergent gravity (ITJ)", "O-MAKE-TOPO"),
       d68_asked("H-IT as an information layer (ITB)", "O-MAKE-TOPO"),
       d68_verdict(D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]),
       d68_words("M-D68-27"), D66_TURN["ruling"]["adopted"], O9_ANSWERED_BY_AS_WAVE1))



# ----- O9's DOCKET 66 part (docstring section 8) ----------------------------
# Appended to O9's cell AFTER DOCKET 68's (o9_claim() and O9_ANSWERED_BY are
# DOCKET 68's and are kept exactly; the row is their concatenation with the
# two below).  Every verdict asked of combine66.D66Screen (D66_ASKED); every
# census figure READ from B-combine66.md (D66_CENSUS).
def d66_o9_part():
    """O9's DOCKET 66 part: member-attributed first, then the OPEN pathways
    the D66 readings add, the interference, the defeasibility, the seat
    condition, the readings on record, the finding for the D68 board, and D66
    wave 1's words kept."""
    v, lb = D66_CENSUS["variants"], D66_CENSUS["load-bearing"]
    cons = D66_CENSUS["conservative"]
    retired = "; ".join("%s (%s)" % (k, combine66.RETIRED[k].split(".  D66-fix: ")[0].replace(
        "wave 1: ", "wave 1 said ")) for k in sorted(combine66.RETIRED))
    return (
        "  DOCKET 66, WAVE 1 (seated in this form: docstring section 8; combine66.py runs "
        "combine.py's engine with DOCKET 66's commitments as tracked constraints, z3, asked "
        "here on %d named variants at %s and %d at %s -- its full screen of %s + %s variants "
        "at 1 ly and %s + %s at 1 AU is its own, READ from B-combine66.md: "
        "H-LEDGER-ASKS-REPRESENTATIVES).  M's hypotheses, carried as hypotheses: "
        "H-DEFECT-SEAT (a topological defect as a seat, M-S1A-P3 (ii)), H-THROAT-BITS (the "
        "throat compressed to binary information, M-S1A-P3 (i) with M's clarification), "
        "H-QET-EXOTIC (M-D65-1).  MEMBER-ATTRIBUTED FIRST: a D66 literal is load-bearing in "
        "a removal or non-binding in %s of the variants asked (combine66.d66_attributed); "
        "the full screen reports %s in %s consistent variants at 1 ly and %s in %s at 1 AU "
        "(READ).  The member removal stays D68's: a static string seat with W2 x F1 gives "
        "O-BITS %s, and at 1 AU %s.  R-LIT (the question's parenthetical read as arrival "
        "alone) is %s; with W2 x F1 it is consistent by the absence of a refutation and "
        "sits in O-BITS supports only by entailing W2 (in a support and load-bearing "
        "nowhere: %s).  WHAT THE D66 READINGS ADD IS OPEN PATHWAYS, NONE A REMOVAL.  "
        "O-SEAT: %s; otherwise %s.  O-HOLD: %s; QET's pathway is N_QETHAD alone, N_XI and "
        "N_QEIC being the board's (QET with RQ: %s); together, DTHR with TBHOLO %s, DTHR "
        "with QET %s and TBTEL with QET %s -- a union of pathways, none closing another's "
        "gap.  O-MAKE-TOPO: %s -- M's ruling M-S1A-P3 applied to every D66 geometric throat "
        "(a singular throat is not disqualified; the throat-creation classes stay OPEN).  "
        "INTERFERENCE: beside ITB a D66 throat makes N_QTOPO a premise clash, so ITB's "
        "non-bindings fall: DTHR with ITB gives O-MAKE-TOPO %s and O-HOLD %s; TBHOLO with "
        "ITB, O-HOLD %s; R-ITB carries ITB's own, O-HOLD %s.  DEFEASIBLE ONLY THROUGH A "
        "HELD STRING-SUPPORTED THROAT (FKZ: unbalanced mouths in one space make a time "
        "machine): DTHR's removals defeasible %s, its seat %s.  THE SEAT CONDITION M-S1A-P3 "
        "(i): %s; the texture %s, with {%s} a premise clash -- under H-SEAT-PERSISTS a "
        "texture is an event, not a seat (A1); VIOLATED in no variant asked, and in no "
        "consistent variant of the full screen (READ).  READING ON RECORD: H-SEAT-ROUTES on a string seat, O-SEAT %s.  "
        "THE D68 BOARD, RE-GRADED ON M'S RULING (M-D68-28, %s): M-S1A-P3 now reaches D68's "
        "own throats in combine.py itself -- the board alone O-MAKE-TOPO %s and with RQ %s "
        "(combine.py, asked), as combine66's reading singok-board gives (%s; %s), and D68 wave "
        "2's LEFT is combine's history encoding d68w2-topo (the board alone %s, RQ %s, asked).  "
        "The moved variants are combine66's census, READ and not asked here: %s moved, %s of "
        "them context-only (B-combine66.md), the contexts D68's own census names as %s "
        "(B-combine.md section 0); this board asks the board alone and RQ only.  FIRST SAID "
        "(D66-seat, kept; its verdicts re-asked of the history encoding): RECORDED FOR THE "
        "D68 BOARD, NOT REPAIRED: M-S1A-P3 read as a board ruling reaching "
        "D68's own throats (combine66's reading singok-board) gives the board alone "
        "O-MAKE-TOPO %s and with RQ %s, where combine.py gives %s and %s; combine66 cannot "
        "change D68 rows (its conservative-extension rule), and whether combine.py "
        "re-grades is the D68 board's (B-combine66.md section 9, finding 8).  The extended "
        "screen with no D66 literal against combine.py's board alone, obstructions that "
        "differ: %s; combine66's full conservative-extension run: %s compared, %s differ "
        "(READ).  D66 WAVE 1 FIRST SAID (kept; asked of combine66's history encodings): M's "
        "singular-throat ruling credited to TBHOLO and TBTSH only (singok-a2: DTHR's "
        "O-MAKE-TOPO %s); QET's hold gated through the board's pathways too "
        "(qet-board-paths: QET's O-HOLD %s); and two pathways since retired "
        "(combine66.RETIRED): %s"
        % (len(D66_VARIANTS), combine.CELL_MAIN, len(D66_VARIANTS_AU), combine.CELL_AU,
           v[0], v[1], v[2], v[3],
           "none" if not d66_load_bearing() else d66_load_bearing(),
           lb[0], lb[1], lb[2], lb[3],
           d66_asked("DSTR with W2 x F1", "O-BITS"),
           d66_asked("DSTR with W2 x F1", "O-BITS", au=True),
           d66_asked("H-QET-EXOTIC: R-LIT (QLIT)", "O-BITS"),
           ", ".join(d66_in_support_only()) or "none",
           d66_group(D66_DEFECT_SEATS, "O-SEAT"),
           d66_group([k for k, _p in D66_VARIANTS[6:13]], "O-SEAT"),
           d66_group([k for k, _p in D66_VARIANTS[6:13]], "O-HOLD"),
           d66_asked("QET with R-QUANTUM (RQ)", "O-HOLD"),
           d66_asked("DTHR with TBHOLO", "O-HOLD"), d66_asked("DTHR with QET", "O-HOLD"),
           d66_asked("TBTEL with QET", "O-HOLD"),
           d66_group([k for k, _p in D66_VARIANTS[6:13]], "O-MAKE-TOPO"),
           d66_asked("DTHR with ITB", "O-MAKE-TOPO"), d66_asked("DTHR with ITB", "O-HOLD"),
           d66_asked("TBHOLO with ITB", "O-HOLD"),
           d66_asked("H-THROAT-BITS: R-ITB with ITB (TBITB)", "O-HOLD"),
           "; ".join("%s via %s" % (o, ", ".join(p)) for o, p in sorted(
               d66_defeasible("H-DEFECT-SEAT: string-supported throat (DTHR)").items())) or "nowhere",
           d66_seat("H-DEFECT-SEAT: string-supported throat (DTHR)"),
           d66_group([k for k, _p in D66_VARIANTS[1:13] if "(DTEX)" not in k], "SEAT"),
           d66_seat("H-DEFECT-SEAT: texture seat (DTEX)"),
           "; ".join(", ".join(c) for c in
                     D66_ASKED["H-DEFECT-SEAT: texture seat (DTEX)"]["premise_clash_named"]),
           d66_asked("H-SEAT-ROUTES on DSTR", "O-SEAT", reading=True),
           d68_words("M-D68-28"),
           d68_asked("the board alone", "O-MAKE-TOPO"), d68_asked("R-QUANTUM alone (RQ)", "O-MAKE-TOPO"),
           d66_asked("singok-board on the board alone", "O-MAKE-TOPO", reading=True),
           d66_asked("singok-board with RQ", "O-MAKE-TOPO", reading=True),
           d68_verdict(D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]),
           d68_verdict(D68_TOPO_W2_ASKED["R-QUANTUM alone (RQ)"]["per"]["O-MAKE-TOPO"]),
           D66_TOPO_READ["d68w2-topo"][0], D66_TOPO_READ["d68w2-topo"][1],
           D68_TOPO_CENSUS["contexts"][2],
           d66_asked("singok-board on the board alone", "O-MAKE-TOPO", reading=True),
           d66_asked("singok-board with RQ", "O-MAKE-TOPO", reading=True),
           d68_verdict(D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]),
           d68_verdict(D68_TOPO_W2_ASKED["R-QUANTUM alone (RQ)"]["per"]["O-MAKE-TOPO"]),
           d66_d68_board_agrees() or "none", cons[0], cons[1],
           d66_asked("singok-a2 on DTHR (D66 wave 1's encoding)", "O-MAKE-TOPO", reading=True),
           d66_asked("qet-board-paths on QET (D66 wave 1's encoding)", "O-HOLD", reading=True),
           retired))


def d66_o9_answer():
    """O9's DOCKET 66 answer: what would answer the D66 OPEN pathways, asked."""
    mm = D66_FIG
    return (
        "  DOCKET 66 (wave 1, seated) closes nothing on O9 and opens no route that removes "
        "anything: what would answer its OPEN pathways, none shown realised -- %s "
        "(combine66.D66_OPEN, asked).  For N_GJWPAY, Maldacena-Milekhin-Popov's held "
        "one-space throat is computed and does not admit the payload (throatbits.mmp_scales, "
        "H-MMP-OOM: its binding energy equals the payload's rest energy only at r_e <= %s m, "
        "below l_P = %s m; at r_fit it needs N_f >= %s to %s massless charged species); for "
        "N_QETHAD, H-QET-HADAMARD's short check, not run; N_QLITNL, arrival-alone energy "
        "under a non-linear dynamics, a candidate computed nowhere.  THE TURN READING, RULED BY "
        "M (M-D68-27, %s): %s adopted, %s kept as the alternative on record "
        "(defects.TURN_RULING, asked); the straight string TURNs, its rays crossing at L = %.0f "
        "AU for b = R_sun at the Planck Nambu-Goto bound (defects.string_turn, asked), and no "
        "obstruction on this board moves.  FIRST CARRIED HERE AS A QUESTION FOR M (A1's since "
        "D66 wave 1, not seated as pending; kept): %s.  Why: %s.  Proposed: %s.  Waiting on it: "
        "%s.  O9 still CLOSES only on O-BITS with no named premise, in a D68 or a D66 variant "
        "asked (OPEN_ROW_READINGS)"
        % ((", ".join(sorted(combine66.D66_OPEN)),
           _d66_e(mm["MMP binding = payload at r_e (max), l_P"][0]),
           _d66_e(mm["MMP binding = payload at r_e (max), l_P"][1]),
           _d66_e(mm["MMP N_f at r_fit (species count)"][0], 2),
           _d66_e(mm["MMP N_f at r_fit (species count)"][1], 2),
           d68_words("M-D68-27"), D66_TURN["ruling"]["adopted"],
           D66_TURN["ruling"]["alternative on record"], D66_TURN["L AU"])
           + d66_turn_question()))


D66_O9_PART = d66_o9_part()
D66_O9_ANSWER = d66_o9_answer()


def d66_o_bits_removed_outright():
    """[variant] among the DOCKET 66 variants asked (both cells) where
    combine66 says O-BITS is REMOVED with no named premise -- [] while every
    removal is REMOVED-IF."""
    out = []
    for lab, asked in (("D66 ", D66_ASKED), ("D66 1 AU: ", D66_ASKED_AU)):
        for k, r in asked.items():
            if r["consistent"] and "O-BITS" in combine.counts(r, ("REMOVED",)):
                out.append(lab + k)
    return out


def o9_removed_outright():
    """What closing O9 would need, over DOCKET 68's and DOCKET 66's asked
    variants (d68_o_bits_removed_outright + d66_o_bits_removed_outright)."""
    return d68_o_bits_removed_outright() + d66_o_bits_removed_outright()


OPEN_ROWS += [("O9", o9_claim() + D66_O9_PART, O9_ANSWERED_BY + D66_O9_ANSWER,
               ("combine", "counts"))]

#: WHAT AN O ROW'S OWNER SAYS ABOUT CLOSING, where no owner pins a flag.  O9's
#: owner, combine.py, pins no O9_CLOSED; what would close O9 is ASKED of it:
#: O-BITS REMOVED with no named premise in an asked variant.  (row id ->
#: (what is asked, the asking function)).  A row not named here is asked by
#: its owner's flag, as before.
OPEN_ROW_READINGS = {
    "O9": ("combine.counts(<each asked variant>, ('REMOVED',)) holding O-BITS -- "
           "DOCKET 68's variants and, since DOCKET 66's seating, combine66's",
           o9_removed_outright),
}


def open_row_answer(r):
    """(what was asked, its value) for an O row's closing: its owner's flag,
    or for a row in OPEN_ROW_READINGS the owner's computed reading."""
    if r[0] in OPEN_ROW_READINGS:
        lab, fn = OPEN_ROW_READINGS[r[0]]
        return lab, fn()
    return "%s.%s" % (r[3][0], r[3][1]), ask(r[3])

#: THE WORDING DOCKETS 62 AND 64 REPLACED.  (row id, the docket that replaced
#: it, the wording as it stood -- claim, then what would answer it -- and why it
#: was replaced.)  KEYED BY (row, docket): O5 was narrowed twice, and both of
#: its earlier wordings are kept.  KEPT, NEVER DELETED: a row rewritten in
#: place is otherwise indistinguishable from one that always said the new
#: thing, and three of DOCKET 62's five said something now refuted.
SUPERSEDED_WORDING = [
    ("O5", "DOCKET 62",
     "Does a self-consistent static semiclassical solution with m(r) < 0 exist "
     "at all?  Fewster & Teo bound the NORMAL-ORDERED density relative to the "
     "static vacuum, so the bound is on rho_ren - rho_vac and not on rho_ren "
     "|| a self-consistent solve of G_ab = 8 pi <T_ab> on the negative-mass "
     "corridor, rather than a bound evaluated on an assumed background",
     "true of Fewster & Teo and NOT a limit on QEIs: " +
     throatmass.NARROWING_3_STATUS + "; the answering solve is now named "
     "exactly (HPS's system, regular-centre data)"),
    ("O6", "DOCKET 62",
     "THE BRANE-BULK TRANSDUCER.  DOCKET 61's intersection is structurally "
     "intact -- the two refusals genuinely cancel -- and dies on a coupling: "
     "neither GKLP paper states a coupling constant, a source model or an "
     "emission rate, and 2208.09014 has none in sixteen pages.  DOCKET 57's "
     "confinement ruling forces the available bulk fields to be gravitational "
     "|| a transducer that writes a specification into a bulk mode at one end "
     "and reads it at the other with brane-confined apparatus.  The "
     "energy-per-bit estimate spans 50 ORDERS AND STRADDLES ZERO, so its SIGN "
     "is unsettled and no figure may be seated from it",
     "the cause of death is REFUTED -- true of the two papers read, false of "
     "the literature: " + branelink.COUPLING_SOURCE),
    ("O7", "DOCKET 62",
     "OUR OWN BOOST RELATIVE TO THE PREFERRED BRANE FRAME.  The bulk saving is "
     "Delta_tau = (L/Gamma^2)[1/(1-B) - 1/(gamma-B)]: 94 ns at B ~ 0, and THE "
     "FULL LIGHT TIME as B approaches 1/beta.  B cannot be purchased, because "
     "buying it means boosting the fabricator out of the destination's rest "
     "frame and forfeiting the destination-supplied atoms that are the premise "
     "|| a measurement of Earth's velocity relative to the preferred brane "
     "frame, if one exists.  The only preferred-frame velocity ever measured "
     "is the CMB dipole at 370 km/s, Gamma - 1 = 7.6e-7, which is what gives "
     "94 ns",
     "WRONG PROVENANCE: the saving at B = 0 is " + branelink.PROVENANCE_94NS +
     "; the dipole is a candidate for B, not the source of the figure.  "
     "DOCKET 67: 'the only preferred-frame velocity ever measured' also "
     "overstated -- the CMB frame is a candidate preferred brane frame, and "
     "reading the dipole as a velocity assumes it is purely kinematic"),
    ("O2", "DOCKET 62",
     "Fewster & Teo give an EXACT static-spacetime QEI with no curvature cap, "
     "TIGHTER than Ford-Roman in the Minkowski limit, and the corridor is "
     "genuinely static so the class is right.  It has never been evaluated on "
     "the corridor || evaluate it once the corridor's scalar mode functions "
     "are determined -- the authors' own conclusion asks for exactly this for "
     "the static Morris-Thorne wormhole",
     "'TIGHTER' invited a void adjustment to C_F, which already IS the "
     "Fewster-Teo constant at the optimal sampler; the mode functions it "
     "waits on are NOT-FOUND; and the right instrument is Fewster & Smith's "
     "ABSOLUTE QEI"),
    ("O3", "DOCKET 62",
     "Whether ANY braneworld shortcut yields a closed timelike curve.  Every "
     "published 'no' is a one-extra-dimension or flat-bulk result; the single "
     "'yes' needs two extra dimensions and two inequivalent preferred frames "
     "|| a general result at codimension two, or an explicit CTC at "
     "codimension one.  The split in the literature tracks codimension and "
     "nobody has closed it",
     "an explicit codimension-one CTC is no longer enough -- a hand-written "
     "metric answers nothing -- and the flat-bulk 'no' is now a THEOREM (D21), "
     "forced rather than contingent"),
    # ----- DOCKET 64.  O5's DOCKET 62 wording, and the two demand rows whose
    # wording DOCKET 64 replaced rather than extended (D24's claim, D25 and O2
    # were only appended to, so nothing of theirs was replaced). -------------
    ("O5", "DOCKET 64",
     O5_DOCKET62[0] + " || " + O5_DOCKET62[1],
     "the question is narrowed to the ESTABLISHED domain: m < 0 is found in "
     "HPS's own conserved system (hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM = "
     "%s), outside the domain the AHS approximation is established for.  "
     "throatmass.py's NOT-FOUND describes what HPS REPORTED and stays true "
     "of that, but is no longer printed as the tree's finding; the row is "
     "re-owned to hpscentre.O5_CLOSED.  DOCKET 67, of the kept wording: "
     "'the largest ever built' is the tree's survey hypothesis -- HPS's 300 "
     "l_P throats are 'local' solutions with horizons far from the throat, "
     "not shown, and HPS say throats can be arbitrarily large; and "
     "'EXPELLED ... names no hypothesis to attack' is wrong of AMM, whose "
     "failure names a growing gauge-invariant mode, and eps ~ 1 lies "
     "outside Flanagan-Wald's theorem, not shown outside semiclassical "
     "gravity"
     % hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM),
    ("D22", "DOCKET 64", D22_DOCKET62,
     "the smeared price is computed in flat space (noise.py: C1 a THEOREM in "
     "H1-H6) and reaches the corridor only as a SURVEY, so the row moves OPEN "
     "-> SURVEY; 'needs the curved-space renormalisation of quartic operator "
     "products' is wrong as to NEW renormalisation for the TIME-smeared "
     "variance (Hu & Verdaguer 3.2, READ, for the counterterm cancellation "
     "and separated-point finiteness), and the finiteness it does need is "
     "NAMED, not run (Fewster 1208.5399 Sec. 3.3); "
     "fluctuation.PRICES_THE_CORRIDOR stays False and stays true of "
     "fluctuation.py.  DOCKET 67, of the kept wording: 'every demand row is a "
     "demand on <rho>' is exact only at alpha = beta = 0; Kuo & Ford propose "
     "Delta as 'a measure', not the equation's error; and their 1993 remark "
     "concerns pointwise normal-ordered quartics (renormalised since: "
     "Hollands-Wald 2001), which they exempt from averaged quantities"),
    ("D24", "DOCKET 64", D24_ANSWER_DOCKET62,
     "the third part -- the passage from flat space to a configuration that "
     "changes no topology -- is priced by formation.py (F1, F2), so 'no "
     "instrument in the tree does that yet' is no longer true; the row is "
     "re-owned to formation.NUCLEATION_PRICEABLE_FROM_SOURCE"),
    # ----- DOCKET 65.  S5's first sentence, replaced in place when S11-S13
    # were seated: S5 was the only priced row and is no longer. ------------
    ("S5", "DOCKET 65",
     "THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL",
     "S11-S13, DOCKET 65's priced remainders, are priced OPEN rows too"),
]


def superseded_dockets(table=None):
    """'62, 64 and 65': the dockets SUPERSEDED_WORDING names, built from the
    table, for the section header."""
    table = SUPERSEDED_WORDING if table is None else table
    ns = sorted(set(int(r[1].split()[1]) for r in table))
    return (", ".join(str(n) for n in ns[:-1]) + " and " + str(ns[-1])
            if len(ns) > 1 else str(ns[0]))

# ---------------------------------------------------------------------------
# WHAT WAS OPEN AND IS NOW ANSWERED.  KEPT, NEVER DELETED, for the reason the
# withdrawn rows are kept: an open question that closes and leaves no trace is
# indistinguishable from one nobody ever asked.
# ---------------------------------------------------------------------------

CLOSED_ROWS = [
    ("O4",
     "Does the contraction criterion survive the change from a CENTRE to an "
     "AXIS?  The priced object cannot have a destination (D14) and a corridor "
     "has an axis; the static cylindrical throat was unpriced in any geometry",
     "CLOSED, AND THE AXIS DOES NOT ESCAPE THE SIGN.  axial.py, six sympy "
     "residuals all 0.  In the Lambda = 0 gauge -- a FULL gauge fixing -- "
     "8 pi u W = -(W Psi')' - W Psi'^2 - W''.  On a regular axis (W(0) = 0, "
     "W'(0) = 1, phi of period 2 pi, W Psi' -> 0 at r = 0) and asymptotically "
     "flat in axial.py's sense (W -> r, so W' -> 1 -- no angular deficit at "
     "infinity -- and W Psi' -> 0) both boundary "
     "terms vanish and INT 8 pi u W dr = -INT W Psi'^2 dr <= 0, with equality "
     "IFF Psi' == 0.  ANY axial contraction forces u < 0 somewhere -- in that "
     "class, where u >= 0 everywhere already forces u == 0 and W == r with or "
     "without contraction, so the sign is carried by the boundary conditions; "
     "with string asymptotics (W' -> k < 1) a contracting profile with u >= 0 "
     "everywhere exists (CORRECTED, DOCKET 67: these were unstated).  NO ENERGY "
     "CONDITION IS USED -- geometry and two boundary conditions.  Phi is absent "
     "from u, so redshift buys nothing, which closes the S - 2u escape that "
     "looked real for one pass.  Same shape as certify.py's: a square carrying "
     "a minus sign, here -W Psi'^2 under an integral.  The one term with the "
     "other sign is a conical ANGLE EXCESS, W'(0) > 1, contributing exactly "
     "(W'(0) - 1) -- measured to nine places at four defects -- and an angle "
     "excess is the deficit of a NEGATIVE linear mass density, so it restates "
     "the requirement rather than avoiding it -- for a string with W Psi' -> 0 "
     "at the axis, axial pressure p = -mu at first order (Vilenkin's deficit "
     "is 4 pi G (mu - p); with p > mu an excess needs no negative mu, outside "
     "the class -- DOCKET 67)"),
    ("O1",
     "The nonminimally coupled scalar admits no state-independent QEI, so the "
     "sharpest limb of DOCKET 55 has a hole exactly where the project's "
     "most-favoured route sits",
     "CLOSED, AND REFUSED.  Both answers the row itself named are supplied, "
     "and it was S4 counted a second time -- this file's own note very nearly "
     "said so.  The compensating positive energy IS the enclosed-mass problem "
     "returning: E_pos/|E_neg| = 3 pi/(32 f xi c0^3) >= 1039.13 at xi = 1/4 "
     "and >= 1803.55 at xi = 1/6, from Fewster & Osterbrink's own "
     "construction.  LAMBDA CANCELS AND L CANCELS -- the overhead is a PURE "
     "NUMBER, which is WORSE than a power law: a growing penalty could in "
     "principle be outrun by building small, and a scale-free factor of 10^3 "
     "cannot be outrun at all.  CORRECTED (DOCKET 67): neither the formula "
     "nor the two figures is in Fewster & Osterbrink, and f and c0 were "
     "defined nowhere.  They are this tree's accounting on FO's one-particle "
     "family (massless field, 4D Minkowski, xi in (0, 1/4]): f a threshold as "
     "a fraction of the peak |rho(0,0)|, c0 the radius of the largest FO ball "
     "on which rho <= -f|rho(0,0)|, E_neg that threshold times the ball's "
     "volume, E_pos = <H>, minimised over f.  Against the same state's "
     "actual integrated negative energy the ratio is 22.79 and 102.02 "
     "respectively.  'Cannot be outrun' holds of that one family: FO prove "
     "no bound on <H>/|E_neg| over all states.  The refusal rests on S4's EFT "
     "field cutoff, not on these figures"),
]


# ---------------------------------------------------------------------------
# WHAT THIS PROJECT ASSERTED AND THEN REFUTED.  Kept, never deleted.
# ---------------------------------------------------------------------------

WITHDRAWN_ROWS = [
    ("W1", "achievable.py: the census is 'bounded by a THEOREM', and the core "
     "falls short by sixty-five orders",
     "Ford-Roman is a TIME average at ONE SPATIAL POINT, not a cap on |rho| "
     "over a spatial scale.  There is no pointwise cap to price against, and "
     "the figure was computed with the inequality's own coefficient dropped.  "
     "CORRECTED (DOCKET 67): 'no pointwise cap' holds for a general state; "
     "for a STATIC density the time average is the point value, so in flat "
     "space the inequality forces rho >= 0, and with the window capped by a "
     "spatial scale it gives Fewster's -C/(2l)^4 -- the one-sided cap "
     "achievable.duration_bound and bounds.py already apply (D7)"),

    ("W2", "bounds.py: 'Casimir is the Ford-Roman bound saturated, not an "
     "exception to it, which is why no material choice crosses it'",
     "Fewster reports the Casimir density at 3-7 %% of the bound and asks in "
     "print why it is so small a proportion.  Three per cent is not a wall "
     "with something standing against it.  (DOCKET 67, of the words above: "
     "'the Casimir density' is the massless minimally coupled Dirichlet "
     "scalar's -- the EM ideal-plate density, under an unread H_EM, is "
     "0.432 %% of the scalar bound at the midpoint -- and the withdrawn "
     "claim's 'the Ford-Roman bound' is Fewster's Eq. (4) relabelled.)  "
     "DOCKET 67 "
     "(ford-roman-qi-and-fewster-casimir-fraction, NARROWED; the reopen "
     "adjudicated REOPENS-NARROWER; recorded on M's ruling of 2026-10-02): "
     "the 3-7 %% is of Fewster's own a priori Eq. (4) bound, not of the "
     "Ford-Roman or the sharp bound.  W2 stays WITHDRAWN on four carried "
     "counts: (i) saturation of Fewster's own bound, %.4f %% to %.4f %%; (ii) "
     "saturation across the slab of any -K/(2l)^4 bound (the profile does not "
     "depend on K and falls by %.3f from midplane to plates); (iii) 'not an "
     "exception' against the uncapped Ford-Roman Eq. (1), which a static "
     "negative density violates above the cap; (iv) 'known saturated' (K = 0 "
     "stays wrong: an OPEN saturation is 'not known').  ONE READING OF THE "
     "PREMISE IS %s, NOT REFUTED: whether the Casimir midplane density of the "
     "massless minimally coupled Dirichlet scalar saturates the unknown SHARP "
     "a priori bound -C_s/(2l)^4 -- bracket %.2f %% to 100 %%, where 100 %% "
     "needs C_s = %.6f = C/%.3f and Fewster's locality step via %s "
     "(bounds.sharp_bound_reading()).  Saturation in Ford-Roman's capped sense, "
     "for that profile: %s (where computed, for the periodic scalar, equality "
     "at the cap holds by construction, evidence neither way).  'Which is why "
     "no material choice crosses it' is NOT reinstated, and nothing anti-warp "
     "comes back" % (100 * bounds.sharp_bound_reading()["plate"],
             100 * bounds.sharp_bound_reading()["bracket"][0],
             bounds.sharp_bound_reading()["spread_mid_over_plate"],
             bounds.SHARP_BOUND_MIDPLANE_SATURATION,
             100 * bounds.sharp_bound_reading()["bracket"][0],
             bounds.sharp_bound_reading()["C_s"],
             bounds.sharp_bound_reading()["C_over_C_s"],
             bounds.FEWSTER_LOCALITY_STEP.replace("Fewster's ref. [31], ", "ref. [31], "),
             bounds.CAPPED_SENSE_SATURATION_DIRICHLET)),

    ("W3", "tolman.py: 'p_r is a SCALAR under H'",
     "It is DETERMINED BY a scalar and is not one.  A boost witness turns the "
     "tension into a pressure at the same event while 1 - 2m/R does not move"),

    ("W4", "tolman.py: Phi' = 0 is an exactness route, and the class is smaller",
     "Under the computed G^r_r it forces 4 pi r^3 p_r = -m, which with the "
     "identity gives m == 0.  It does not restrict the class, it EMPTIES it"),

    ("W5", "tolman.py: the regular-centre hypothesis here and DOCKET 52's are "
     "'one fact seen twice'",
     "A separating witness holds certify.py's m(0) = 0 while C = 4 pi A != 0.  "
     "Two hypotheses, not one"),

    ("W6", "the corridor shortfall is 18.5 orders",
     "That figure is vacuumcorridor.py's ratio of two POSITIVE masses answering "
     "a domain-of-validity question.  It is not a supply against a demand, and "
     "quoting it understated the real shortfall by 52.1 orders"),
    ("W7", "DOCKET 61 pass A: the directional crack is closed by observation, "
     "because at Gamma = 1.89e6 the GKLP forward direction is supercritical",
     "ARITHMETICALLY WRONG BY A FACTOR OF 14.1.  Supercriticality needs "
     "Gamma >= 1/beta = 2.6726124e7, and 1.894565e6 is SUBcritical.  The crack "
     "is closed instead by a sky-fraction coincidence of prior 2.6e-7 plus an "
     "unmeasured cosmological boost -- a residual, recorded as one, not a "
     "proof"),

    ("W8", "DOCKET 61 pass D: the unbounded saving needs endpoints in common "
     "relativistic motion while the route needs the receiver at rest in the "
     "destination's atoms, so the two premises are jointly unsatisfiable",
     "B is the COMMON boost of both endpoints relative to the PREFERRED BRANE "
     "FRAME, not relative to Proxima.  Earth and Proxima are comoving to about "
     "one part in 1e4, so a receiver at rest in Proxima's atoms automatically "
     "shares Earth's B whatever B is.  No contradiction, and the closure does "
     "not stand.  CORRECTED (DOCKET 67): 'about one part in 1e4' is a "
     "seasonal range, beta_rel = 3.6e-5 to 2.08e-4 (Gaia DR3 astrometry and "
     "Kervella 2017's radial velocity, read via restatement, with Earth's "
     "orbit); and 'shares B' holds multiplicatively -- the Doppler and "
     "Lorentz factors of any common boost agree between the endpoints to "
     "within e^(+-2.1e-4) -- not for B as a velocity when B is comparable to "
     "beta_rel (8.1 % apart at the CMB-dipole speed).  The closure still "
     "does not stand"),

    # DOCKET 63.  ASKED, NOT RETYPED: W9 is excite.W9 and W10-W13 are
    # address.WITHDRAWN, each a (claim, why) whose figures are computed there.
    ("W9", "DOCKET 63: " + excite.W9[0],
     "; ".join(excite.W9[1])),
] + [(k, address.WITHDRAWN[k][0], address.WITHDRAWN[k][1])
     for k in ("W10", "W11", "W12", "W13")]


def _one_line(text, width):
    """First `width` characters of `text`, on one line, with an ellipsis if cut.

    NOT text.split(".")[0].  That was the first draft and it amputated every
    sentence containing a module name -- "certify.py's COROLLARY ..." printed as
    "certify".  A report that silently truncates at a full stop is unreadable
    exactly where this tree's prose is most specific.
    """
    t = " ".join(text.split())
    return t if len(t) <= width else t[:width - 3] + "..."


def ask(owner):
    """Fetch a row's pinned value from the module that owns it.

    THE WHOLE DISCIPLINE OF THIS FILE IS IN THIS FUNCTION.  A row with an owner
    is not believed, it is asked, every run.  A row whose owner has dropped the
    attribute raises rather than defaulting, because a silently absent pin is
    how `achievable.py`'s figure survived as long as it did.
    """
    if owner is None:
        return None
    mod, attr = owner
    m = sys.modules[mod]
    if not hasattr(m, attr):
        raise AttributeError("%s no longer pins %s -- ledger row is stale"
                             % (mod, attr))
    return getattr(m, attr)


def unaskable():
    """Rows this file cannot ask, because their owner is a paper.

    COUNTED AND NAMED RATHER THAN HIDDEN.  A row backed by a citation is not
    worse than one backed by a module, but it is defended differently, and a
    reader is owed the count.
    """
    return tuple(r[0] for r in DEMAND if r[3] is None)


def open_demand():
    """DEMAND rows whose status is OPEN.  Counted once, as demand, by
    statuses(); listed again beside the O rows so the open section shows
    every open question and not only the ones filed under an O."""
    return [r for r in DEMAND if r[2] == OPEN]


def statuses():
    """The status census over both sides plus the open and withdrawn rows."""
    c = dict((s, 0) for s in STATUSES)
    for r in DEMAND:
        c[r[2]] += 1
    for r in SUPPLY:
        c[r[2]] += 1
    c[OPEN] += len(OPEN_ROWS)
    c[WITHDRAWN] += len(WITHDRAWN_ROWS)
    # A CLOSED row counts as REFUSED, not as OPEN.  O1 closed by being refused,
    # and leaving it in the OPEN tally would report an opening this tree does
    # not have -- which is the exact inflation S4's four wrong words caused.
    c[REFUSED] += len(CLOSED_ROWS)
    return c


def pending_rulings():
    """PENDING_RULINGS as printed (none since M ruled M-D65-2; DOCKET 68's
    M-D68-P1 was converted to the ruling M-D68-C12; DOCKET 66's question on
    spec.py's 'TURN' is carried in O9's answer, not here)."""
    return list(PENDING_RULINGS)


def balance():
    """[(id, what, demand, supply, gap in orders or None)] -- the two sides.

    A gap of None means REFUSED: the mechanism fails before the magnitude is
    reached, so there is no ladder and a number would invent one.
    """
    rows = []
    rows.append(("B1", "negative enclosed mass, 1 m of contraction",
                 "%.6g kg" % required_negative_mass(1.0),
                 "no mechanism supplies negative enclosed mass at all",
                 None))
    rows.append(("B2", "negative enclosed mass, the Proxima span",
                 "%.6g kg  (%.6g solar masses)"
                 % (required_negative_mass(PROXIMA_M),
                    required_negative_mass(PROXIMA_M) / M_SUN),
                 "as B1", None))
    # CORRECTED (DOCKET 67).  B3's supply as first written: "m(r) > 0 near the
    # wall for every real mirror" -- true only for eps <~ the plasma
    # wavelength, on the INTERIOR side (outside, the plasma term has the
    # opposite sign), on tolman.py's RECONSTRUCTED spherical prefactor; the
    # sign holds for every passive, local, sharp-boundary medium.  For
    # a >> lambdabar_p the band lambdabar_p << eps << a follows the ideal
    # p_r < 0 (argued, not computed, for a sphere), and there B3's refusal
    # rests on the magnitude ground, 2G|m|/(ac^2) <= 2.3e-56, not on the sign.
    rows.append(("B3", "Casimir as a source of negative enclosed mass",
                 "m(r) < 0 near the wall",
                 "m(r) > 0 near the wall, inside, for every real mirror, at "
                 "eps <~ the plasma wavelength (any passive, local, "
                 "sharp-boundary medium; outside, the sign reverses)",
                 None))
    # CORRECTED (DOCKET 67).  B4's supply as first written: "<= 2.72e-8 for
    # hydrogen, the lightest conceivable sheet".  The literal has no owning
    # instrument; its construction, recovered by DOCKET 67 to 3 s.f., is the
    # continuum bound R <= pi^2 hbar / (1440 d m c) with gap = site spacing
    # d = a0 and site mass m = m_H (H-CONTINUUM, H-GAP-GE-SPACING, spacing >=
    # a0, site mass >= m_H, H-PASSIVE, H-PLANAR-INFINITE, H-T0).  Hydrogen is
    # not the maximum: muonium 2.40e-7, positronium 1.25e-5, nuclear density
    # 7.83e-4 -- all below 1, so the refusal stands.  (CORRECTED, DOCKET 67
    # follow-ups: the nuclear entry was typed 7.43e-4, at the recalled 2.3e17;
    # it is now NUCLEAR_SHEET_RATIO, computed on address.RHO_NUCLEAR.)
    rows.append(("B4", "the mirror against the asset it buys",
                 "|E_Cas| >= M c^2 for the apparatus",
                 "|E_Cas|/(M c^2) <= 2.72e-8 for hydrogen sheets (ordinary "
                 "atomic matter: continuum, passive, planar, T = 0); "
                 "positronium 1.25e-5, nuclear density "
                 + NUCLEAR_SHEET_RATIO_TEXT + " (first 7.43e-4)",
                 None))
    return rows


def report():
    print(__doc__.split("===============", 1)[0].strip())
    print()
    print("THE EXCHANGE RATE, ASKED AND RE-DERIVED")
    print("  Lambda (overturn.py)           %.15f" % LAMBDA)
    print("  c^2/(G Lambda)                 %.6e kg per metre" % EXCHANGE_RATE)
    print("  the Proxima span               %.6e m" % PROXIMA_M)
    print("  and its demand                 %.6e solar masses"
          % (required_negative_mass(PROXIMA_M) / M_SUN))

    print("\nLEFT -- THE DEMAND")
    for rid, claim, st, owner, moves in DEMAND:
        print("  %-4s %-9s %s" % (rid, st, _one_line(claim, 96)))
        if owner:
            # An owner that is a function (D28's massform.pair_floor_j) is
            # shown by its value at the owner's defaults, not by its address.
            v = ask(owner)
            print("       asked: %s.%s%s = %s"
                  % (owner[0], owner[1], "()" if callable(v) else "",
                     str(v() if callable(v) else v)[:58]))

    print("\nRIGHT -- THE SUPPLY")
    for rid, what, st, owner, note in SUPPLY:
        # The name in full (a cut name can change the meaning: S10's cut read
        # as a refusal of atomic mass formed at a seat, which S11-S13 price).
        print("  %-4s %-9s %s" % (rid, st, what))
        if owner == ("massform", "MECHANISM_VERDICT"):
            # M's mechanism: its one-line is massform.mechanism_label(), asked
            # and printed whole, so the refusal never prints without the
            # priced remainders beside it (M's rule).
            print(textwrap.fill("as stated: " + massform.mechanism_label(), 96,
                                initial_indent="       ",
                                subsequent_indent="         "))
        else:
            print("       %s" % _one_line(note, 100))

    print("\nTHE BALANCE")
    for rid, what, dem, sup, gap in balance():
        print("  %-4s %s" % (rid, what))
        print("       demand: %s" % dem)
        print("       supply: %s" % sup)
        print("       gap:    %s" % ("REFUSED -- no ladder, so no number"
                                     if gap is None else "%.3f orders" % gap))

    print("\nOPEN, AND WHAT WOULD ANSWER EACH")
    for r in OPEN_ROWS:
        rid, claim, answer, owner = r
        print("  %-4s %s" % (rid, _one_line(claim, 100)))
        print("       would be answered by: %s" % _one_line(answer, 96))
        # DOCKET 68: a row with no closing flag on its owner prints the
        # owner's computed reading (OPEN_ROW_READINGS) in its place.
        print("       asked: %s = %s" % open_row_answer(r))
    for rid, claim, _st, owner, moves in open_demand():
        print("  %-4s (a DEMAND row) %s" % (rid, _one_line(claim, 86)))
        print("       would be answered by: %s" % _one_line(moves, 96))
    for q, why, opener in WAITS_FOR_ITS_INSTRUMENT:
        print("  NOT OPENED, WAITING FOR ITS INSTRUMENT: %s" % q)
        print("       %s" % _one_line(why, 96))
        print("       opened by: %s" % _one_line(opener, 96))
    if not WAITS_FOR_ITS_INSTRUMENT:
        print("  NOT OPENED, WAITING FOR ITS INSTRUMENT: none")
    for q, docket, rid, _why in OPENED_FROM_WAITING:
        print("       (was waiting: %s -- opened by %s as %s)" % (q, docket, rid))

    print("\nRULED BY M -- APPLIED")
    for pid, q, why, ruling, unblocks in RULED_BY_M:
        # The question in full as well: M-D65-2's is printed exactly as it
        # was put to M.
        print(textwrap.fill(pid.ljust(8) + " " + " ".join(q.split()), 96,
                            initial_indent="  ", subsequent_indent="           "))
        # In full, never cut: a ruling carries M's own words (M-D65-1).
        print(textwrap.fill("ruled: " + " ".join(ruling.split()), 96,
                            initial_indent="       ",
                            subsequent_indent="         "))
        print(textwrap.fill("unblocks: " + " ".join(unblocks.split()), 96,
                            initial_indent="       ",
                            subsequent_indent="         "))
    print("\nCARRIED BY THE CHARTER FROM M -- PROPOSALS AND INSTRUCTIONS, NOT RULINGS")
    for cid, ctx, carried, feeds in D68_CARRIED:
        print(textwrap.fill(cid.ljust(8) + " " + " ".join(ctx.split()), 96,
                            initial_indent="  ", subsequent_indent="           "))
        print(textwrap.fill("carried: " + " ".join(carried.split()), 96,
                            initial_indent="       ", subsequent_indent="         "))
        print(textwrap.fill("feeds: " + " ".join(feeds.split()), 96,
                            initial_indent="       ", subsequent_indent="         "))
    print("\nCARRIED BY THE RULINGS FILE FROM M -- STATEMENTS, AN INSTRUCTION, A HYPOTHESIS AND "
          "A QUESTION, NOT RULINGS")
    for cid, ctx, carried, feeds in D68_FILE_CARRIED:
        print(textwrap.fill(cid.ljust(8) + " " + " ".join(ctx.split()), 96,
                            initial_indent="  ", subsequent_indent="           "))
        print(textwrap.fill("carried: " + " ".join(carried.split()), 96,
                            initial_indent="       ", subsequent_indent="         "))
        print(textwrap.fill("feeds: " + " ".join(feeds.split()), 96,
                            initial_indent="       ", subsequent_indent="         "))
    print("\nDOCKET 68 WAVE 3 AND STEP 1b -- WHAT STAYS OPEN (section 8c; no board status moves)")
    for oid, what, answers, owner in W3S1B_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nSTEP 1c -- WHAT STAYS OPEN (section 8d; no board status moves)")
    for oid, what, answers, owner in S1C_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nDOCKET 68 WAVE 4 -- WHAT STAYS OPEN (section 8e; DOCKET 68 closed: docket68/CLOSE.md)")
    for oid, what, answers, owner in W4_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nH-CMB-CORRIDOR READING 1 -- WHAT STAYS OPEN (section 8f; the CMB as H-FRAME's frame)")
    for oid, what, answers, owner in CMB_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nH-CMB-CORRIDOR READINGS 2 AND 3, AND THE LOCAL CLOCKS -- WHAT STAYS OPEN (section 8g)")
    for oid, what, answers, owner in CMB2_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nM-SUPPORT'S DYNAMICS AND READING (b)'S PRICE -- WHAT STAYS OPEN (section 8h)")
    for oid, what, answers, owner in CMB3_OPEN:
        print(textwrap.fill("%s %s -- answered by: %s (%s)" % (oid.ljust(8), " ".join(what.split()),
                                                              " ".join(answers.split()), owner),
                            96, initial_indent="  ", subsequent_indent="           "))
    print("\nPENDING M'S RULING -- RECORDED, NOT APPLIED%s"
          % ("" if PENDING_RULINGS else ": none"))
    for pid, q, why, proposal, waits in pending_rulings():
        print("  %-8s %s" % (pid, _one_line(q, 94)))
        print("       %s" % _one_line(why, 96))
        print("       proposed: %s" % _one_line(proposal, 86))
        print("       waiting on it: %s" % _one_line(waits, 81))

    print("\nROW WORDING REPLACED, KEPT: %s  (--md prints it)"
          % ", ".join("%s (%s)" % (r[0], r[1]) for r in SUPERSEDED_WORDING))

    print("\nCLOSED -- WAS OPEN, NOW ANSWERED")
    for rid, claim, answer in CLOSED_ROWS:
        print("  %-4s %s" % (rid, _one_line(claim, 100)))
        print("       %s" % _one_line(answer, 100))

    print("\nWITHDRAWN -- ASSERTED BY THIS PROJECT, THEN REFUTED BY IT")
    for rid, claim, why in WITHDRAWN_ROWS:
        print("  %-4s %s" % (rid, claim[:100]))
        print("       %s" % _one_line(why, 100))

    c = statuses()
    print("\nTHE STATUS CENSUS")
    for s in STATUSES:
        print("  %-11s %3d" % (s, c[s]))
    print("  %-11s %3d  (rows whose owner is a paper, not a module: %s)"
          % ("UNASKABLE", len(unaskable()), ", ".join(unaskable())))
    return 0


# ---------------------------------------------------------------------------
# THE GENERATED DOCUMENT.  `state.py`'s pattern: the markdown is WRITTEN by the
# instrument, never edited, and `--check` re-asks every row and fails on drift.
# A hand-edited LEDGER.md is the failure mode this whole file exists to prevent,
# so the header says so and --check would catch it.
# ---------------------------------------------------------------------------

MD_HEADER = """# The warp result: what is established, and what is owed

Generated by `python3 research/warp-drive/ledger.py --md`. **Do not edit.**
Every row below is asked of the instrument that owns it at generation time;
`--check` re-asks them and exits 1 on drift.

`COMPLETE` is not claimed and is not claimable. This is what has been
established and refuted so far, not a census of what is establishable.
"""


#: CELL WIDTHS FOR LEDGER.md.  The rows DOCKET 64 wrote are longer than any
#: before them, and a cell cut at a fixed width drops the end of a claim --
#: which is where this tree puts its qualifications.  The selftest checks that
#: no demand, supply, open, superseded or pending cell is cut (the closed and
#: withdrawn tables are summaries and keep their shorter widths).  DOCKET 65
#: added the supply note to that check: S10 carries its claim and its movers in
#: one note, and the old fixed 2000 would have cut them.
W_DEMAND_CLAIM = 5200             # DOCKET 67: D24 names the dropped
                                  # hypotheses M ruled repaired ("Repair all").
                                  # DOCKET 68 wave 2: 4000 -> 5200 -- the D23
                                  # and D25 notes carry vacuum.py's and seat.py's
                                  # asked values and D23 keeps wave 1's words
                                  # (4734 and 4472 chars as rendered)
W_DEMAND_MOVES = 1200             # DOCKET 65: D27's movers run past 1000
W_SUPPLY_NOTE = 5000              # DOCKET 65: S10's claim and movers, one note,
                                  # and the item S10 (open) (M-D65-2)
W_OPEN_CLAIM = 15000              # DOCKET 66: 10000 -> 15000 -- O9 carries its
                                  # DOCKET 66 part after DOCKET 68's, every verdict
                                  # asked of combine66 and D66 wave 1's words kept
                                  # (13765 chars as rendered at the seating).
                                  # DOCKET 67: as W_DEMAND_CLAIM (D24 is OPEN);
                                  # follow-ups: O5 names FO/FFKP REFUSED on the
                                  # Hadamard clause, with its correction (4065
                                  # chars as rendered at the follow-ups).
                                  # DOCKET 68 residuals: 4400 -> 6000 -- O9 now
                                  # prints the readings first left unasked (KR,
                                  # ITJ, ITE, RQ, ITB+RQ) and signed.py (4b)'s
                                  # steps with their statuses.  DOCKET 68 wave 2:
                                  # 6000 -> 9000 -- O9 prints support 1's nine
                                  # READ windows, the vacuum and seat grades,
                                  # and wave 1's words kept (8474 chars as
                                  # rendered).  W2 reproduction: 9000 -> 10000
                                  # -- O9 keeps N's whole status from
                                  # seat.proxima_measured and scopes the
                                  # message count, with the wave-2 seat's words
                                  # kept (9170 chars as rendered; at 9000 the
                                  # cut-cell check caught it)
W_OPEN_ANSWER = 5000              # DOCKET 66: 2400 -> 4000 -- O9's answer gains
                                  # DOCKET 66's pathways and the TURN question for M
                                  # (measured at the seating; the cut-cell check guards).
                                  # DOCKET 67: O2's answer names its
                                  # conditions (M ruled "Repair all").
                                  # DOCKET 68 wave 2: 1400 -> 2400 -- O9's
                                  # answer names what wave 2 left open and
                                  # keeps wave 1's answer after it.
                                  # R-seat (M's DOCKET 66 rulings): 4000 -> 5000
                                  # -- O9's answer gains the re-graded
                                  # O-MAKE-TOPO, the adopted TURN reading and the
                                  # TURN question kept as first carried (4572
                                  # chars as rendered; at 4000 the cut-cell
                                  # check caught it)
W_WAS = 1400
W_WHY = 1000                      # DOCKET 67: superseded rows carry
                                  # the corrections M ruled ("Repair all")
W_RULING = 2000                   # DOCKET 66: 1600 -> 2000 -- M-D65-1's ruling
                                  # cell says what DOCKET 66 ran, asked of qet.py,
                                  # and keeps its first wording (1676 chars as
                                  # rendered at the seating).
                                  # DOCKET 65: M-D65-4's ruling cell names M's
                                  # rule for the paper and the DOCKET 63 marker
                                  # READ back from the paper; 600 would cut it.
                                  # DOCKET 67 follow-ups: it now carries the
                                  # DOCKET 67 markers' correction (1007 chars
                                  # as rendered at the follow-ups).  DOCKET 67
                                  # close: 1200 -> 1600 -- M-D65-5's census READs
                                  # the closing rulings' markers too (1298 chars
                                  # as rendered at the close), and 1200 cut it


def _cell(text, width):
    """One table cell: one line, cut at `width`, and every '|' escaped so a
    claim like E_pos/|E_neg| cannot split the row into extra columns."""
    return _one_line(text, width).replace("|", "\\|")


def to_markdown():
    L = [MD_HEADER, "", "## The exchange rate", "",
         "| | |", "|---|---|",
         "| Lambda (overturn.py) | %.15f |" % LAMBDA,
         "| c^2/(G Lambda) | %.6e kg per metre |" % EXCHANGE_RATE,
         "| the Proxima span | %.6e m |" % PROXIMA_M,
         "| its demand | %.6e solar masses |"
         % (required_negative_mass(PROXIMA_M) / M_SUN),
         "", "## Left -- the demand", "",
         "| id | status | claim | asked of | what would move it |",
         "|---|---|---|---|---|"]
    for rid, claim, st, owner, moves in DEMAND:
        src = "%s.%s" % owner if owner else "*(a paper -- see the note)*"
        L.append("| %s | **%s** | %s | `%s` | %s |"
                 % (rid, st, _cell(claim, W_DEMAND_CLAIM), src,
                    _cell(moves, W_DEMAND_MOVES)))

    L += ["", "## Right -- the supply", "",
          "| id | status | mechanism | note |", "|---|---|---|---|"]
    for rid, what, st, _o, note in SUPPLY:
        L.append("| %s | **%s** | %s | %s |"
                 % (rid, st, _cell(what, 80), _cell(note, W_SUPPLY_NOTE)))

    L += ["", "## The balance", "",
          "| id | quantity | demand | supply | gap |", "|---|---|---|---|---|"]
    for rid, what, dem, sup, gap in balance():
        g = "**REFUSED** -- no ladder, so no number" if gap is None \
            else "%.3f orders" % gap
        L.append("| %s | %s | %s | %s | %s |"
                 % (rid, _cell(what, 200), _cell(dem, 200), _cell(sup, 200), g))

    L += ["", "## Open, and what would answer each", ""]
    for r in OPEN_ROWS:
        rid, claim, answer, owner = r
        L += ["### %s" % rid, "", _one_line(claim, W_OPEN_CLAIM), "",
              "**Would be answered by:** %s"
              % _one_line(answer, W_OPEN_ANSWER), "",
              "*Asked:* `%s = %s`" % open_row_answer(r), ""]
    for rid, claim, _st, owner, moves in open_demand():
        L += ["### %s (a demand row)" % rid, "",
              _one_line(claim, W_OPEN_CLAIM), "",
              "**Would be answered by:** %s"
              % _one_line(moves, W_OPEN_ANSWER), "",
              "*Asked:* `%s.%s = %s`" % (owner[0], owner[1], ask(owner)), ""]
    L += ["### Not opened: waiting for its instrument", "",
          "A question with no instrument is opened by the docket that builds",
          "one (the principle in `ledger.py`'s docstring, section 4).", ""]
    if WAITS_FOR_ITS_INSTRUMENT:
        L += ["| question | why it has no row yet | what opens it |",
              "|---|---|---|"]
        for q, why, opener in WAITS_FOR_ITS_INSTRUMENT:
            L.append("| %s | %s | %s |"
                     % (_cell(q, 80), _cell(why, W_WHY), _cell(opener, 200)))
    else:
        L.append("**None.**")
    L += ["", "Opened since, by the docket that built the instrument:", "",
          "| question | opened by | as row | why it had waited |",
          "|---|---|---|---|"]
    for q, docket, rid, why in OPENED_FROM_WAITING:
        L.append("| %s | %s | %s | %s |"
                 % (_cell(q, 80), docket, rid, _cell(why, W_WHY)))
    L.append("")

    L += ["## Ruled by M -- applied", "",
          "| id | question | ruling | unblocks |", "|---|---|---|---|"]
    for pid, q, why, ruling, unblocks in RULED_BY_M:
        L.append("| %s | %s | %s | %s |"
                 % (pid, _cell(q, W_WHY), _cell(ruling, W_RULING), _cell(unblocks, W_WHY)))
    L.append("")
    L += ["## Carried by the charter from M -- proposals and instructions, not rulings", "",
          "M's words, verbatim, that CHARTER.md carries as a named hypothesis or a",
          "standing instruction without a ruling. They are not counted as rulings.", "",
          "| id | M's words in context | carried | feeds |", "|---|---|---|---|"]
    for cid, ctx, carried, feeds in D68_CARRIED:
        L.append("| %s | %s | %s | %s |"
                 % (cid, _cell(ctx, W_RULING), _cell(carried, W_RULING), _cell(feeds, W_WHY)))
    L.append("")
    # ADDED (W3S1B-seat, docstring section 8c).
    L += ["## Carried by the rulings file from M -- statements, an instruction, a hypothesis and "
          "a question, not rulings", "",
          "M's words, verbatim, that M-RULINGS-2026-10-03.md carries without a ruling, each",
          "carried as a named hypothesis or answered by computation in a DOCKET 68 wave-3 or",
          "Step 1b owner. They are not counted as rulings.", "",
          "| id | M's words in context | carried | feeds |", "|---|---|---|---|"]
    for cid, ctx, carried, feeds in D68_FILE_CARRIED:
        L.append("| %s | %s | %s | %s |"
                 % (cid, _cell(ctx, W_RULING), _cell(carried, W_RULING), _cell(feeds, W_WHY)))
    L.append("")
    L += ["## DOCKET 68 wave 3 and Step 1b -- what stays open", "",
          "Seated on M's \"Seat both (Recommended)\" (item 36; docstring section 8c). No board",
          "status moves: wave 3's O-BITS grade is its owner's PROPOSAL, not screened by",
          "combine.py. Each item names what would answer it.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in W3S1B_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    # ADDED (S1C-seat, docstring section 8d).
    L += ["## Step 1c -- what stays open", "",
          "Seated on M's \"3, then 2. Then 1 last please\" (item 39; docstring section 8d). No board",
          "status moves. Each item names what would answer it.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in S1C_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    # ADDED (D68-close, docstring section 8e).
    L += ["## DOCKET 68 wave 4 -- what stays open (DOCKET 68 closed)", "",
          "Seated on M's \"2 then 1 please\" (item 40; docstring section 8e). DOCKET 68's close",
          "record is docket68/CLOSE.md: not found, not excluded; O9 stays OPEN.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in W4_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    # ADDED (CMB-seat, docstring section 8f).
    L += ["## H-CMB-CORRIDOR reading 1 -- what stays open", "",
          "Seated on M's \"Seat it, then medium\" (item 45; docstring section 8f): the background's rest",
          "frame as H-FRAME's frame (docket68/cmb/). No board status moves; O9 stays OPEN.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in CMB_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    # ADDED (CMB2-seat, docstring section 8g).
    L += ["## H-CMB-CORRIDOR readings 2 and 3, and the local clocks -- what stays open", "",
          "Seated on M's \"3, then 2, then 1 please\" (item 54; docstring section 8g): the background as a",
          "medium, the observation model and the local clocks (docket68/cmb/). support.py and bias.py",
          "are built and verified, not seated. No board status moves; O9 stays OPEN.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in CMB2_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    # ADDED (CMB3-seat, docstring section 8h).
    L += ["## M-SUPPORT's dynamics and reading (b)'s price -- what stays open", "",
          "Seated on M's \"Seat both\" (item 55; docstring section 8h): support.py and bias.py",
          "(docket68/cmb/). No board status moves; O9 stays OPEN.", "",
          "| id | open | what would answer it | owner |", "|---|---|---|---|"]
    for oid, what, answers, owner in CMB3_OPEN:
        L.append("| %s | %s | %s | %s |" % (oid, _cell(what, W_WHY), _cell(answers, W_WHY),
                                            _cell(owner, W_WHY)))
    L.append("")
    L += ["## Pending M's ruling -- recorded, not applied", "",
          "This file edits no peer and changes no requirement. A question",
          "that needs M's ruling is recorded here so the board shows it.", "",
          "| id | question | why it is asked | proposed | waiting on it |",
          "|---|---|---|---|---|"]
    for pid, q, why, proposal, waits in pending_rulings():
        L.append("| %s | %s | %s | %s | %s |"
                 % (pid, _cell(q, W_WHY), _cell(why, W_WHY),
                    _cell(proposal, W_WHY), _cell(waits, W_WHY)))
    L.append("")

    L += ["## Row wording replaced by DOCKETS %s" % superseded_dockets(), "",
          "Kept, never deleted: a row rewritten in place is otherwise",
          "indistinguishable from one that always said the new thing.", "",
          "| id | replaced by | as it stood (claim \\|\\| answer) "
          "| why it was replaced |",
          "|---|---|---|---|"]
    for rid, docket, was, why in SUPERSEDED_WORDING:
        L.append("| %s | %s | %s | %s |"
                 % (rid, docket, _cell(was, W_WAS), _cell(why, W_WHY)))
    L.append("")

    L += ["## Closed -- was open, now answered", "",
          "| id | what was open | how it closed |", "|---|---|---|"]
    for rid, claim, answer in CLOSED_ROWS:
        L.append("| %s | %s | %s |"
                 % (rid, _cell(claim, 220), _cell(answer, 400)))

    L += ["", "## Withdrawn -- asserted by this project, then refuted by it", "",
          "Kept, never deleted. A withdrawn figure that leaves no trace is how",
          "a corpus forgets it was ever wrong.", "",
          "| id | what was claimed | why it fell |", "|---|---|---|"]
    for rid, claim, why in WITHDRAWN_ROWS:
        L.append("| %s | %s | %s |"
                 % (rid, _cell(claim, 220), _cell(why, 300)))

    c = statuses()
    L += ["", "## Status census", "", "| status | rows |", "|---|---|"]
    for st in STATUSES:
        L.append("| %s | %d |" % (st, c[st]))
    L += ["", "Rows whose owner is a paper rather than a module, and which this",
          "file therefore cannot ask: **%s**." % ", ".join(unaskable()), ""]
    return "\n".join(L) + "\n"


def write_md(path=LEDGER_MD):
    io_open = open
    with io_open(path, "w", encoding="utf-8") as fh:
        fh.write(to_markdown())
    print("wrote %s" % path)
    return 0


def check(path=LEDGER_MD):
    """Re-ask every row and compare against the written document."""
    try:
        with open(path, encoding="utf-8") as fh:
            on_disk = fh.read()
    except FileNotFoundError:
        print("XX   %s does not exist -- run --md" % path)
        return 1
    fresh = to_markdown()
    if on_disk == fresh:
        print("ok   %s agrees with a fresh ask of every row" % path)
        return 0
    da, db = on_disk.split("\n"), fresh.split("\n")
    print("XX   %s has DRIFTED from its instruments" % path)
    shown = 0
    for i in range(max(len(da), len(db))):
        a = da[i] if i < len(da) else "<absent>"
        b = db[i] if i < len(db) else "<absent>"
        if a != b and shown < 6:
            print("     line %d\n       on disk: %s\n       fresh:   %s"
                  % (i + 1, a[:100], b[:100]))
            shown += 1
    return 1


def _superseded_keys_unique(entries):
    """True iff no (row, docket) key occurs twice in `entries`."""
    keys = [(r[0], r[1]) for r in entries]
    return len(keys) == len(set(keys))


def _withdrawn_needles_64():
    """Wordings DOCKET 64 withdrew or corrected, each with its source.  Held
    as data for the needle check; none of them is a result."""
    return [
        "exp(-10^142)",                       # noise.CORRECTED (computed)
        "no confirmed condensed reservoir",   # formation [W2]
        "confirms no condensed reservoir",    # formation [W2], ruling C text
        "cannot be priced from the source",   # formation [W3]
        "OBSTRUCTION IS PROVED",              # linstab.WITHDRAWN
        "ONE RENORMALISATION CONSTANT",       # linstab.WITHDRAWN
        "Planck-scale runaways",              # linstab.WITHDRAWN
        "nothing grows from it",              # linstab.WITHDRAWN
        "0.0074335 ",                         # hpscentre.WITHDRAWN (typed K)
        "two misprints and two errors",       # hpscentre.WITHDRAWN
        "domain of validity for",             # hpscentre.WITHDRAWN (DOMAIN)
        "SATISFIED --",                       # qeihps withdrawn verdict form
        "PROVED NOT EVALUABLE",               # formation [W6]
        "HPS integrated the PRINTED",         # hpscentre.WITHDRAWN
    ]


def _truncated_cells(demand_claim=None, demand_moves=None, open_claim=None,
                     open_answer=None, was=None, why=None, supply_note=None):
    """(table, id) of every demand, supply, open, superseded or pending cell
    that _one_line would cut at the given widths (default: the module's)."""
    dc = W_DEMAND_CLAIM if demand_claim is None else demand_claim
    dm = W_DEMAND_MOVES if demand_moves is None else demand_moves
    oc = W_OPEN_CLAIM if open_claim is None else open_claim
    oa = W_OPEN_ANSWER if open_answer is None else open_answer
    wa = W_WAS if was is None else was
    wh = W_WHY if why is None else why
    sn = W_SUPPLY_NOTE if supply_note is None else supply_note

    def cut(text, width):
        return _one_line(text, width) != " ".join(text.split())
    out = []
    for r in DEMAND:
        if cut(r[1], dc) or cut(r[4], dm):
            out.append(("demand", r[0]))
        if r[2] == OPEN and (cut(r[1], oc) or cut(r[4], oa)):
            out.append(("open demand", r[0]))
    for r in SUPPLY:
        if cut(r[4], sn):
            out.append(("supply", r[0]))
    for r in OPEN_ROWS:
        if cut(r[1], oc) or cut(r[2], oa):
            out.append(("open", r[0]))
    for r in SUPERSEDED_WORDING:
        if cut(r[2], wa) or cut(r[3], wh):
            out.append(("superseded", r[0] + " " + r[1]))
    # Every cell of a pending ruling: its question states what M approved.
    for r in pending_rulings():
        if cut(r[1], wh) or cut(r[2], wh) or cut(r[3], wh) or cut(r[4], wh):
            out.append(("pending", r[0]))
    # A ruling carries M's own words (M-D65-1) and its question as put to M
    # (M-D65-2): neither is ever cut, nor what it unblocks.
    for r in RULED_BY_M:
        if cut(r[1], wh) or cut(r[3], W_RULING) or cut(r[4], wh):
            out.append(("ruled", r[0]))
    # A carried item carries M's words too: never cut.
    for r in D68_CARRIED + D68_FILE_CARRIED:
        if cut(r[1], W_RULING) or cut(r[2], W_RULING) or cut(r[3], wh):
            out.append(("carried", r[0]))
    for r in W3S1B_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("w3s1b-open", r[0]))
    for r in S1C_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("s1c-open", r[0]))
    for r in W4_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("w4-open", r[0]))
    for r in CMB_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("cmb-open", r[0]))
    for r in CMB2_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("cmb2-open", r[0]))
    for r in CMB3_OPEN:
        if any(cut(c, wh) for c in r[1:]):
            out.append(("cmb3-open", r[0]))
    return out


#: DOCKET 65's QUALIFIERS, per seated row: (phrase, how many times the row
#: carries it).  The board's other guard on these rows is exact equality with
#: massform.PROPOSED_ROWS, and massform's own REQUIRED_WORDING does not pin
#: every one, so a qualifier deleted at the owner would reach LEDGER.md green.
#: Each is a named hypothesis, a scope or an admission the row rests on; a
#: count, not a presence, so deleting one of several occurrences is caught.
#: The bare hypothesis tokens are pinned by WHOLE-ROW count as well as in one
#: phrase each: a phrase pin covers one context, and every other occurrence of
#: the token (D27's 'on H-PRESENT it needs no P-UNIFORM', HELD_SEAT_TEXT's
#: H-TREE and H-UNSOURCED-SEAT, _C1_TEMPLATE's H-TREE) could otherwise be
#: deleted at the owner and reach LEDGER.md green.  The counts are what
#: _row_text returned when they were pinned.
SEATED_QUALIFIERS = {
    # D27's scope: 'can only LOWER |phi|' is a claim within D20's model, and
    # without the phrase it reads unconditional.
    "D27": (("Where H-UNSOURCED-SEAT fails", 1), ("measured masses (H-PRESENT)", 1),
            ("within excite's section-3 model", 1), ("Within D20's model", 1),
            ("H-PRESENT", 5), ("H-UNSOURCED-SEAT", 4), ("H-TREE", 3), ("P-UNIFORM", 6)),
    # D28's 'at least': the pair floor is PROVED as a floor; without it the
    # row states an exact cost, which is false.
    # 'both NAMED-NOT-READ' is still its owners' status (DOCKET 67 follow-ups,
    # checked): gravity.U_KG is typed CODATA 2018 and stock.ATOMIC_MASS is
    # uncited -- neither was READ by DOCKET 67, unlike G_F (D20, S11).
    "D28": (("both NAMED-NOT-READ", 1), ("H-BL", 1), ("H-AME", 1),
            ("negligible at payload scale", 1), ("costs at least", 1)),
    # D29's and S12's H-BRIDGE (DOCKET 67, key 1809.06923, M's ruling
    # 2026-10-02): the bridge from the READ decay clauses to 'no atomic mass at
    # the seat', on which D29's THEOREM grade (decay conjunct only) and S12's
    # 'Priced, not refused' rest.  Without it both read as carried by the READ
    # text alone, which they are not.
    "D29": (("H-REAL", 2), ("claimed and not computed", 1), ("not established", 1),
            ("INFERENCE", 1), ("H-BRIDGE", 3), ("for its decay conjunct only", 1)),
    "S10": (("as NET formation only", 1), ("on P-UNIFORM)", 1), ("H-LINEAR", 1),
            ("none a bound", 1), ("OPEN, and no verdict rests on it", 1),
            ("elements (H-PRESENT)", 1),
            ("H-PRESENT", 5), ("H-UNSOURCED-SEAT", 3), ("H-TREE", 2), ("P-UNIFORM", 6),
            # The item S10 (open), carried in S10's note on M's ruling M-D65-2
            # (these pins were O8's while it was seated as a row): its
            # admissions, and 'undecided'/'H-LINEAR' counted over the note.
            ("(H-LINEAR)", 1), ("Not computed and not read here", 1),
            ("whether it exceeds half is undecided here", 2),
            ("H-LINEAR", 2), ("undecided", 2)),
    # S11's admission that v is NAMED-NOT-READ (via alpha_W) -- as first
    # pinned.  CORRECTED (DOCKET 67 follow-ups): DOCKET 67 READ G_F (PDG 2024
    # Table 1.1) and massform.py now says v is COMPUTED from the READ G_F, at
    # tree level; the old phrase survives at the owner only as history ("which
    # lifted alpha_W's NAMED-NOT-READ"), so that pin now guards the record of
    # the lift, and the current status and its tree-level scope are pinned
    # beside it (counts as _row_text returned them when pinned).
    "S11": (("CONTESTED", 1), ("dissent", 1), ("decides nothing", 1), ("unproven", 1),
            ("alpha_W's NAMED-NOT-READ", 1),
            ("lifted alpha_W's NAMED-NOT-READ", 1),
            ("v (COMPUTED from the READ G_F, tree level)", 1),
            ("tree-level G_mu-scheme coupling, its scale and scheme unfixed", 1)),
    # S12's 'at least': the carrier supplies the pair floor or more.
    "S12": (("(not computed here)", 1), ("supplies at least the pair floor", 1),
            ("H-BRIDGE", 3), ("rests on H-BRIDGE through D29", 1)),
    # RE-PINNED BY DOCKET 66's SEATING: H-RELEASE 3 -> 4 -- S13's DOCKET 66
    # note names it once more (the defect core's hold cannot use it).
    "S13": (("Within excite's section-3 model", 2), ("not a bound", 1),
            ("H-RELEASE", 4), ("H-UNSOURCED-SEAT", 2), ("H-TREE", 1),
            ("(not computed here)", 1)),
}


def _row_text(rid, rows=None):
    """Every text field of seated row `rid`, whitespace-normalised."""
    rows = dict((r[0], r) for r in DEMAND + SUPPLY + OPEN_ROWS) if rows is None else rows
    return " ".join(" ".join(x.split()) for x in rows[rid] if isinstance(x, str))


def missing_qualifiers(rows=None):
    """[(row id, phrase, times carried, times required)] for every DOCKET 65
    qualifier a seated row carries fewer times than SEATED_QUALIFIERS says."""
    out = []
    for rid, need in SEATED_QUALIFIERS.items():
        t = _row_text(rid, rows)
        for phrase, n in need:
            if t.count(phrase) < n:
                out.append((rid, phrase, t.count(phrase), n))
    return out


_VERBATIM = re.compile(r"verbatim: '([^']+)'")
#: M-D65-3's words hold apostrophes, so every cell quotes them in double quotes.
_VERBATIM_DQ = re.compile(r'verbatim: "([^"]+)"')
#: (the constant M's words are held in, the pattern that finds a printed copy)
#: per DOCKET 65 ruling that quotes M verbatim.
_M_WORDS = {"M-D65-1": (M_D65_1_WORDS, _VERBATIM),
            "M-D65-3": (M_D65_3_WORDS, _VERBATIM_DQ)}


def verbatim_faults(qrow=None, md=None, rid="M-D65-1"):
    """[fault] where a printed copy of M's words in a DOCKET 65 ruling (`rid`:
    M-D65-1 or M-D65-3) -- `why`, the ruling cell (which LEDGER.md and the
    report print), or LEDGER.md's line for it -- is not exactly the constant
    the words are held in, or where a copy is missing."""
    qrow = [r for r in RULED_BY_M if r[0] == rid][0] if qrow is None else qrow
    md = to_markdown() if md is None else md
    words, pat = _M_WORDS[rid]
    line = [l for l in md.splitlines() if l.startswith("| %s |" % rid)]
    bad = []
    for where, text, want in (("why", qrow[2], 1), ("ruling cell", qrow[3], 1),
                              ("LEDGER.md", " ".join(line), 1)):
        got = pat.findall(" ".join(text.split()))
        if len(got) != want:
            bad.append("%s: %d verbatim copies, want %d" % (where, len(got), want))
        bad += ["%s: '%s'" % (where, g) for g in got if g != words]
    return bad


def m_d65_1_faults(qrow=None):
    """[fault] where M-D65-1 misdescribes QET's standing: the literature named
    to M incomplete (arXiv:2506.19878 was named); the ruling cell not EXACTLY
    its template filled from the constants and what DOCKET 66 ran
    (M_D65_1_RULING_T, d66_m_d65_1_ran -- so no verdict on QET can be typed
    beside the required phrases); DOCKET 65's first wording ('QET is to be
    tested inside DOCKET 66 (NOT YET RUN)') missing from the history clause, or
    NOT YET RUN printed outside it; a literature item printed as READ that
    qet.py's sources do not record as READ; the unblocks cell still saying
    NOT YET RUN outside its history; or the question's parenthetical printed
    as READ rather than as the question's own description.  CORRECTED
    (DOCKET 66's seating): this first required 'QET is to be tested inside
    DOCKET 66 (NOT YET RUN)' as the APPLIED clause and refused 'QET is tested
    inside' -- true while DOCKET 66 had not run."""
    qrow = [r for r in RULED_BY_M if r[0] == "M-D65-1"][0] if qrow is None else qrow
    why, ruling, unb = (" ".join(qrow[2].split()), " ".join(qrow[3].split()),
                        " ".join(qrow[4].split()))
    bad = []
    for aid in ("1701.03805", "2301.02666", "2505.04689", "2506.19878"):
        if not ("arXiv:%s" % aid in why and "arXiv:%s" % aid in ruling):
            bad.append("arXiv:%s missing from why or the ruling cell" % aid)
    want = " ".join((M_D65_1_RULING_T % (M_D65_1_ANSWER, M_D65_1_WORDS, M_D65_1_LITERATURE,
                                         d66_m_d65_1_ran())).split())
    if ruling != want:
        bad.append("the ruling cell is not M_D65_1_RULING_T filled from the constants and "
                   "what DOCKET 66 ran (d66_m_d65_1_ran)")
    hist = "FIRST APPLIED (kept): QET is to be tested inside DOCKET 66 (NOT YET RUN)"
    if hist not in ruling:
        bad.append("the ruling cell drops DOCKET 65's first wording (history)")
    if ruling.replace(hist, "").count("NOT YET RUN"):
        bad.append("the ruling cell says NOT YET RUN outside its history clause")
    read_ok = dict(d66_qet_literature())
    for item, entry in read_ok.items():
        if entry is None:
            bad.append("%s: qet.py records no READ entry for it" % item)
    # Only an arXiv id an item already carries is printed (specthm compares the
    # row's ids with its DOCKET 66 record's), so a READ claim names the item.
    for m in re.finditer(r"arXiv:(\d{4}\.\d{4,5})[^;:]*: READ", ruling):
        if not any(m.group(1) in (e or "") for e in read_ok.values()):
            bad.append("arXiv:%s printed as READ, and qet.py's sources head no entry with it"
                       % m.group(1))
    uhist = "FIRST SAID (kept): " + M_D65_1_UNBLOCKS_AS_FIRST_WRITTEN
    if uhist not in unb or unb.replace(uhist, "").count("NOT YET RUN"):
        bad.append("the unblocks cell: NOT YET RUN outside its history, or the history dropped")
    clause = "the question's description as put to M, not READ"
    if not (clause in why and clause in ruling):
        bad.append("the question's parenthetical is not attributed to the question")
    return bad


def p3_unblocks_faults(text=None):
    """[fault] where M-S1A-P3's unblocks cell does not say DOCKET 66 has run,
    built from the docket66 owners (d66_p3_ran), after its first wording
    ('DOCKET 66 opens', kept) -- or drops what the owners read in it ('the
    throat-creation classes stay OPEN', which defects.py and combine66.py
    check at run time)."""
    text = ([r for r in RULED_BY_M if r[0] == "M-S1A-P3"][0][4]
            if text is None else text)
    want = M_S1A_P3_UNBLOCKS_AS_FIRST_WRITTEN + ".  DOCKET 66 has run: " + d66_p3_ran()
    # EQUALITY, so no verdict can be typed beside the required phrases.
    if " ".join(text.split()) != " ".join(want.split()):
        return ["not its first wording followed by 'DOCKET 66 has run: ' and d66_p3_ran()"]
    return []


#: The DOCKET 66 charter's quotations, each with the ledger constant it must
#: occur in verbatim (whitespace normalised): the charter says 'Every quotation
#: of M below is taken from the ledger, which holds M's words as constants and
#: checks them (ledger.py: M-S1A-P3, M-D65-1)', and this is that check.
D66_CHARTER_FILE = os.path.join(D66_DIR, "CHARTER.md")


def _d66_charter_holders():
    """{charter quotation: (where the ledger holds it, the held text)}."""
    p3 = [r for r in RULED_BY_M if r[0] == "M-S1A-P3"][0]
    q1 = [r for r in RULED_BY_M if r[0] == "M-D65-1"][0]
    return {
        "1 then 2 then 3 then 4": ("D68_M_WORDS M-D68-10", D68_M_WORDS["M-D68-10"][0]),
        "Is a closed causal curve, or a Borde pathology, disqualifying?": ("M-S1A-P3 question", p3[1]),
        "My ruling refers to the seat/destination. Singular occurs in the throat where the "
        "geometry is compressed to binary information, and then push to the seat":
            ("M-S1A-P3 ruling cell", p3[3]),
        "Seating occurs in a place where matter can occur but not in its original geometric "
        "form": ("M-S1A-P3 ruling cell", p3[3]),
        "with M's throat-compression mechanism": ("M-S1A-P3 ruling cell (the ledger's words)", p3[3]),
        "these are defects": ("M-S1A-P3 ruling cell", p3[3]),
        "Should Quantum Energy Teleportation (information arriving at the destination creates a "
        "local negative-energy region there) be tested as its own docket?": ("M-D65-1 question", q1[1]),
        "Fold into D66": ("M_D65_1_ANSWER", M_D65_1_ANSWER),
        "consider the idea that the introduction of information into a space that never "
        "previously contained it would be considered exotic matter": ("M_D65_1_WORDS", M_D65_1_WORDS),
        "S5 counts": ("D68_M_WORDS M-D68-7", D68_M_WORDS["M-D68-7"][0]),
        "non physical properties/bounds that give shape to the geometry at the seat":
            ("D68_M_WORDS M-D68-1", D68_M_WORDS["M-D68-1"][0]),
        "from the seat": ("D68_M_WORDS M-D68-5", D68_M_WORDS["M-D68-5"][0]),
        "Hotta 2008; Funai & Martin-Martinez arXiv:1701.03805; Ikeda arXiv:2301.02666; review "
        "arXiv:2505.04689; arXiv:2506.19878": ("M_D65_1_LITERATURE", M_D65_1_LITERATURE),
    }


#: CHARTER QUOTATIONS THAT ARE THE LEDGER'S WORDS, NOT M'S (D66-repro,
#: FIX-SEAT-RESULT result.v): 'with M's throat-compression mechanism' is the
#: ledger's wording in its M-S1A-P3 ruling cell (it names M in the third
#: person).  The charter quotes it verbatim from the ledger and, since
#: R-apply, attributes it to the ledger; it is checked verbatim like the rest
#: (d66_charter_quote_faults) but is NOT counted among M's quotations, so
#: d66_quote_faults does not accept it as M's words in a DOCKET 66 cell.  The
#: seat first held it among M's quotations, labelled '(the ledger's words)'.
D66_CHARTER_LEDGER_WORDS = ("with M's throat-compression mechanism",)
#: The charter's attribution of it, READ (R-apply's words in CHARTER.md).
D66_CHARTER_LEDGER_ATTRIBUTION = ("is attributed to the ledger here and is not one of M's "
                                  "quotations")


def d66_charter_m_quotes(holders=None):
    """{charter quotation: holder} for M's quotations proper -- the charter's
    holders less the ledger's own words (D66_CHARTER_LEDGER_WORDS)."""
    holders = _d66_charter_holders() if holders is None else holders
    return dict((k, v) for k, v in holders.items() if k not in D66_CHARTER_LEDGER_WORDS)


def d66_charter_attribution_faults(charter=None):
    """[span] of D66_CHARTER_LEDGER_WORDS that docket66/CHARTER.md quotes
    without attributing it to the ledger (D66_CHARTER_LEDGER_ATTRIBUTION READ
    in the 400 characters after the quotation)."""
    if charter is None:
        with open(D66_CHARTER_FILE, encoding="utf-8") as fh:
            charter = fh.read()
    t = " ".join(charter.split())
    bad = []
    for sp in D66_CHARTER_LEDGER_WORDS:
        i = t.find('"%s"' % sp)
        if i < 0 or D66_CHARTER_LEDGER_ATTRIBUTION not in t[i:i + 400]:
            bad.append(sp)
    return bad


def d66_charter_quote_faults(charter=None, holders=None):
    """[(span, why)] -- a quotation in docket66/CHARTER.md (every double-quoted
    span, every single-quoted span with a space, and the literature list as
    the charter names it) that is not held verbatim in the ledger constant
    _d66_charter_holders names, or that it names no holder for."""
    if charter is None:
        with open(D66_CHARTER_FILE, encoding="utf-8") as fh:
            charter = fh.read()
    holders = _d66_charter_holders() if holders is None else holders
    t = " ".join(charter.split())
    spans = re.findall(r'"([^"]+)"', t)
    spans += re.findall(r"(?<![A-Za-z])'([^']+ [^']+)'(?![A-Za-z])", t)
    lit = "Hotta 2008; Funai & Martin-Martinez arXiv:1701.03805"
    spans += [x for x in holders if x.startswith(lit) and lit in t and x in t]
    bad = []
    for sp in spans:
        if sp not in holders:
            bad.append((sp, "no ledger constant is named for it"))
        elif sp not in " ".join(holders[sp][1].split()):
            bad.append((sp, "not verbatim in " + holders[sp][0]))
    if not any(x.startswith(lit) for x in spans):
        bad.append((lit, "the charter no longer names the literature as M_D65_1_LITERATURE holds it"))
    return bad


def _d66_tree_text():
    """docket66/'s own words: the charter, the A- and B-reports and the four
    instruments' source, whitespace normalised -- what a DOCKET 66 cell may
    quote with a single quote."""
    out = []
    for f in ("CHARTER.md", "A1-defects.md", "A2-throatbits.md", "A3-qet.md", "B-combine66.md",
              "defects.py", "throatbits.py", "qet.py", "combine66.py"):
        with open(os.path.join(D66_DIR, f), encoding="utf-8") as fh:
            out.append(" ".join(fh.read().split()))
    return " ".join(out)


def _d66_cells():
    """{site: text} -- every DOCKET 66 cell this file prints: O9's DOCKET 66
    part and answer, the S5 and S13 notes, M-S1A-P3's unblocks, M-D65-1's
    ruling and unblocks, the TURN question for M."""
    p3 = [r for r in RULED_BY_M if r[0] == "M-S1A-P3"][0]
    q1 = [r for r in RULED_BY_M if r[0] == "M-D65-1"][0]
    out = {"O9 D66 part": D66_O9_PART, "O9 D66 answer": D66_O9_ANSWER,
           "M-S1A-P3 unblocks": p3[4], "M-D65-1 ruling": q1[3], "M-D65-1 unblocks": q1[4]}
    out.update(("note " + k, v) for k, v in D66_NOTES.items())
    out.update(("TURN question col %d" % i, c) for i, c in enumerate(d66_turn_question(), 1))
    return out


def d66_quote_faults(cells=None):
    """[(site, span)] -- a quotation in a DOCKET 66 cell that is not the tree's
    words: a double-quoted span that is not M's words as the ledger holds them
    (_d66_charter_holders) or a single-quoted span with a space that occurs
    neither in docket66/'s own files nor in the ledger's held texts (M's words
    the M-S1A-P3 and M-D65-1 rows quote)."""
    cells = _d66_cells() if cells is None else cells
    # M's quotations proper (the ledger's own words excluded -- R-seat), and
    # M's words for the DOCKET 66 rulings, items 26-28 (D68_M_WORDS).  The
    # seat first joined every holder's text, the ledger's words included.
    # Each key is a charter quotation checked verbatim against its holder
    # (d66_charter_quote_faults); a holder's whole text (a ruling cell) is not
    # M's words, so the keys, not the holders' texts, are what is accepted.
    held = " || ".join(list(d66_charter_m_quotes())
                       + [D68_M_WORDS[k][0] for k in ("M-D68-26", "M-D68-27", "M-D68-28")])
    tree = _d66_tree_text()
    dq = re.compile(r'"([^"]+)"')
    sq = re.compile(r"(?<![A-Za-z])'([^']+ [^']+)'(?![A-Za-z])")
    bad = []
    for site, text in cells.items():
        t = " ".join(text.split())
        bad += [(site, m) for m in dq.findall(t) if m not in held]
        bad += [(site, m) for m in sq.findall(t) if m not in tree and m not in held]
    return bad


def d66_index3_faults(findings=None):
    """[(row, why)] -- the DOCKET 66 index3 decision (docstring section 8,
    H-NO-D66-ROW): index3.py seats NO row citing docket66/, because DOCKET 66's
    answer reads (0, 0, 0) in the house reading (it removes nothing and states
    no requirement in numbers of its own) and the priced requirements its
    owners state are carried on O9 and the S5 note, as M ruled the analogous
    vacuum figures (M-RULINGS-2026-10-03.md item 18, 'No, keep on O9'),
    pending M.  A row citing docket66/ without this decision moving is caught."""
    import index3
    rows = index3.FINDINGS if findings is None else findings
    return [(f[0], "cites %s" % f[4]) for f in rows if str(f[4]).startswith("docket66/")]


def p1_unblocks_faults(text=None):
    """[fault] where M-S1A-P1's unblocks cell does not say DOCKET 65 has run and
    which rows it seated, built from massform's ids."""
    text = ([r for r in RULED_BY_M if r[0] == "M-S1A-P1"][0][4]
            if text is None else text)
    want = "DOCKET 65 has run: %s (massform.py)" % D65_SEATED_IDS
    return [] if want in " ".join(text.split()) else ["missing: " + want]


@contextlib.contextmanager
def _scratch(attr, value):
    """Replace one module-level table for the duration, restored after."""
    g = globals()
    keep = g[attr]
    g[attr] = value
    try:
        yield
    finally:
        g[attr] = keep


#: DOCKET 65's POLARITY: (row, the phrase in which the seated text states a
#: DIRECTION, the owner predicate that direction reports, asked NOW).  massform
#: owns both the typed text and the flag, and either can drift alone, so each
#: seated row's text direction is tied here to the owner value it states.  Red
#: if the phrase is missing from the row or the owner disagrees.
POLARITY = (
    ("D27", "arrival switches nothing on",
     lambda: not massform.FIELD_SWITCHED_ON_BY_ARRIVAL),
    ("D28", "costs at least", lambda: massform.pair_floor_j() > 0),
    ("D28", "leaves B units of antibaryon number", lambda: massform.COUNTS["B"] > 0),
    ("D29", "has no energy to give about v",
     lambda: not massform.HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY),
    ("S10", "REFUSED, gap None", lambda: massform.MECHANISM_VERDICT[0] == REFUSED),
    # S11's text states its price per transition and its limits; it carries no
    # 'PRICED' word, so its priced direction is the stated exponent.
    ("S11", "exp(-4 pi/alpha_W) per transition", lambda: massform.ANOMALY_ROUTE_PRICED),
    ("S11", "extra leptons (D28)", lambda: massform.extra_leptons() > 0),
    ("S11", "Two-particle collisions: CONTESTED",
     lambda: massform.COLLIDER_RATE_STATUS == "CONTESTED"),
    ("S12", "Priced, not refused", lambda: massform.PAIR_ROUTE_PRICED),
    ("S13", "PRICED at eps", lambda: massform.HELD_SEAT_ROUTE_PRICED),
    ("S5", "survives M's mechanism: no mass forms at the seat",
     lambda: massform.RECONSTRUCTION_SURVIVES),
)


def polarity_faults(rows=None, table=None):
    """[(row, phrase, fault)] for every POLARITY entry whose phrase the seated
    row does not carry, or whose owner, asked now, disagrees with it."""
    table = POLARITY if table is None else table
    out = []
    for rid, phrase, owner_says in table:
        if phrase not in _row_text(rid, rows):
            out.append((rid, phrase, "phrase missing"))
        elif not owner_says():
            out.append((rid, phrase, "owner disagrees"))
    return out


def theorem_owner_disagreements():
    """[row id] of D27-D29 whose owner, asked NOW, no longer says what the
    THEOREM row says: D27 CONSIDERATION_HOLDS True; D28 the pair floor, above
    the rest energy by exactly B mu_min c^2; D29 HIGGS_FIELD_SUPPLIES_THE_
    MASS_ENERGY False.  This compares owner VALUES only.  The rows' text and
    the owner values are separate objects on massform and either can drift
    alone, so the text's DIRECTION is tied to the values by POLARITY
    (polarity_faults), checked beside this in selftest 4d."""
    row = dict((r[0], r) for r in DEMAND)
    bad = []
    if ask(row["D27"][3]) is not True:
        bad.append("D27")
    floor, rest = massform.pair_floor_j(), massform.rest_energy_j()
    pairs = massform.COUNTS["B"] * massform.MU_MIN[0] * massform.MEV_J
    if (row["D28"][3] != ("massform", "pair_floor_j") or not floor > rest
            or abs(floor - (rest + pairs)) > 1e-12 * floor):
        bad.append("D28")
    if ask(row["D29"][3]) is not False:
        bad.append("D29")
    return bad


def selftest():
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = got == want
        ok &= good
        print("  [%s] %-58s %s" % ("ok" if good else "XX", label,
                                   got if good else "%s != %s" % (got, want)))

    print("1. EVERY ROW WITH AN OWNER IS ASKED, AND THE ASK SUCCEEDS")
    asked = 0
    for rid, _claim, _st, owner, _m in DEMAND + [(a, b, c, d, e)
                                                 for a, b, c, d, e in SUPPLY]:
        if owner is not None:
            ask(owner)                       # raises if the peer dropped it
            asked += 1
    # RE-PINNED 10 -> 11: D14 (the addressing theorem, DOCKET 60) is asked of
    # certify.THEOREM_SCOPE, because the scope line IS the claim -- a device
    # specified by (Phi, m) of r alone has no parameter for a destination.
    chk("every owned row's attribute still exists on its peer", asked, 35)
    # RE-PINNED 28 -> 35 BY DOCKET 65, to what this loop counts after the
    # seating: +3 D27-D29 and +4 S10-S13, each asked of massform.py.  (The
    # finite share, seated first as O8 and folded into S10's note on M's
    # ruling M-D65-2, is no row and adds no owner here.)
    # RE-PINNED 27 -> 28 BY DOCKET 64, to what this loop counts after the
    # edit: +1 D26 (linstab.SEMICLASSICAL_EVALUABLE_ON_DEMAND).  D22 and D24
    # were already owned and are RE-OWNED (noise.CORRIDOR_APPLICATION,
    # formation.NUCLEATION_PRICEABLE_FROM_SOURCE), which moves no count.
    # RE-PINNED 11 -> 23 BY DOCKETS 62 AND 63, to what this loop counts after
    # the edit (the DOCKET 63 ruling projected 20; that was a prediction, not
    # a pin).  +6 D15-D20 and +3 S6-S8, owners as DOCKET 63 named them; +1
    # D21, the lattice theorem, asked of latticectc.py; +1 D22, fluctuation.py,
    # the board catching up with the tree; +1 S5, now asked of branelink.py
    # whether its four figures were measured -- they were not.
    # RE-PINNED 23 -> 27 by the fix pass on DOCKETS 62/63, to what this loop
    # counts: the row-opening principle (docstring section 4) applied to
    # every candidate with an instrument -- +1 D23 (transit.py), +1 D24
    # (create.py), +1 D25 (stockgate.py), +1 S9 (warpfolder.py).
    open_asked = 0
    for rid, _c, _a, owner in OPEN_ROWS:
        ask(owner)
        open_asked += 1
    chk("and every O row is asked of the instrument that narrowed it",
        open_asked, len(OPEN_ROWS))

    print("\n2. THE PEERS STILL SAY WHAT THE ROWS SAY THEY SAY")
    row = dict((r[0], r) for r in DEMAND + SUPPLY)
    chk("certify.py's scope is unmoved",
        ask(("certify", "THEOREM_SCOPE")), "static and spherically symmetric only")
    chk("foliation.py does not dispute the identity",
        ask(("foliation", "IDENTITY_DISPUTED")), False)
    chk("driven.py: the local criterion is not a scalar",
        ask(("driven", "CONTRACTION_IS_A_SCALAR")), False)
    chk("nonstatic.py: sustaining does not force rho < 0",
        ask(("nonstatic", "SUSTAINING_FORCES_NEGATIVE_RHO")), False)
    chk("drivensource.py: the corollary is NARROWED",
        ask(("drivensource", "CERTIFY_COROLLARY")).startswith("NARROWED"), True)
    chk("tolman.py does not supersede certify.py",
        ask(("tolman", "SUPERSEDES_CERTIFY")), False)
    chk("tolman.py restates it on a smaller class",
        ask(("tolman", "RESTATES_CERTIFY_ON_SMALLER_CLASS")), True)
    chk("bounds.py: the Ford-Roman saturation coding is wrong",
        ask(("bounds", "FORD_ROMAN_K_IS_WRONG")), True)
    # DOCKET 63's owners.
    for attr in ("TAIL_RATE_IS_MASS", "DISPLACEMENT_IS_ULTRALOCAL",
                 "FLAT_DIRECTIONS_ARE_INERT", "ROLE1_DOMINATED_BY_OWN_SOURCE"):
        chk("excite.py: %s" % attr, ask(("excite", attr)), True)
    chk("excite.py: the Higgs does not rebind (S7 REFUSED)",
        ask(("excite", "ROLE2_REBINDS")), False)
    chk("excite.py: the electron-mass ruler is a THEOREM on named hypotheses",
        ask(("excite", "ELECTRON_MASS_IS_A_RULER")).startswith("THEOREM given"),
        True)
    chk("higgs.py: a minimal scalar satisfies the NEC (D17, S8)",
        ask(("higgs", "MINIMAL_SCALAR_SATISFIES_NEC")), True)
    # D20 is ASKED; the ruling's 2.204772e11 is the FIXTURE it must reproduce,
    # and the ask must be the seated function's output, not a copy of it.
    # DOCKET 63 printed 2.204772e11 at the withdrawn pin 125.20; M's ruling switched
    # m_h to the READ 125.13, and the figure carries m_h^2.
    _mh = higgs.M_HIGGS / higgs.M_HIGGS_PIN_WITHDRAWN
    chk("D20 reproduces DOCKET 63's 2.204772e11 kg/m^3, rescaled by (m_read/m_pin)^2",
        abs(ask(("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18"))
            / (2.204772e11 * _mh ** 2) - 1.0) < 1e-6, True)
    # DOCKET 67 follow-ups, residue pass: S2's and B4's nuclear-density entry is
    # COMPUTED on address.RHO_NUCLEAR; the typed 7.43e-4 is a RECORD of the
    # recalled n0 = 0.1375 fm^-3 (2.3e17) with site mass m_n.
    chk("S2/B4 construction reproduces the hydrogen entry 2.72e-8 (d = a0, m = m_H)",
        "%.2e" % casimir_sheet_ratio(address.A_BOHR_M, 1.6735575e-27), "2.72e-08")
    chk("  nuclear entry computed on address.RHO_NUCLEAR (n0 0.16/fm^3 x m_p): 7.83e-4",
        NUCLEAR_SHEET_RATIO_TEXT, "7.83e-4")
    chk("  RECORD: as first written, 7.43e-4, at n0 = 0.1375/fm^3 with m_n",
        "%.2e" % casimir_sheet_ratio(N0_RECALLED_PER_M3 ** (-1.0 / 3.0), M_NEUTRON_KG),
        "%.2e" % NUCLEAR_SHEET_RATIO_AS_FIRST_WRITTEN)
    chk("  and S2 and B4 print the computed entry, the typed one only as 'first'",
        (NUCLEAR_SHEET_RATIO_TEXT + " at nuclear density" in _row_text("S2"),
         "nuclear density " + NUCLEAR_SHEET_RATIO_TEXT in
         " ".join(r[3] for r in balance() if r[0] == "B4"),
         "positronium, 7.43e-4" in _row_text("S2")),
        (True, True, False))
    chk("  still below 1: the refusal does not move", NUCLEAR_SHEET_RATIO < 1.0, True)
    # DOCKET 67 follow-ups: D20's G_F status word is asked of higgs.py, which
    # READ it (PDG 2024 Table 1.1); the old word survives only in the quote.
    _d20 = _row_text("D20")
    chk("  D20's G_F status is higgs.STATUS_D67's READ, the old word only quoted",
        (higgs.STATUS_D67["G_FERMI"], "G_F is READ (PDG 2024 Table 1.1" in _d20,
         _d20.count("G_F is NAMED-NOT-READ"),
         "this read 'G_F is NAMED-NOT-READ'" in _d20),
        ("READ", True, 1, True))
    chk("  and it IS address.source_density at the fixture's eps",
        ask(("excite", "HOLD_HIGGS_DERIVED_KG_M3_AT_EPS_1E18")),
        address.source_density(excite.EPS_AT_FIXTURE, 1.0)[1])
    chk("W9-W13 are asked of their owners, not retyped",
        ([r[1:] for r in WITHDRAWN_ROWS[-4:]]
         == [address.WITHDRAWN[k] for k in ("W10", "W11", "W12", "W13")],
         WITHDRAWN_ROWS[-5][2] == "; ".join(excite.W9[1])), (True, True))
    chk("  and each W10-W13 claim is withdrawn on its owner too",
        (address.OPTICAL_OPTICAL_IS_EXACTLY_BLIND,
         address.K_ALPHA_H1_IS_NEGATIVE,
         address.SOURCE_TO_FIELD_IS_QUARTER_OVER_EPS,
         address.SAME_OBSTRUCTION_EVERY_ROLE), (False, False, False, False))
    # DOCKET 62's owners.
    chk("latticectc.py: the lattice theorem is a THEOREM (D21)",
        ask(("latticectc", "LATTICE_THEOREM_STATUS")), THEOREM)
    chk("  with its hypotheses named", len(latticectc.HYPOTHESES), 3)
    chk("  and GKLP's 'no' forced, the spacelike rank-2 span CTC-free",
        (latticectc.GKLP_NO_IS_FORCED, latticectc.RANK2_SPACELIKE_SPAN_HAS_CTC,
         latticectc.RANK2_TIMELIKE_SPAN_HAS_CTC), (True, False, True))
    chk("DOCKET 57's two routes are NOT independent at codimension one",
        latticectc.DOCKET57_ROUTES_INDEPENDENT_AT_CODIM1, False)
    # D22, DOCKET 64 (ruling C): the row is asked of noise.py now.  Its status
    # is THIS file's ruling, and the check ties it to the owner's own word, so
    # a noise.py that moved its corridor application off SURVEY turns it red.
    chk("noise.py: C1 is a THEOREM in the flat model, and D22's status IS "
        "noise.CORRIDOR_APPLICATION",
        (noise.C1_FLAT_THEOREM, ask(("noise", "CORRIDOR_APPLICATION")),
         row["D22"][2] == noise.CORRIDOR_APPLICATION), (True, SURVEY, True))
    chk("  the curved part is carried by an existing OPEN row (O2), not a new "
        "one",
        (noise.CURVED_PART_CARRIED_BY in [r[0] for r in OPEN_ROWS],
         noise.ROW_TO_OPEN), (True, None))
    chk("  and noise.py no longer claims to decide D22 (DECIDES_D22 withdrawn)",
        (noise.DECIDES_D22, "DECIDES_D22 = True" in noise.WITHDRAWN),
        (False, True))
    chk("  H2 fails on the corridor: (b/l_G)^2 = noise.B_OVER_LG_SQUARED > 1, "
        "and the owner agrees",
        (noise.B_OVER_LG_SQUARED > 1.0, noise.H2_SATISFIED_BY_CORRIDOR),
        (True, False))
    chk("  D22 prints the owner's figures at the precision the ruling named",
        all(t in row["D22"][1] for t in (
            "%.6f C/tau^4" % noise.SD0_OVER_C,
            "%.6f beta" % noise.TAU_STAR_OVER_BETA,
            "(b/l_G)^2 = %.0f" % noise.B_OVER_LG_SQUARED)), True)
    # The EL-surrogate bound: the ruling typed exp(-10^142) and computation
    # refutes it (noise.CORRECTED).  The exponent printed is floor() of the
    # owner's computed log10(-ln P), so it cannot drift from the owner.
    _el = int(math.floor(noise.EL_VACUUM_LOG10_NEG_LN_P))
    chk("  the EL-surrogate bound D22 prints is the owner's computed one",
        (("below exp(-10^%d)" % _el) in row["D22"][1],
         noise.EL_VACUUM_BELOW_EXP_MINUS_10_141 == (_el == 141),
         noise.EL_VACUUM_BELOW_EXP_MINUS_10_142), (True, True, False))
    chk("fluctuation.py does not price the corridor, and that stays true of "
        "fluctuation.py (D22 is no longer asked of it)",
        (ask(("fluctuation", "PRICES_THE_CORRIDOR")), row["D22"][3][0]),
        (False, "noise"))
    chk("  and its bound is sign-blind and needs no diagonal G",
        (fluctuation.POINTWISE_DELTA_DISCRIMINATES_SIGN,
         fluctuation.BOUND_NEEDS_DIAGONAL_G), (False, False))
    chk("branelink.py: S5's four figures are NOT measured (S5 stays OPEN)",
        ask(("branelink", "S5_FIGURES_MEASURED")), False)
    # The principle's rows (docstring section 4), each asked of its owner.
    chk("transit.py: the traversal is moved earlier, not removed (D23)",
        (ask(("transit", "TRAVERSAL_IS_REMOVED")), transit.BEATS_LIGHT),
        (False, False))
    chk("  and S5's note carries D23's amortisation reading",
        ("AMORTISATION SCHEME" in row["S5"][4],
         ("%.4g years" % PROXIMA_LY) in row["S5"][4]), (True, True))
    chk("create.py: nucleation is NOT-RUN (create.py's own word, unmoved)",
        create.NUCLEATION_STATUS, "NOT-RUN")
    # D24, DOCKET 64.  The ruling asked for NUCLEATION_PRICEABLE_FROM_SOURCE
    # = False; formation.py's verification withdrew that (not a proved
    # obstruction) and the owner now says NOT DETERMINED.  The weaker word is
    # the one asked, and the row stays OPEN because the price is not computed.
    chk("formation.py: nucleation READ, not computed, priceability NOT "
        "DETERMINED -- so D24 stays OPEN",
        (ask(("formation", "NUCLEATION_PRICEABLE_FROM_SOURCE")),
         formation.NUCLEATION_PRICED, formation.NUCLEATION_NECK_EXPLICIT,
         row["D24"][2]), (formation.NOT_DETERMINED, False, False, OPEN))
    chk("  and the withdrawn 'cannot be priced' is kept on the owner",
        formation.NUCLEATION_PRICEABLE_FROM_SOURCE_WITHDRAWN[0], False)
    chk("  D24 prints F1's and F2's hypotheses as the owner names them",
        ("; ".join(formation.F1_THEOREM) in row["D24"][1],
         formation.H_NULL in row["D24"][1],
         set(formation.F2_THEOREM) - set(formation.F1_THEOREM)
         == {formation.H_NULL}), (True, True, True))
    chk("  and the D4 observation is the owner's computed flag",
        ("PHASE1_D4_POINTWISE_DURING_PASSAGE = %s"
         % formation.PHASE1_D4_POINTWISE_DURING_PASSAGE) in row["D24"][1],
        True)
    chk("  exotic matter does not help creation; no escape stays in GR",
        (create.EXOTIC_MATTER_HELPS_CREATION,
         create.any_escape_stays_in_lorentzian_gr()), (False, False))
    chk("stockgate.py: D25's claim quotes the gate its owner states",
        ask(("stockgate", "GATE")) in row["D25"][1], True)
    chk("  and its binder is the one stockgate.py computes for a CI chondrite",
        ("binds on %s at %.4g"
         % stockgate.binding_under("as-composed 59", "CI chondrite"))
        in row["D25"][1], True)
    # D25, DOCKET 64: stays OPEN; formation.py narrows nothing and its
    # verification withdrew both "NARROWED" and "no confirmed condensed
    # reservoir".  stockgate's figures appear ONCE (over-representation).
    _bind = "%.4g" % stockgate.binding_under("as-composed 59",
                                             "CI chondrite")[1]
    chk("D25 stays OPEN, printing formation.D25_VERDICT, and stockgate's "
        "figure appears once",
        (row["D25"][2], formation.D25_VERDICT in row["D25"][1],
         formation.D25_VERDICT.startswith("OPEN AND UNCHANGED"),
         row["D25"][1].count(_bind)), (OPEN, True, True, 1))
    chk("  the survey names a CONDENSED body; primitive and accessible are "
        "unmeasured; no reservoir is claimed either way",
        (formation.SURVEY_CONDENSED_BODY_FOUND,
         formation.SURVEY_PRIMITIVE_MEASURED,
         formation.SURVEY_ACCESSIBLE_MEASURED,
         formation.SURVEY_CONFIRMED_RESERVOIR,
         formation.SURVEY_CONFIRMED_RESERVOIR_WITHDRAWN[0]),
        (True, False, False, formation.UNDETERMINED, False))
    chk("  and the aperture hit count D25 prints is the owner's",
        ("%d files hit" % len(set(formation.APERTURE_HITS)
                              | set(formation.APERTURE_SYNONYM_HITS)))
        in row["D25"][1], True)
    # DOCKET 67 follow-ups: the 1-4 au belt's status is asked of formation.py
    # (evidence removed READ, excluded COMPUTED False, its hypotheses named),
    # and the wording it replaces survives only as the quoted correction.
    _d25 = row["D25"][1]
    chk("  D25's belt: evidence removed (READ), not excluded (computed), "
        "H_unres/H_peak/H_3sig named, old wording only quoted",
        (formation.SURVEY_BELT_1_4AU_EVIDENCE_REMOVED_BY_SOURCE,
         formation.SURVEY_BELT_1_4AU_EXCLUDED_BY_SOURCE,
         formation.SURVEY_BELT_1_4AU_EXCLUDED_BY_SOURCE
         == formation.belt_excluded(formation.BELT_ANGLADA_UJY),
         "excluded by the source = %s" % formation.belt_excluded(
             formation.BELT_ANGLADA_UJY) in _d25,
         "%.2f sigma below" % formation.belt_sigma_low(
             formation.BELT_PHOTOSPHERE_UJY + formation.BELT_ANGLADA_UJY) in _d25,
         all(h in _d25 for h in ("H_unres", "H_peak", "H_3sig")),
         _d25.count("about 2 sigma against it"),
         "this read 'about 2 sigma against it" in _d25),
        (True, False, True, True, True, True, 1, True))
    # D26, DOCKET 64: opened by the docket that built its instrument.
    # A GREEN BOARD OVER A RED OWNER is what the ownership contract forbids
    # (DOCKET 64 seating verifier): D26's typed flag alone cannot see linstab's
    # scan go red.  So the board re-runs the owner's own scan, over the owners
    # the board itself names, and requires the verdict False with nothing unread.
    _owners = linstab.demand_owners()[0]
    chk("linstab's scan, re-run by the board: verdict False and no unread hit",
        linstab.semiclassical_evaluable_on_demand(
            linstab.self_consistency_scan(_owners), _owners), (False, []))
    chk("linstab.py: D26 is OPEN because the semiclassical sector is not "
        "evaluable on any demand configuration",
        (ask(("linstab", "SEMICLASSICAL_EVALUABLE_ON_DEMAND")),
         row["D26"][2], linstab.D26_STATUS), (False, OPEN, OPEN))
    chk("  its text and answer are the owner's, not retyped",
        (row["D26"][1].startswith(linstab.D26_CLAIM),
         row["D26"][4] == linstab.D26_ANSWERED_BY), (True, True))
    chk("  classical radial THEOREM, infimum -1/4, the wall formula at u",
        (linstab.CLASSICAL_RADIAL_STATUS, linstab.BETA2_CRIT_INFIMUM,
         linstab.DEVICE_IS_WALL_FORMULA_AT_U), (THEOREM, "-1/4", True))
    chk("  the IFF is narrowed and 'recorded or shown' replaces a proof",
        ("recorded or shown" in linstab.D26_CLAIM,
         "GMMPS's reported" in linstab.D26_CLAIM,
         linstab.ALPHA_ZERO_ROOT_GROWTH), (True, True, OPEN))
    chk("  hpscentre is one of the scan's positive controls",
        "hpscentre" in linstab.POSITIVE_CONTROLS, True)
    chk("warpfolder.py: the flash is not a reconstruction mechanism (S9)",
        ask(("warpfolder", "FLASH_IS_A_RECONSTRUCTION_MECHANISM")), False)
    chk("  heating restores the symmetry; the budget is unconnected",
        (warpfolder.HEATING_TO_EW_SCALE_RESTORES_SYMMETRY,
         warpfolder.ENERGY_BUDGET_IS_CONNECTED_TO_THE_CHAIN), (True, False))
    chk("  S9's shortfall is warpfolder.shortfall() at its first payload",
        ("short by %.1f orders"
         % math.log10(warpfolder.shortfall(warpfolder.PAYLOADS_KG[0])))
        in row["S9"][4], True)
    chk("  and both NOT-ADJUDICATED claims are named in S9, not given rows",
        (all(n in row["S9"][4] for n in warpfolder.NOT_ADJUDICATED),
         len(warpfolder.NOT_ADJUDICATED)), (True, 2))
    chk("every OPEN demand row has an instrument (the principle's first half)",
        [r[0] for r in open_demand() if r[3] is None], [])
    chk("every question waiting for its instrument names what opens it",
        all(bool(w[2]) for w in WAITS_FOR_ITS_INSTRUMENT), True)
    chk("  and none of them is also a row",
        [w[0] for w in WAITS_FOR_ITS_INSTRUMENT
         if any(w[0] in r[1].lower() for r in DEMAND + SUPPLY)], [])
    # Those two rows are vacuous on an empty list, so the move itself is
    # checked: what left the list is a row now, and the row it names exists.
    chk("linearised stability left the waiting list and IS a row (D26)",
        ([w[0] for w in WAITS_FOR_ITS_INSTRUMENT],
         [(q, rid, rid in row and q in row[rid][1].lower())
          for q, _d, rid, _w in OPENED_FROM_WAITING]),
        ([], [("linearised stability", "D26", True)]))
    chk("  and LEDGER.md prints 'None.' rather than dropping the section",
        "### Not opened: waiting for its instrument\n\nA question with no "
        "instrument is opened by the docket that builds\none (the principle "
        "in `ledger.py`'s docstring, section 4).\n\n**None.**"
        in to_markdown(), True)
    # The phase1 D4 question (DOCKET 64 ruling D.2) is recorded for M, not
    # applied.  Its premise is computed on both owners, so it can fail.
    # M RULED on the phase1 D4 question: restate.  Each premise is computed on the
    # owners, so a revert of phase1.py or formation.py fails here.
    chk("the phase1 D4 question is RULED and APPLIED, on computed premises",
        ([p[0] for p in RULED_BY_M], [p[0] for p in PENDING_RULINGS],
         phase1.D4_RESTATED_ON_M_RULING,
         phase1.is_transition(True, True, True, True, True),
         phase1.is_transition(False, True, True, True, True, net_momentum=True),
         phase1.is_transition(False, True, True, True, True, passage_flux=True),
         formation.PHASE1_D4_POINTWISE_DURING_PASSAGE),
        # RE-PINNED BY DOCKET 68 (M: "1 then 2 then 3 then 4"): + M-D68-1..10
        # and M-D68-C1..C8 (D68_RULED), and the one pending question,
        # M-D68-P1 (asked of M and unanswered in CHARTER.md).
        # RE-PINNED BY THE DOCKET 68 RESIDUALS: + M-D68-11 (item 11, M's
        # novelty gate); M-D68-C4, C6 and C7 OFF this list -- M's instruction,
        # proposal and statement, carried by the charter and not rulings, now
        # in D68_CARRIED (pinned below), never counted here.
        # RE-PINNED WHEN M-D68-P1 WAS CONVERTED: + M-D68-C12 (M had answered
        # the ER = EPR citation question before DOCKET 68 opened; item 14),
        # and the pending list empties -- nothing is pending M.
        # RE-PINNED WITH ITEMS 12 AND 13: + M-D68-12 and M-D68-13, M's rulings
        # on the paper ("Correct it", "Scope it"), seated after M-D68-11.
        # RE-PINNED BY DOCKET 68 WAVE 2: + M-D68-15 and M-D68-16 (items 15-16,
        # the retrieval route; 15 superseded by 16, kept as history), seated
        # after M-D68-13.  Item 14 is M-D68-C12.
        # RE-PINNED WITH M'S DOCKET 66 RULINGS (R-seat): + M-D68-26, M-D68-27
        # and M-D68-28 (items 26-28: the paper's Gott bound, spec.py's TURN,
        # re-grading D68), appended to D68_RULED after M-D68-C12.
        # RE-PINNED WITH WAVE 3 AND STEP 1b (W3S1B-seat, M: "Seat both
        # (Recommended)", item 36): + M-D68-22, 24, 29, 30, 33, 34 and 36,
        # M's answers to questions put (items 22-24 of 2026-10-04 first seated
        # here); items 21, 23, 25, 31, 32 and 35 are D68_FILE_CARRIED, not
        # counted.
        # RE-PINNED WITH STEP 1c (S1C-seat, item 39's step 1): + M-D68-37,
        # 38 and 39, M's answers on Step 1c.
        # RE-PINNED WITH THE D68 CLOSE (D68-close): + M-D68-40.
        # RE-PINNED WITH THE CMB SEATING (CMB-seat, M: "Seat it, then medium",
        # item 45): + M-D68-42, 43 and 45; items 41 and 44 are D68_FILE_CARRIED.
        # RE-PINNED WITH READINGS 2 AND 3 AND THE LOCAL CLOCKS (CMB2-seat, M:
        # "3, then 2, then 1 please", item 54): + M-D68-47, 49, 51, 53 and 54;
        # items 46, 48, 50 and 52 are D68_FILE_CARRIED.
        # RE-PINNED WITH SUPPORT.PY AND BIAS.PY (CMB3-seat, M: "Seat both",
        # item 55): + M-D68-55.
        (["M-D64-1", "M-S1A-P1", "M-S1A-P2", "M-S1A-P3", "M-S1A-P4",
          "M-S1A-P5", "M-D65-1", "M-D65-2", "M-D65-3", "M-D65-4", "M-D65-5",
          "M-D67-1", "M-D67-2"]
         + ["M-D68-%d" % i for i in list(range(1, 14)) + [15, 16]]
         + ["M-D68-C%d" % i for i in (1, 2, 3, 5, 8, 12)]
         + ["M-D68-%d" % i for i in (26, 27, 28)]
         + ["M-D68-%d" % i for i in (22, 24, 29, 30, 33, 34, 36)]
         + ["M-D68-%d" % i for i in (37, 38, 39, 40)]
         + ["M-D68-%d" % i for i in (42, 43, 45)]
         + ["M-D68-%d" % i for i in (47, 49, 51, 53, 54, 55)], [],
         True, False, False, True, False))

    print("\n3. THE EXCHANGE RATE, RE-DERIVED FROM ASKED CONSTANTS")
    chk("Lambda is overturn.py's", LAMBDA, overturn.LAMBDA)
    chk("c^2/(G Lambda) reproduces the tree's 1.348948e26 to 7 figures "
        "(arithmetic; G fixes about 5)",
        round(EXCHANGE_RATE / 1e26, 6), 1.348948)
    chk("and the Proxima demand reproduces 5.4194e42 kg to 5 figures "
        "(arithmetic; the J2016.0 parallax's sigma fixes about 4)",
        round(required_negative_mass(PROXIMA_M) / 1e42, 4), 5.4194)

    print("\n4. THE LEDGER'S OWN SHAPE")
    c = statuses()
    # RE-PINNED BY DOCKETS 60 AND 61, and every move is a row this file got
    # wrong or a row a docket answered -- not growth.
    #   THEOREM 11 -> 11: D14 arrives, D13 leaves for THEOREM-NARROWED.
    #   MEASURED 3 -> 2: S5 downgraded, because the four figures it was seated
    #     on occur in NO file in this tree.  Measured by grep, all four absent.
    #   OPEN 3 -> 7: O1 closes (refused), O4-O7 arrive, and S5 joins as open.
    #   WITHDRAWN 6 -> 8: W7 and W8, both of them DOCKET 61's own passes.
    #   REFUSED 3 -> 4: the closed row counts here, not as an opening.
    chk("the status census", c,
        {THEOREM: 20, NARROWED: 1, MEASURED: 3, SURVEY: 2, OPEN: 14,
         WITHDRAWN: 13, REFUSED: 10})
    # RE-PINNED BY DOCKET 68 (M: "1 then 2 then 3 then 4") to what statuses()
    # returned after the seating: OPEN 13 -> 14, O9 (the two classical bits,
    # asked of combine.py).  The notes on S5, S10, S13, D23 and D25 move no
    # status; M-D68-* are rulings (M-D68-P1, first pending, is now the ruling
    # M-D68-C12), not statuses.
    # RE-PINNED BY DOCKET 65 to what statuses() returned after the seating
    # (M: "Seat as proposed"), every status asked of massform.PROPOSED_ROWS:
    #   THEOREM 17 -> 20: D27, D28, D29.
    #   OPEN 10 -> 13: S11, S12, S13 (priced remainders).  S5 stays OPEN;
    #     its note is appended to, not moved.  The seating first opened the
    #     finite Higgs share as O8 and statuses() gave 14; M ruled M-D65-2
    #     ('Fold into S10 (Recommended)'), O8 left OPEN_ROWS for S10's note,
    #     and this is RE-PINNED 14 -> 13 to what statuses() returned after it.
    #   REFUSED 9 -> 10: S10, M's mechanism as a supply (gap None).
    #   M-D65-1 and M-D65-2 are rulings, not statuses, and move no count.
    # RE-PINNED BY DOCKET 64 to what statuses() returned after the edit (not
    # typed from the ruling, which did not predict it).  The moves only:
    #   D22 OPEN -> SURVEY (noise.py: C1 a THEOREM in the flat model; the
    #     corridor application a SURVEY).       SURVEY 1 -> 2, OPEN -1.
    #   D26 new, OPEN (linstab.py).             OPEN +1, so OPEN 10 -> 10.
    #   Linearised stability left WAITS_FOR_ITS_INSTRUMENT (not a status).
    #   O5 re-owned to hpscentre.py; D24 re-owned to formation.py.
    #   No row closed, none withdrawn, none refused.
    # RE-PINNED BY THE FIX PASS ON DOCKETS 62/63, to what statuses() returns:
    #   OPEN 7 -> 10: D23 (the first trip, transit.py), D24 (formation,
    #     create.py), D25 (the destination stock gate, stockgate.py) -- the
    #     principle: a question the tree already has an instrument for gets a
    #     row now.  Linearised stability has no instrument and is NOT opened;
    #     it is in WAITS_FOR_ITS_INSTRUMENT, for the calculations docket.
    #   REFUSED 8 -> 9: S9, warpfolder.py's device specification as a supply.
    # AND WHY NONE OF DOCKET 63's SECTION E IS AN O ROW (its census said "OPEN
    # 6 plus the O rows added from E").  The thirteen are unsettled questions
    # INTERNAL to the refused rows S6-S8 and to D20's figure, and E12 says in
    # terms that the H1/H2 split gates nothing: every verdict in B holds under
    # both hypotheses.  Read one by one, none gates a requirement --
    #   E1 cheapest stable source and E10 the Yukawa-running correction MOVE
    #     D20's MEASURED figure, which D20 already names as what would move it;
    #     S6 and S7 are refused on kind, not on that price.
    #   E2 fermion bag, E3 f = -2.45, E4 in-medium massless point, E5
    #     evanescent reach, E7 release of a phi = 0 region, E8 hot restored
    #     region, E11 macroscopic gauged configuration: each is a way the
    #     displacement might be sourced, held or extended, and each still
    #     needs a source filling the region (D16), so S6-S8 stand either way.
    #   E6 curvature sourcing is the xi != 0 case, which is S4 and O1, both
    #     refused already; E13 a BSM dilaton is outside the docket's subject.
    #   E9 endpoint.py's E1/E3a/E3 checks verify an instrument, and no row on
    #     this board is asked of those theorems -- the board asks endpoint.py
    #     only for Degrassi's scale, in S8's note.
    # Opening them would count one refusal's internal questions as openings,
    # which is the inflation S4's four wrong words once caused.
    # RE-PINNED BY DOCKETS 62 AND 63 to what statuses() returns after the edit.
    # The DOCKET 63 ruling's projection (THEOREM 16, OPEN 6 plus E) and the
    # DOCKET 62 ruling's (UNCHANGED) were predictions, and each was made
    # without the other docket or the fluctuation row:
    #   THEOREM 11 -> 17: D15-D19 (DOCKET 63) and D21 (DOCKET 62's lattice
    #     theorem, seated as its own row).
    #   MEASURED 2 -> 3: D20.
    #   OPEN 6 -> 7: D22, fluctuation.py.  DOCKET 62 closed none of O2, O3,
    #     O5, O6, O7 and opened nothing; S5 stays open.
    #   WITHDRAWN 8 -> 13: W9-W13.
    #   REFUSED 5 -> 8: S6-S8.
    # O4 joins O1: OPEN 7 -> 6, REFUSED 4 -> 5.  axial.py answered it in the
    # negative -- the axis costs the same sign the sphere does.
    chk("rows that left OPEN by being ANSWERED, kept rather than deleted",
        sorted(r[0] for r in CLOSED_ROWS), ["O1", "O4"])
    chk("and no id appears in two lists at once",
        len(set([r[0] for r in OPEN_ROWS] + [r[0] for r in CLOSED_ROWS])),
        len(OPEN_ROWS) + len(CLOSED_ROWS))
    chk("every closed row says how it closed",
        all(bool(r[2]) for r in CLOSED_ROWS), True)
    chk("every status used is one of the five plus REFUSED",
        set(r[2] for r in DEMAND + SUPPLY) <= set(STATUSES), True)
    chk("every demand row names what would move it",
        all(bool(r[4]) for r in DEMAND), True)
    chk("every open row names what would answer it",
        all(bool(r[2]) for r in OPEN_ROWS), True)
    chk("every withdrawn row names why it fell",
        all(bool(r[2]) for r in WITHDRAWN_ROWS), True)
    chk("the unaskable rows are named, not hidden", unaskable(),
        ("D5", "D6", "D12", "D13"))

    print("\n4b. DOCKET 62 CLOSED NOTHING, AND WHAT IT REFUSED IS NOT HERE")
    # DOCKET 68: O9's owner pins no closing flag, so its closing is the
    # owner's computed reading (OPEN_ROW_READINGS); every other row's flag.
    chk("no O row's owner says it closed",
        [r[0] for r in OPEN_ROWS if open_row_answer(r)[1]], [])
    chk("the five narrowed rows are all still open",
        [r for r in DOCKET62_NARROWED if r not in [x[0] for x in OPEN_ROWS]], [])
    # DOCKET 65 opens no O row: the finite Higgs share, first seated as O8, is
    # an OPEN item in S10's note on M's ruling M-D65-2.  The five are asked for
    # by name (DOCKET62_NARROWED), and no other O row stands beside them.
    # RE-PINNED BY DOCKET 68: O9 stands beside them (docstring section 7).
    chk("  and the only O row beside them is DOCKET 68's O9 (O8 folded into "
        "S10's note, M-D65-2)",
        sorted(r[0] for r in OPEN_ROWS if r[0] not in DOCKET62_NARROWED), ["O9"])
    # RE-KEYED BY DOCKET 64 (ruling C, O5).  This compared sorted ids with the
    # OPEN ids, and O5's second entry (DOCKET 64 replacing DOCKET 62's
    # wording) would have turned it red for a correct reason.  Entries are
    # keyed by (row, docket) now, and the check is on SETS.
    chk("every narrowed row's replaced wording is kept (as sets)",
        set(DOCKET62_NARROWED) <= set(r[0] for r in SUPERSEDED_WORDING),
        True)
    chk("  DOCKET 62's entries are exactly the five O rows it narrowed",
        sorted(r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 62"),
        sorted(DOCKET62_NARROWED))
    chk("  DOCKET 64's are the rows whose wording it replaced, not extended",
        sorted(r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 64"),
        ["D22", "D24", "O5"])
    chk("  DOCKET 65's is S5's replaced first sentence (it was the only priced "
        "row), and the sentence is no longer on S5",
        ([r[2] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 65"],
         [r[0] for r in SUPERSEDED_WORDING if r[1] == "DOCKET 65"],
         any("THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL" in r[4]
             for r in SUPPLY if r[0] == "S5")),
        (["THE ONLY ROW ON THIS LEDGER WITH A PRICE RATHER THAN A REFUSAL"], ["S5"],
         False))
    chk("  the section header names the dockets the table holds, built from it",
        (superseded_dockets(),
         "## Row wording replaced by DOCKETS 62, 64 and 65" in to_markdown()),
        ("62, 64 and 65", True))
    chk("  CONTROL: the table without its DOCKET 65 entry would print the old "
        "header, '62 and 64' (built, not typed)",
        superseded_dockets([r for r in SUPERSEDED_WORDING if r[1] != "DOCKET 65"]),
        "62 and 64")
    chk("  no (row, docket) key is used twice",
        _superseded_keys_unique(SUPERSEDED_WORDING), True)
    chk("  CONTROL: a duplicated (row, docket) key is caught",
        _superseded_keys_unique(SUPERSEDED_WORDING + SUPERSEDED_WORDING[:1]),
        False)
    chk("  every superseded id is a row on this board",
        [r[0] for r in SUPERSEDED_WORDING
         if r[0] not in [x[0] for x in DEMAND + SUPPLY + OPEN_ROWS]], [])
    chk("and each says why it was replaced",
        all(bool(r[3]) for r in SUPERSEDED_WORDING), True)
    chk("  O5's DOCKET 62 wording is kept verbatim as the board printed it",
        [r[2] for r in SUPERSEDED_WORDING
         if r[:2] == ("O5", "DOCKET 64")],
        [O5_DOCKET62[0] + " || " + O5_DOCKET62[1]])
    ids = [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS + CLOSED_ROWS
           + WITHDRAWN_ROWS]
    chk("no R-1 row (it is O7 renamed) -- and its owner agrees",
        ("R-1" in ids, branelink.R1_ROW_OPENED), (False, False))
    chk("no separate NEC-everywhere row (it is O3 with a clause)",
        latticectc.NEC_EVERYWHERE_ROW_OPENED, False)
    chk("no Caldwell & Langlois withdrawal (it has no referent)",
        (latticectc.CALDWELL_LANGLOIS_WITHDRAWAL_SEATED,
         any("Caldwell" in r[1] for r in WITHDRAWN_ROWS)), (False, False))
    chk("no id is used twice anywhere on the board",
        len(ids), len(set(ids)))
    # The refused figures: the curvature-tightened persistence shortfall, its
    # redshift-loosened variant, and the void 9/64 adjustment.  Rendered
    # nowhere.  The needles are the owner's own computed values, so this fires
    # if any is ever printed at the precision the ruling refused.
    flat, curved, loosened = fewsterteo.refused_figures()
    md = to_markdown()
    needles = ["%.3f" % curved, "%.3f" % loosened,
               "%.6f" % fewsterteo.refused_void_adjustment(),
               "%.3f" % fewsterteo.WITNESS_ORDERS]
    chk("the refused figures appear nowhere in LEDGER.md",
        [n for n in needles if n in md], [])
    chk("  CONTROL: the needle search finds the figure that stands",
        "%.3f" % flat in md, True)
    chk("  CONTROL: and fires on a copy with a refused figure planted",
        [n for n in needles if n in md + needles[0]], needles[:1])
    chk("the 9/64 is not applied to C_F, on its owner",
        fewsterteo.NINE_64_APPLIES_TO_C_F, False)
    # O5, DOCKET 64: re-owned to hpscentre.py; every figure asked.
    o5 = [r for r in OPEN_ROWS if r[0] == "O5"][0]
    chk("O5 is asked of hpscentre.py, which says it did not close",
        (o5[3], ask(o5[3]), throatmass.O5_CLOSED),
        (("hpscentre", "O5_CLOSED"), False, False))
    chk("  m < 0 found in HPS's system, NOT inside the established domain",
        (hpscentre.M_NEGATIVE_FOUND_IN_HPS_SYSTEM,
         hpscentre.M_NEGATIVE_FOUND_INSIDE_DOMAIN,
         hpscentre.THROAT_M_NEGATIVE_READING, hpscentre.AHS_REACHED),
        (True, False, "CONSERVED", False))
    chk("  which system HPS integrated is NOT DETERMINED (the claim withdrawn)",
        (hpscentre.HPS_INTEGRATED_THE_PRINTED_SYSTEM,
         "NOT DETERMINED" in o5[1]), ("NOT DETERMINED", True))
    # The two instruments found the repairs independently; this compares
    # qeihps.py's scan with hpscentre.py's printed -> conserved change, so a
    # disagreement between the peers turns it red.
    chk("  qeihps.py's two repairs ARE hpscentre.py's printed -> conserved",
        (qeihps.REPAIR_CONSERVATION[2:],
         qeihps.REPAIR_DIMENSION[2:],
         hpscentre.PRINTED["a_th"] == hpscentre.CONSERVED["a_th"]),
        ((hpscentre.PRINTED["a_tt"], hpscentre.CONSERVED["a_tt"]),
         (_hps_ll_denominator(hpscentre.PRINTED["ll_pow"]),
          _hps_ll_denominator(hpscentre.CONSERVED["ll_pow"])), True))
    chk("  the first m < 0 is printed as the owner pins it, in l_P",
        ("first at %.4f l_P" % hpscentre.FIRST_NEGATIVE_M_THROAT_LP) in o5[1],
        True)
    chk("  the throat-geodesic verdict is qeihps.py's 'NOT A TEST'",
        (qeihps.VERDICT_THROAT_GEODESIC.startswith("NOT A TEST"),
         ("On the throat geodesic: " + qeihps.VERDICT_THROAT_GEODESIC)
         in o5[1]), (True, True))
    # CORRECTED (DOCKET 67 follow-ups): this label read "(FO and FFKP both
    # OPEN)", true before M's ruling added the Hadamard hypothesis in qeihps;
    # the owner now REFUSES both on the Hadamard clause, OPEN only were HPS's
    # state Hadamard -- asked of the owner below, not of the label.
    chk("  Kontou's test is the owner's (FO and FFKP both REFUSED on the "
        "Hadamard clause; OPEN if Hadamard), F-S REFUSED",
        (qeihps.KONTOU_REQUEST_FOUND,
         qeihps.KONTOU_REQUESTED_TEST_ON_HPS in o5[1],
         qeihps.FEWSTER_SMITH_ON_HPS.startswith("REFUSED"),
         qeihps.DOCKET62_INSTRUMENT_STANDS), (True, True, True, False))
    chk("  FO and FFKP REFUSED on HPS's state, Hadamard NOT-ESTABLISHED, "
        "OPEN/OPEN only were it Hadamard (asked of qeihps)",
        (qeihps.FO_ON_HPS.startswith("REFUSED"),
         qeihps.FFKP_IV1_ON_HPS.startswith("REFUSED"),
         qeihps.HPS_STATE_HADAMARD_ESTABLISHED,
         sorted(v[0] for v in qeihps.CONDITIONAL_IF_HADAMARD.values())),
        (True, True, False, ["OPEN", "OPEN"]))
    chk("  O5's prose and hpscentre's answer name the Hadamard blocker",
        ("REFUSED on HPS's state as published" in o5[1],
         "NOT-ESTABLISHED" in o5[1],
         "HPS's state established Hadamard" in hpscentre.O5_ANSWERED_BY,
         "apply in form only where their hypotheses do -- FO needs global "
         "hyperbolicity, FFKP" in o5[1]),
        (True, True, True, False))
    _tm = "-- %s, not NO" % throatmass.NEGATIVE_MASS_SELF_CONSISTENT_FOUND
    chk("  throatmass's NOT-FOUND is no longer printed as the tree's finding",
        (_tm in o5[1], _tm in O5_DOCKET62[0]), (False, True))
    chk("  and O5 answers with hpscentre.O5_ANSWERED_BY, not throatmass's",
        o5[2], hpscentre.O5_ANSWERED_BY)
    chk("O5's narrowing #3 is demoted on its owner",
        (throatmass.NO_QEI_CAN_BOUND_RHO_REN,
         throatmass.SEPARATES_O5_FROM_O2_PERMANENTLY), (False, False))
    chk("O7's B is unmeasured on its owner", branelink.B_MEASURED, False)
    o6 = [r for r in OPEN_ROWS if r[0] == "O6"][0][1]
    chk("O6 says its saving is at the UNTESTED B = 0, figure from branelink",
        ("UNTESTED B = 0" in o6,
         ("%.1f ns" % branelink.SAVING_AT_B0_NS) in o6), (True, True))
    s8 = [r for r in SUPPLY if r[0] == "S8"][0][4]
    chk("S8 prints excite.py's full band and its centre, not the ruling's",
        all(("%.0e" % v) in s8 for v in excite.XI_FIELD_OVER_INSTABILITY),
        True)
    chk("O6's cause of death is refuted on its owner, and it did not close",
        (branelink.O6_CAUSE_OF_DEATH_REFUTED, branelink.O6_CLOSED),
        (True, False))
    chk("O5 declines Flanagan-Wald and Sanders 5.1 on its owner",
        (throatmass.FLANAGAN_WALD_APPLIED, throatmass.SANDERS_51_APPLIED),
        (False, False))
    chk("O2's Sec. 7 is not transplanted to M < 0 on its owner",
        fewsterteo.SEC7_TRANSPLANTABLE_TO_NEGATIVE_M, False)
    chk("fluctuation.py's own flag that it moves no row is unmoved",
        fluctuation.LEDGER_ROW_MOVES, False)
    o2 = [r for r in OPEN_ROWS if r[0] == "O2"][0]
    # DOCKET 67 follow-ups: fewsterteo.PREFACTOR_212 is now the printed 1/pi;
    # the cell prints the owner's printed string, never a '%d' of the float
    # (which rendered 'exactly 0'), and the text-layer 1 is pi x 1/pi.
    chk("O2 prints fewsterteo's printed prefactor (1/pi), not 'exactly 0' or 1",
        (("Its prefactor is %s as printed" % fewsterteo.PREFACTOR_212_PRINTED)
         in o2[1],
         abs(fewsterteo.PREFACTOR_212 - 1.0 / math.pi) < 1e-15,
         abs(math.pi * fewsterteo.PREFACTOR_212
             - fewsterteo.PREFACTOR_212_TEXT_LAYER_READING) < 1e-15,
         "prefactor is exactly 0" in o2[1], "Its prefactor is exactly 1" in o2[1]),
        (True, True, True, False, False))
    chk("O2's answer now names D22's curved question (ruling C addendum)",
        ("D22's distribution question" in o2[2],
         "note [18]" in o2[2]), (True, True))

    print("\n4c. DOCKET 64: WHAT WAS WITHDRAWN OR CORRECTED IS NOT PRINTED")
    # Each needle is a wording a DOCKET 64 verifier or computation withdrew.
    # LEDGER.md must carry none of them; the superseded and withdrawn tables
    # hold only the board's OWN earlier wording, which contains none.
    needles64 = _withdrawn_needles_64()
    md = to_markdown()
    chk("no withdrawn DOCKET 64 wording appears in LEDGER.md",
        [n for n in needles64 if n.lower() in md.lower()], [])
    chk("  CONTROL: the search fires on a copy with one planted",
        [n for n in needles64
         if n.lower() in (md + needles64[2]).lower()], [needles64[2]])
    chk("  each withdrawal is kept on its owner, not deleted",
        (len(noise.WITHDRAWN) > 0, len(hpscentre.WITHDRAWN) > 0,
         len(linstab.WITHDRAWN) > 0,
         qeihps.VERDICT_THROAT_GEODESIC_WITHDRAWN.startswith("WITHDRAWN"),
         formation.D25_VERDICT_WITHDRAWN.startswith("WITHDRAWN")),
        (True, True, True, True, True))
    # No cell DOCKET 64 made long is cut in LEDGER.md: a cut drops the end of
    # a claim, which is where its qualification sits.
    cut = _truncated_cells()
    chk("no demand, open, superseded or pending cell is cut in LEDGER.md",
        cut, [])
    chk("  CONTROL: at the widths before DOCKET 64 it would have cut some",
        len(_truncated_cells(demand_claim=900, open_claim=1400,
                             open_answer=600, was=900, why=400)) > 0, True)

    print("\n4d. DOCKET 65: EVERY SEATED ROW IS massform.py's, ASKED")
    row = dict((r[0], r) for r in DEMAND + SUPPLY)
    opn = dict((r[0], r) for r in OPEN_ROWS)
    chk("D27-D29 are massform's rows exactly (claim, status, owner, movers)",
        [rid for rid in ("D27", "D28", "D29")
         if row[rid][1:] != tuple(massform.PROPOSED_ROWS[
             [p[0] for p in massform.PROPOSED_ROWS].index(rid)][2:])], [])
    chk("  each a THEOREM, owned by massform",
        [(row[r][2], row[r][3][0]) for r in ("D27", "D28", "D29")],
        [(THEOREM, "massform")] * 3)
    chk("S10's status IS massform.MECHANISM_VERDICT[0], REFUSED, asked of it",
        (row["S10"][2], massform.MECHANISM_VERDICT[0], row["S10"][3]),
        (REFUSED, REFUSED, ("massform", "MECHANISM_VERDICT")))
    chk("S11-S13 are OPEN, owned by the flags that say each route is PRICED",
        [(row[r][2], row[r][3], ask(row[r][3])) for r in ("S11", "S12", "S13")],
        [(OPEN, ("massform", a), True) for a in (
            "ANOMALY_ROUTE_PRICED", "PAIR_ROUTE_PRICED", "HELD_SEAT_ROUTE_PRICED")])
    chk("  each note carries massform's claim and its movers, uncut",
        [r for r in ("S10", "S11", "S12", "S13")
         if not (PROPOSED[r][2] in row[r][4] and PROPOSED[r][5] in row[r][4])], [])
    chk("  and their names are massform.SURVIVES's, asked, one route each",
        (all(row[r][1] in [n for n, _t in massform.SURVIVES]
             for r in ("S11", "S12", "S13")),
         len(set(row[r][1] for r in ("S11", "S12", "S13")))), (True, 3))
    # M-D65-2 (RULED_BY_M): 'Fold into S10 (Recommended)'.  The finite share
    # is an OPEN item inside S10's note, asked of massform, and no row.
    chk("the finite share (massform's S10 (open)) is in S10's note, text and "
        "movers asked, OPEN on its owner, and is no row (M-D65-2)",
        (PROPOSED["S10 (open)"][2] in row["S10"][4],
         PROPOSED["S10 (open)"][5] in row["S10"][4],
         "not a row (M-D65-2)" in row["S10"][4],
         massform.FINITE_HIGGS_SHARE_STATUS,
         [r[0] for r in OPEN_ROWS if r[0] == "O8" or "FINITE Higgs share" in r[1]],
         "S10 (open)" in [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS]),
        (True, True, True, OPEN, [], False))
    _keep = massform.FINITE_HIGGS_SHARE_STATUS
    massform.FINITE_HIGGS_SHARE_STATUS = "COMPUTED"
    try:
        _raised = False
        try:
            _s10_open_item()
        except ValueError:
            _raised = True
    finally:
        massform.FINITE_HIGGS_SHARE_STATUS = _keep
    chk("  CONTROL: a finite share no longer OPEN on its owner is not carried as "
        "an OPEN item (it raises)", _raised, True)
    chk("S5 stays OPEN and its note carries DOCKET 65's append, asked",
        (row["S5"][2], _s5_docket65_append() in row["S5"][4],
         massform.RECONSTRUCTION_SURVIVES), (OPEN, True, True))
    chk("S5 no longer claims to be the only priced row (S11-S13 are priced)",
        ("THE ONLY ROW ON THIS LEDGER WITH A PRICE" in row["S5"][4],
         "S11-S13" in row["S5"][4]), (False, True))
    chk("massform asks D23 of this board, and gets this board's row",
        massform.d23_row()[:4] == [r for r in DEMAND if r[0] == "D23"][0][:4],
        True)
    chk("  and its held-seat route needs that prior arrival",
        massform.preparation_needs_prior_arrival(), True)
    _qet = [r for r in RULED_BY_M if r[0] == "M-D65-1"]
    chk("M-D65-1: QET folded into DOCKET 66, M quoted, literature CITED not READ",
        (len(_qet), _qet[0][3].startswith("RULED BY M: FOLD INTO DOCKET 66"),
         "'%s'" % M_D65_1_ANSWER in _qet[0][3],
         M_D65_1_WORDS in _qet[0][2],
         "CITED, not READ" in _qet[0][2],
         all(a in _qet[0][2] for a in ("Hotta 2008", "1701.03805",
                                       "2301.02666", "2505.04689", "2506.19878"))),
        (1, True, True, True, True, True))
    _raw = to_markdown()
    _md = " ".join(_raw.split())
    chk("M's words in M-D65-1 are ONE sentence wherever printed: `why`, the "
        "ruling cell and LEDGER.md each quote exactly M_D65_1_WORDS",
        verbatim_faults(_qet[0], _raw), [])
    for _where, _mut in ((3, "ruling cell"), (2, "why"), (None, "LEDGER.md line")):
        _q = list(_qet[0])
        _m = _raw
        _bad = "consider that the introduction"
        if _where is None:
            _m = _raw.replace("consider the idea that the introduction", _bad)
        else:
            _q[_where] = _q[_where].replace("consider the idea that the introduction",
                                            _bad, 1)
        chk("  CONTROL: 'consider the idea that the' shortened in the %s only is "
            "caught" % _mut, len(verbatim_faults(tuple(_q), _m)) > 0, True)
    chk("  CONTROL: a copy of M's words dropped from the ruling cell is caught",
        len(verbatim_faults((_qet[0][0], _qet[0][1], _qet[0][2],
                             _qet[0][3].replace("verbatim: '", "roughly: '"),
                             _qet[0][4]), _raw)) > 0, True)
    _ms2 = [r for r in RULED_BY_M if r[0] == "M-D65-2"]
    chk("M-D65-2 is RULED: the question exactly as put to M, M's answer "
        "verbatim, the fold APPLIED, and nothing pending",
        (len(_ms2), _ms2[0][1] == M_D65_2_QUESTION,
         _ms2[0][3].startswith("RULED BY M: FOLD INTO S10's NOTE"),
         "M's answer: '%s'" % M_D65_2_ANSWER in _ms2[0][3],
         all("'%s'" % f in _ms2[0][2] for f in M_D65_2_OPTION),
         M_D65_2_QUESTION in _md, "'%s'" % M_D65_2_ANSWER in _md,
         # DOCKET 68 added a pending question of its own (M-D68-P1, since
         # converted to the ruling M-D68-C12); none is DOCKET 65's.
         [p[0] for p in PENDING_RULINGS if not p[0].startswith("M-D68-")],
         "O8" not in [r[0] for r in OPEN_ROWS]),
        (1, True, True, True, True, True, True, [], True))
    # DOCKET 66's seating carries QET in O9's DOCKET 66 part and S5's note, a
    # note and no row: the part is taken out of O9's claim before the ask.
    chk("  and M-D65-1 opens no row (QET is DOCKET 66's, not the board's; DOCKET "
        "66's seating carries it in O9's DOCKET 66 part and S5's note, no row)",
        [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS
         if "QET" in r[1].replace(D66_O9_PART, "")
         or "Teleportation" in r[1].replace(D66_O9_PART, "")], [])
    chk("D27-D29's owners still SAY what the THEOREM rows say (values, asked)",
        theorem_owner_disagreements(), [])
    for _attr, _flip, _rid in (("CONSIDERATION_HOLDS", False, "D27"),
                               ("HIGGS_FIELD_SUPPLIES_THE_MASS_ENERGY", True, "D29")):
        _keep = getattr(massform, _attr)
        setattr(massform, _attr, _flip)
        try:
            _got = theorem_owner_disagreements()
        finally:
            setattr(massform, _attr, _keep)
        chk("  CONTROL: massform.%s -> %s is caught on %s" % (_attr, _flip, _rid),
            _got, [_rid])
    _keep = massform.pair_floor_j
    massform.pair_floor_j = lambda c=None: _keep(c) / 2.0
    try:
        _got = theorem_owner_disagreements()
    finally:
        massform.pair_floor_j = _keep
    chk("  CONTROL: massform.pair_floor_j halved is caught on D28", _got, ["D28"])
    chk("every DOCKET 65 qualifier is on its seated row, as often as pinned",
        missing_qualifiers(), [])
    _rows = dict((r[0], r) for r in DEMAND + SUPPLY + OPEN_ROWS)
    _ctl = [(rid, phrase) for rid, need in SEATED_QUALIFIERS.items()
            for phrase, _n in need
            if not any(q[:2] == (rid, phrase) for q in missing_qualifiers(
                dict(_rows, **{rid: tuple(x.replace(phrase, "", 1)
                                          if isinstance(x, str) and phrase in x
                                          else x for x in _rows[rid])})))]
    chk("  CONTROL: deleting any one qualifier from its row is caught (each)",
        _ctl, [])
    # DOCKET 67 (2309.10848-eft-breakdown, M's ruling 2026-10-02): S4 stays ONE
    # REFUSED row; its OPEN xi < 0 window is recorded in its text, with the
    # owner's figures, and is never counted as an open row.
    _s4 = [r for r in SUPPLY if r[0] == "S4"][0]
    _win = candidates.xi_negative_window()
    _s4_window = lambda t: all(x in t for x in (
        "%.6f" % _win[1], "%.6f l_P" % _win[2], "xi < 0 sub-class",
        "FFKP eq. (109)", "xi_tree > 0", "not counted as an open row"))
    chk("S4 is one REFUSED row; its xi < 0 window (DOCKET 67) is in its text with "
        "candidates' figures, OPEN, and in no open count",
        (_s4[2], sum(1 for r in SUPPLY if r[0] == "S4"), _s4_window(_s4[4]),
         candidates.XI_NEGATIVE_WINDOW_STATUS,
         "S4" in ([r[0] for r in DEMAND + SUPPLY if r[2] == OPEN]
                  + [r[0] for r in OPEN_ROWS])),
        (REFUSED, 1, True, "OPEN", False))
    chk("  CONTROL: S4's text with the window's top edge drifted is caught",
        _s4_window(_s4[4].replace("%.6f" % _win[1], "1.300000")), False)
    # DOCKET 67 (ford-roman-qi-and-fewster-casimir-fraction, M's ruling
    # 2026-10-02): W2 stays WITHDRAWN; one reading of its premise is OPEN, with
    # bounds' figures, and nothing anti-warp is reinstated.
    _w2 = [r for r in WITHDRAWN_ROWS if r[0] == "W2"][0]
    _sbr = bounds.sharp_bound_reading()
    _w2_reading = lambda t: all(x in t for x in (
        "W2 stays WITHDRAWN on four carried counts",
        "ONE READING OF THE PREMISE IS OPEN, NOT REFUTED",
        "C_s = %.6f" % _sbr["C_s"], "C/%.3f" % _sbr["C_over_C_s"],
        "NAMED-NOT-READ", "is NOT reinstated"))
    chk("W2 stays WITHDRAWN; its sharp-bound midplane reading is OPEN in its text "
        "with bounds' figures; nothing reinstated",
        (sum(1 for r in WITHDRAWN_ROWS if r[0] == "W2"),
         "W2" in [r[0] for r in DEMAND + SUPPLY + OPEN_ROWS],
         _w2_reading(_w2[2]), bounds.SHARP_BOUND_MIDPLANE_SATURATION,
         bounds.NO_MATERIAL_CHOICE_CROSSES_IT_REINSTATED,
         ask(("bounds", "FORD_ROMAN_K_IS_WRONG"))),
        (1, False, True, "OPEN", False, True))
    chk("  CONTROL: W2's text with C_s drifted is caught",
        _w2_reading(_w2[2].replace("%.6f" % _sbr["C_s"], "0.212000")), False)
    _d28 = dict(_rows, D28=tuple(x.replace("costs at least ", "costs ", 1)
                                 if isinstance(x, str) else x for x in _rows["D28"]))
    chk("  CONTROL: D28 with 'at least' deleted (a floor read as an exact cost) "
        "is caught", [q[:2] for q in missing_qualifiers(_d28) if q[0] == "D28"],
        [("D28", "costs at least")])
    chk("M-D65-1 as LEDGER.md PRINTS it: M's whole sentence, CITED not READ, "
        "the anchors; no ruling's question, ruling or unblocks cell is cut",
        (M_D65_1_WORDS in _md,
         "consider the idea that the introduction of information" in _md,
         "CITED, not READ" in _md,
         all(a in _md for a in ("Hotta 2008", "arXiv:1701.03805",
                                "arXiv:2301.02666", "arXiv:2505.04689",
                                "arXiv:2506.19878")),
         [c for c in _truncated_cells() if c[0] == "ruled"]),
        (True, True, True, True, []))
    chk("the finite share is NOT a row, on M's ruling, stated in the docstring "
        "(sections 4 and 6) and in the census comment's re-pin",
        ("NOT A ROW, ON M's\n       RULING M-D65-2" in __doc__,
         "S10 (open)     NOT A ROW" in __doc__,
         "Nothing from\nDOCKET 65 is pending M" in __doc__,
         "O8   the FINITE Higgs share" in __doc__), (True, True, True, False))
    _buf = io.StringIO()
    with contextlib.redirect_stdout(_buf):
        report()
    _rep = " ".join(_buf.getvalue().split())
    chk("the plain report prints S10's name whole and massform.mechanism_label() "
        "whole beside it (a cut there read as a bare refusal)",
        (S10_NAME in _rep, " ".join(massform.mechanism_label().split()) in _rep),
        (True, True))
    chk("nothing DOCKET 65 seated carries the status word DECLARED",
        [r[0] for r in massform.PROPOSED_ROWS if "DECLARED" in r[3]], [])
    # DOCKET 65's closing round.
    _seated65 = {"D27", "D28", "D29", "S10", "S11", "S12", "S13", "S10 (open)",
                 "S5 (note)"}
    chk("massform.PROPOSED_ROWS' ids are exactly what this board seats from "
        "DOCKET 65 (the rows, the S10 (open) item and the S5 append)",
        set(r[0] for r in massform.PROPOSED_ROWS), _seated65)
    chk("  CONTROL: a proposed row this board does not seat (D30) is caught here",
        set(r[0] for r in massform.PROPOSED_ROWS + (("D30",),)) == _seated65, False)
    chk("every seated row's text DIRECTION agrees with the owner value it states "
        "(POLARITY: phrase on the row, owner asked)", polarity_faults(), [])
    _inv = {"arrival switches nothing on": "arrival switches the field on",
            "costs at least": "costs",
            "leaves B units of antibaryon number": "leaves nothing",
            "has no energy to give about v": "has energy to give about v",
            "REFUSED, gap None": "PRICED, gap None",
            "exp(-4 pi/alpha_W) per transition": "no price per transition",
            "extra leptons (D28)": "no extra leptons",
            "Two-particle collisions: CONTESTED": "Two-particle collisions: SETTLED",
            "Priced, not refused": "Refused, not priced",
            "PRICED at eps": "REFUSED at eps",
            "survives M's mechanism: no mass forms at the seat":
                "is refused with M's mechanism: mass forms at the seat"}
    _ctl = []
    for _rid, _phrase, _p in POLARITY:
        _r2 = dict(_rows, **{_rid: tuple(x.replace(_phrase, _inv[_phrase], 1)
                                          if isinstance(x, str) else x
                                          for x in _rows[_rid])})
        if (_rid, _phrase, "phrase missing") not in polarity_faults(_r2):
            _ctl.append((_rid, _phrase))
    chk("  CONTROL: each phrase inverted on a private copy of its row is caught",
        _ctl, [])
    for _attr, _flip, _rid, _phrase in (
            ("FIELD_SWITCHED_ON_BY_ARRIVAL", True, "D27", "arrival switches nothing on"),
            ("PAIR_ROUTE_PRICED", False, "S12", "Priced, not refused"),
            ("RECONSTRUCTION_SURVIVES", False, "S5",
             "survives M's mechanism: no mass forms at the seat")):
        _keep = getattr(massform, _attr)
        setattr(massform, _attr, _flip)
        try:
            _got = polarity_faults()
        finally:
            setattr(massform, _attr, _keep)
        chk("  CONTROL: massform.%s -> %s is caught on %s (owner disagrees)"
            % (_attr, _flip, _rid), _got, [(_rid, _phrase, "owner disagrees")])
    chk("S10's label is a label for M's mechanism, not a refusal of what S12 "
        "and S13 price", s10_name_faults(), [])
    chk("  CONTROL: 'atomic mass formed at the seat' as the label is caught",
        len(s10_name_faults("atomic mass formed at the seat")), 2)
    # CORRECTED (DOCKET 66's seating): this check first required QET TO BE
    # tested in DOCKET 66 (NOT YET RUN); DOCKET 66 has run, so the cell must now
    # EQUAL its template filled with what ran (asked of qet.py) and keep the
    # first wording as history -- the old cell is a control below.
    chk("M-D65-1 names the literature as it was named to M (arXiv:2506.19878 "
        "included), says QET IS TESTED in DOCKET 66 -- the cell EQUAL to its "
        "template filled from what DOCKET 66 ran, asked of qet.py -- keeps "
        "'(NOT YET RUN)' only as its first wording, prints as READ only what "
        "qet.py's sources READ, and keeps the question's parenthetical as the "
        "question's description, not READ",
        m_d65_1_faults(), [])
    _q1 = list(_qet[0])
    _q1[3] = M_D65_1_RULING_AS_FIRST_WRITTEN_T % (M_D65_1_ANSWER, M_D65_1_WORDS,
                                                  M_D65_1_LITERATURE)
    _q2 = list(_qet[0])
    _q2[2] = _q2[2].replace("; arXiv:2506.19878", "")
    _q3 = list(_qet[0])
    _q3[3] = _q3[3].replace("; the question's parenthetical is the question's "
                            "description as put to M, not READ", "")
    _q4 = list(_qet[0])
    _q4[3] = _q4[3].split("  FIRST APPLIED (kept)")[0]
    _q5 = list(_qet[0])
    _q5[3] = _q5[3].replace("arXiv:2506.19878: READ",
                            "arXiv:2506.19878: READ; spin-chain arXiv:0803.0348: READ")
    _q6 = list(_qet[0])
    _q6[4] = M_D65_1_UNBLOCKS_AS_FIRST_WRITTEN
    _q7 = list(_qet[0])
    _q7[3] = _q7[3].replace("QET IS TESTED inside DOCKET 66: ",
                            "QET IS TESTED inside DOCKET 66: QET is exotic matter; ")
    chk("  CONTROL: the cell as DOCKET 65's seating wrote it (NOT YET RUN), the "
        "literature without 2506.19878, the parenthetical unattributed, the history "
        "dropped, a source qet.py does not READ (its spin-chain 0803.0348) printed "
        "as READ, the unblocks cell as it stood, and a typed verdict planted beside "
        "what ran are each caught",
        [len(m_d65_1_faults(tuple(q))) > 0 for q in (_q1, _q2, _q3, _q4, _q5, _q6, _q7)],
        [True] * 7)
    chk("M-S1A-P3's unblocks cell says DOCKET 66 has run, built from the docket66 "
        "owners, after its first wording ('DOCKET 66 opens', kept), and keeps 'the "
        "throat-creation classes stay OPEN' (which defects.py and combine66.py read)",
        p3_unblocks_faults(), [])
    chk("  CONTROL: the cell as it stood ('...; DOCKET 66 opens' alone), a typed "
        "verdict in place of what ran, and the throat-creation clause dropped are "
        "each caught",
        [len(p3_unblocks_faults(t_)) > 0 for t_ in (
            "the seat of every object must be free of a closed causal curve and a "
            "pathology; the throat-creation classes stay OPEN; DOCKET 66 opens",
            "the seat of every object must be free of a closed causal curve and a "
            "pathology; the throat-creation classes stay OPEN; DOCKET 66 opens.  DOCKET "
            "66 has run: a defect seat supplies the payload's matter",
            [r for r in RULED_BY_M if r[0] == "M-S1A-P3"][0][4].replace(
                "the throat-creation classes stay OPEN; ", ""))], [True] * 3)
    chk("M-S1A-P1's unblocks cell says DOCKET 65 has run and names its rows, "
        "built from massform's ids", p1_unblocks_faults(), [])
    chk("  CONTROL: the cell as it stood ('DOCKET 65 opens' alone) is caught",
        len(p1_unblocks_faults("S-1 stands NONEMPTY with no contraction "
                               "requirement; DOCKET 65 opens")), 1)
    _d67 = [r for r in RULED_BY_M if r[0] == "M-D65-3"]
    chk("M-D65-3: DOCKET 67 OPENED by M -- the question exactly as put to M, "
        "M's answer verbatim, M's words verbatim in `why`, the ruling cell and "
        "LEDGER.md, NOT YET RUN and its order in what it unblocks",
        (len(_d67), _d67[0][1] == M_D65_3_QUESTION,
         _d67[0][3].startswith("RULED BY M: OPEN IT -- M's answer: '%s'"
                               % M_D65_3_ANSWER),
         verbatim_faults(_d67[0], _raw, rid="M-D65-3"),
         "NOT YET RUN" in _d67[0][4],
         "after DOCKET 65 is seated and before DOCKET 66" in _d67[0][4],
         M_D65_3_QUESTION in _md, "'%s'" % M_D65_3_ANSWER in _md),
        (1, True, True, [], True, True, True, True))
    chk("  M-D65-3's unblocks cell EQUALS its first wording (NOT YET RUN, kept) "
        "followed by what ran, READ from docket67-raw/CLOSE.md (d67_ran); "
        "CONTROLS: the first wording alone, and 'every audited result STANDS' "
        "appended, are each caught",
        (m_d65_3_unblocks_faults(), len(d67_close_sections()) >= 5,
         "M's closing rulings" in d67_ran(),
         len(m_d65_3_unblocks_faults(M_D65_3_UNBLOCKS_AS_FIRST_WRITTEN)) > 0,
         len(m_d65_3_unblocks_faults(_d67[0][4] + "  Every audited result STANDS.")) > 0),
        ([], True, True, True, True))
    # EQUALITY, not substring presence: the seated cells must EQUAL their
    # templates filled from the asked constants, so no verdict on a docket
    # that has not run can be typed beside the required phrases (a planted
    # 'DOCKET 67 has run: every audited result STANDS' passed substring
    # guards green).
    chk("  M-D65-3's ruling cell EQUALS M_D65_3_RULING_T filled from M's answer "
        "and M's words, and `why` EQUALS the owners' record (m_d65_3_why())",
        (_d67[0][3] == M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS),
         _d67[0][2] == m_d65_3_why()), (True, True))
    chk("  CONTROL: 'DOCKET 67 has run: every audited result STANDS' planted in "
        "the ruling cell is caught",
        _d67[0][3] + "  DOCKET 67 has run: every audited result STANDS"
        == M_D65_3_RULING_T % (M_D65_3_ANSWER, M_D65_3_WORDS), False)
    _verdict = re.compile(r"\b(has run|HAS RUN|STANDS|WRONG|NARROWED|cannot|"
                          r"fails|expected to|is not exotic|no negative)\b")
    chk("  no template carries a verdict word in the board's own words "
        "(either direction) -- STANDS / NARROWED / WRONG enter only inside M's "
        "asked question; M-D65-4's ruling and `why` templates and M-D65-5's "
        "ruling template are scanned too",
        (_verdict.findall(M_D65_3_RULING_T), _verdict.findall(M_D65_3_WHY_T),
         _verdict.findall(M_D65_4_RULING_T), _verdict.findall(M_D65_4_WHY_T),
         _verdict.findall(M_D65_4_UNBLOCKS_T), _verdict.findall(M_D65_5_RULING_T)),
        ([], [], [], [], [], []))
    _nf, _nne = fluctuation_discrepancies()
    _nm = len(massform_divergences())
    # The 'second regex' in the COUNTS check below (a full stop followed by
    # whitespace, over the same paragraph) is the SAME splitting rule as
    # massform_divergences(): an arithmetic check of the split, not an
    # independent count of the owner's sentences.
    chk("  the characterisation in `why` is the owners': fluctuation's preprint "
        "version and its journal clause, massform's own heading, the p.7 "
        "pairing beside the p.2 one -- and 'published errors' is nowhere",
        ("against arXiv gr-qc/9304008 v1" in _d67[0][2],
         "is COMPARED-BY-M (fluctuation.JOURNAL_VERSION_READ = False), and its own "
         "clause holds: 'they carry to the journal version on M's "
         "comparison, not on this file's reading'" in _d67[0][2],
         "'DIVERGENCES FROM THE SOURCES, RECORDED AND NOT REPAIRED'" in _d67[0][2],
         "their p.7 pairing, 1/%g, gives 10^%.2f" % (
             massform.TW_ALPHA_INV[0],
             massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[0])) in _d67[0][2],
         "published errors" in _d67[0][2], "published errors" in M_D65_3_WHY_T),
        (True, True, True, True, False, False))
    chk("  the lead-in's COUNTS are the owners': the printed '%d of the %d "
        "discrepancies' equals the count of fluctuation's KF flags recomputed "
        "here (KF_*_IS_EXACT False + the claim flag False + the typographical "
        "flag True + the conclusion flag False), the printed '%d of the %d divergences' equals the sentences "
        "under massform's heading, the nouns are the owners' ('discrepancies', "
        "'refuted', 'typographical', 'divergences'), the framing is scoped to "
        "the cited items, and 'refutation' is nowhere"
        % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf, len(M_D65_3_WHY_ITEMS_MASS), _nm),
        ("%d of the %d discrepancies fluctuation.py records against a preprint "
         "version" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf) in _d67[0][2],
         _nf == sum(1 for k in ("KF_216_FINAL_IS_EXACT", "KF_37_IS_EXACT",
                                "KF_38_IS_EXACT", "KF_319_IS_EXACT", "KF_323_IS_EXACT")
                    if getattr(fluctuation, k) is False)
         + (not fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1)
         + fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL
         + (not fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES),
         "the rest, %d KF_*_IS_EXACT flags False" % _nne in _d67[0][2],
         "%d of the %d divergences massform.py records under its own heading"
         % (len(M_D65_3_WHY_ITEMS_MASS), _nm) in _d67[0][2],
         _nm == len(re.findall(r"\.(?:\s|$)", " ".join(re.search(
             r"RECORDED AND NOT REPAIRED\.(.*?)\n\n", massform.__doc__, re.S)
             .group(1).split()) + " ")),
         'FALSE by z3 -- "refuted" -- and (3.41)\'s 1/2 "typographical"' in _d67[0][2],
         "Of what this project has recorded against outside results, the items "
         "whose owners expose flags asked here" in _d67[0][2],
         "refutation" in _d67[0][2], "refutation" in M_D65_3_WHY_T,
         "What this project has already RECORDED" in _d67[0][2]),
        (True, True, True, True, True, True, True, False, False, False))
    # The tuples naming what the cell details are TIED to the cell: every
    # fluct member is printed as 'fluctuation.<flag> = ' and no other KF_ flag
    # is printed (LEDGER_ROW_MOVES is not a KF_ name), and every mass label is a
    # substring of the cell that is the subject of exactly one sentence of
    # massform_divergences() (its surnames open the sentence; a 'p.N' in the
    # label is in it).  The '%d of' numerators are these guarded len()s.
    def _why_items(why, fl, ms):
        kf_in_cell = {k for k in vars(fluctuation)
                      if k.startswith("KF_") and "fluctuation.%s" % k in why}
        return (all("fluctuation.%s = " % k in why for k in fl),
                kf_in_cell == set(fl),
                all(m in why for m in ms),
                [sum(1 for s in massform_divergences()
                     if all(n in s[:40]
                            for n in re.findall(r"[A-Z][a-z]+", m.split("'s")[0]))
                     and all(p in s for p in re.findall(r"p\.\d+", m)))
                 for m in ms])
    chk("  the tuples naming what `why` details are tied to the cell: each fluct "
        "member printed as 'fluctuation.<flag> = ' and no other KF_ flag printed "
        "; each mass label in the cell and "
        "the subject of exactly one sentence under massform's heading -- the "
        "'%d of' numerators are these len()s" % len(M_D65_3_WHY_ITEMS_FLUCT),
        _why_items(_d67[0][2], M_D65_3_WHY_ITEMS_FLUCT, M_D65_3_WHY_ITEMS_MASS),
        (True, True, True, [1] * len(M_D65_3_WHY_ITEMS_MASS)))
    with _scratch("M_D65_3_WHY_ITEMS_FLUCT", M_D65_3_WHY_ITEMS_FLUCT + ("KF_37_IS_EXACT",)):
        _why3 = m_d65_3_why()
        _tied3 = _why_items(_why3, M_D65_3_WHY_ITEMS_FLUCT, M_D65_3_WHY_ITEMS_MASS)
    chk("  CONTROL: another KF name appended to M_D65_3_WHY_ITEMS_FLUCT prints "
        "'%d of the %d' and is caught by the tie (not printed as "
        "'fluctuation.<flag> = ')" % (len(M_D65_3_WHY_ITEMS_FLUCT) + 1, _nf),
        ("%d of the %d discrepancies" % (len(M_D65_3_WHY_ITEMS_FLUCT) + 1, _nf) in _why3,
         _tied3[0], _tied3[1]), (True, False, False))
    chk("  CONTROL: a mass label the cell does not carry ('RS96 eq. (2.8)', the "
        "label as it stood) is caught",
        _why_items(_d67[0][2], M_D65_3_WHY_ITEMS_FLUCT,
                   ("RS96 eq. (2.8)",) + M_D65_3_WHY_ITEMS_MASS[1:])[2], False)
    chk("  fluctuation's verdict is in `why`, asked of its flags: Kuo & Ford's "
        "qualitative conclusion does NOT survive, with the owner's own reason, "
        "and no ledger row moves",
        ("Kuo & Ford's qualitative conclusion does NOT survive -- fluctuation.py: "
         "\"a displaced squeezed state carries negative energy with Delta = 0 "
         "(section 2)\" (fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = False) and "
         "no ledger row moves (fluctuation.LEDGER_ROW_MOVES = False)" in _d67[0][2],
         fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES, fluctuation.LEDGER_ROW_MOVES),
        (True, False, False))
    chk("  CONTROL: the verdict as it stood ('conclusion SURVIVES') planted in "
        "`why` is caught",
        _d67[0][2].replace("conclusion does NOT survive -- ", "conclusion SURVIVES -- ")
        == m_d65_3_why(), False)
    chk("  CONTROL: the lead-in as it stood ('Three published errors this project "
        "has already caught') planted in `why` is caught",
        _d67[0][2].replace("Of what this project has recorded against outside "
                           "results", "Three published errors this project "
                           "has already caught") == m_d65_3_why(), False)
    chk("  CONTROL: the typed count as it stood ('two refutations of a preprint "
        "version and two divergences') planted in `why` is caught, and would "
        "carry 'refutation'",
        (_d67[0][2].replace(
            "%d of the %d discrepancies fluctuation.py records against a preprint "
            "version" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf),
            "two refutations of a preprint version and two divergences")
         == m_d65_3_why(),
         "refutation" in "two refutations of a preprint version and two divergences"),
        (False, True))
    # The template follows the owner: a KF flag flipped (here, in-process and
    # restored) moves the printed count, and the conclusion clause moves with
    # its flag (and leaves the count).
    _kf, _sv = fluctuation.KF_319_IS_EXACT, fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES
    try:
        fluctuation.KF_319_IS_EXACT = True
        fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = True
        _moved = m_d65_3_why()
    finally:
        fluctuation.KF_319_IS_EXACT, fluctuation.KF_QUALITATIVE_CONCLUSION_SURVIVES = _kf, _sv
    chk("  CONTROL: fluctuation.KF_319_IS_EXACT and KF_QUALITATIVE_CONCLUSION_"
        "SURVIVES flipped True move the printed count to %d and the verdict "
        "clause to SURVIVES (the template follows the owner)" % (_nf - 2),
        ("%d of the %d discrepancies" % (len(M_D65_3_WHY_ITEMS_FLUCT), _nf - 2) in _moved,
         "the rest, %d KF_*_IS_EXACT flags False" % (_nne - 1) in _moved,
         "qualitative conclusion SURVIVES (fluctuation.KF_QUALITATIVE_CONCLUSION_"
         "SURVIVES = True)" in _moved,
         _moved == m_d65_3_why()), (True, True, True, False))
    chk("  the figures in `why` are the owners' (regenerated now: KF flags, TW "
        "p.2 and p.7, RS96)",
        ("KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1 = %s" % fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1
         in _d67[0][2],
         fluctuation.KF_CLAIM_NEGATIVE_MEANS_DELTA_GT_1, fluctuation.JOURNAL_VERSION_READ,
         "KF_341_HALF_IS_TYPOGRAPHICAL = %s" % fluctuation.KF_341_HALF_IS_TYPOGRAPHICAL
         in _d67[0][2],
         "prints 10^%.0f at alpha_W ~ 1/%g where the arithmetic gives 10^%.2f, %.2f "
         "decades off" % (massform.TW_PRINTED_LOG10, massform.TW_ALPHA_INV[1],
                          massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1]),
                          abs(massform.log10_suppression(1.0 / massform.TW_ALPHA_INV[1])
                              - massform.TW_PRINTED_LOG10)) in _d67[0][2],
         "prints 10^%.0f at alpha_W = 1/%g where the arithmetic gives 10^%.2f"
         % (massform.RS96_PRINTED_LOG10, massform.RS96_ALPHA_INV,
            massform.log10_suppression(1.0 / massform.RS96_ALPHA_INV)) in _d67[0][2]),
        (True, False, False, True, True, True))
    _d4 = [r for r in RULED_BY_M if r[0] == "M-D65-4"]
    _d63faults = paper_d63_faults()
    _d63span, _d63text = (paper_d63_marker() if not _d63faults
                          else ("%d" % PAPER_D63_MARKER_LINE, "MARKER NOT FOUND"))
    # A count of the paper's edits or markers in the board's own words, in
    # any of the file's vocabularies ('paper edits', 'marked edits',
    # 'markers'); 'both' counts too.
    _cnt = COUNT_RE
    chk("M-D65-4: the paper's caveat (b) QUALIFIED on M's ruling -- the question "
        "as put to M, M's answer verbatim, the ruling cell EQUAL to its template "
        "filled from the asked pieces (M's rule for the paper, the DOCKET 63 "
        "marker READ back), `why` EQUAL to its template, unblocks EQUAL to its "
        "template (M's rule for the paper stands), printed in LEDGER.md",
        (len(_d4), _d4[0][1] == M_D65_4_QUESTION,
         _d4[0][3] == m_d65_4_ruling(),
         _d4[0][3] == M_D65_4_RULING_T % (M_D65_4_ANSWER, PAPER_CAVEAT_B_LINE,
                                          PAPER_CAVEAT_B_CLAUSE, M_PAPER_RULE_WORDS,
                                          _d63span, _d63text, paper_d67_words_clause()),
         _d4[0][2] == m_d65_4_why(),
         "'%s'" % M_D65_4_ANSWER in _d4[0][3],
         _d4[0][4] == M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS,
         M_D65_4_QUESTION in _md, "'%s'" % M_D65_4_ANSWER in _md,
         "M's ruling on\nthe paper's caveat (b) is M-D65-4" in __doc__),
        (1, True, True, True, True, True, True, True, True, True))
    chk("  M's rule for the paper (M_PAPER_RULE_WORDS) is printed wherever it is "
        "invoked -- the ruling cell, the unblocks cell, LEDGER.md -- with its "
        "provenance ('verbatim from the session, witnessed by the lead'), and "
        "the docstring names it",
        (M_PAPER_RULE_WORDS in _d4[0][3], M_PAPER_RULE_WORDS in _d4[0][4],
         _md.count(M_PAPER_RULE_WORDS),
         _d4[0][3].count("verbatim from the session, witnessed by the lead"),
         "M_PAPER_RULE_WORDS" in __doc__),
        # LEDGER.md prints it as often as the board's cells carry it (M-D65-4's
        # ruling and unblocks, M-D65-5's unblocks) -- asked of RULED_BY_M.
        (True, True, sum(" ".join(str(c).split()).count(M_PAPER_RULE_WORDS)
                         for r in RULED_BY_M for c in r), 1, True))
    chk("  paper/CLAIMS.md:%s, READ now, carries DOCKET 63's marker with both "
        "fragments ('(Corrected on M's ruling:', 'DOCKET 63'), and the ruling "
        "cell names it by its READ lines and text -- the paper's edits on M's "
        "ruling are named, not counted ('the one', 'the second', 'two', 'both' "
        "absent before 'edit(s)' / 'marker(s)')"
        % _d63span,
        (_d63faults, _d63span.startswith("%d" % PAPER_D63_MARKER_LINE),
         "(Corrected on M's ruling:" in _d63text, "DOCKET 63" in _d63text,
         "(paper/CLAIMS.md:%s: \"%s\")" % (_d63span, _d63text) in _d4[0][3],
         bool(_cnt.search(_d4[0][3] + " " + _d4[0][4] + " " + __doc__))),
        ([], True, True, True, True, False))
    # The same count regex over this file's SOURCE from the M-D65-4 constants
    # through RULED_BY_M, comments included: a comment that counted ('the
    # paper carries two marked edits on M's ruling') beside 'counts neither'
    # stood there once, unseen by a regex whose vocabulary was 'paper edits'.
    _srcfull = open(__file__, encoding="utf-8").read()
    _i0 = _srcfull.index("#: M-D65-4: the paper's caveat (b).")
    _i1 = _srcfull.index("\n]\n", _srcfull.index("\nRULED_BY_M = [", _i0))
    _region = _srcfull[_i0:_i1]
    chk("  no count of the paper's edits stands in ledger.py's source from the "
        "M-D65-4 constants through RULED_BY_M, comments included ('the one', "
        "'the second', 'two', 'both' before 'paper edit(s)' / 'marked edit(s)' / "
        "'marker(s)'); the region holds the constants and the M-D65-4 and "
        "M-D65-5 rows",
        (_cnt.findall(_region), "M_PAPER_RULE_WORDS = (" in _region,
         '("M-D65-4",' in _region, '("M-D65-5",' in _region),
        ([], True, True, True))
    chk("  CONTROL: the comment as it stood ('the paper carries two marked edits "
        "on M's ruling, and this file names both and counts neither') planted "
        "in that region is found",
        _cnt.findall(_region + "\n#: the paper carries two marked edits on M's "
                     "ruling, and this file names both and counts neither."),
        [("two", "marked ", "edits")])
    chk("  CONTROL: a count APPENDED to the seated M-D65-5 cell, in each of the "
        "vocabularies round 8's lenses planted ('all three markers ...', 'the "
        "three markers ...', 'five markers ...', 'every marker ...', 'the only "
        "markers ...'), is found by COUNT_RE",
        [bool(COUNT_RE.search([r for r in RULED_BY_M if r[0] == "M-D65-5"][0][3]
                              + " -- " + t)) for t in (
            "all three markers the paper carries from this board name a ruling",
            "the three markers name a ruling", "five markers the paper carries",
            "the paper's five DOCKET markers", "every marker names a ruling",
            "the only markers the paper carries")],
        [True] * 6)
    chk("  CONTROL: the marker altered in a private copy of the paper's lines "
        "(the fragment '(Corrected on M's ruling:' dropped; 'DOCKET 63' dropped; "
        "the marker moved off line %d) is caught each way" % PAPER_D63_MARKER_LINE,
        (paper_d63_faults([l.replace("(Corrected on M's ruling:", "(Corrected:")
                           for l in _paper_lines()]) != [],
         paper_d63_faults([l.replace("DOCKET 63", "DOCKET 6") for l in _paper_lines()]) != [],
         paper_d63_faults([""] + _paper_lines()) != []),
        (True, True, True))
    _srcs = {"ledger.py": open(__file__, encoding="utf-8").read(),
             "specthm.py": open(HERE + "/specthm.py", encoding="utf-8").read(),
             "LEDGER.md": _raw}
    # The withdrawn phrases are assembled from pieces here, so the source
    # scan finds them nowhere but where a planted copy would put them; the
    # scan is by the WORD ('finalis..ed', 'finalis..ation'), since a planted
    # phrase split across two string literals would hide from a phrase scan.
    # M's own 'finalized' (M_PAPER_RULE_WORDS, M's spelling) is not the word.
    _old_edit = "the one paper edit since M " + "finalis" + "ed it, on M's ruling"
    _old_rule = "M's " + "finalis" + "ation rule"
    _old_words = ("finalis" + "ed", "finalis" + "ation")
    chk("  the withdrawn phrases ('since M finalis.. it', 'finalis..ation rule') "
        "stand nowhere in ledger.py, specthm.py or LEDGER.md (source-read, by "
        "the word)",
        sorted(n for n, t in _srcs.items() if any(w in t for w in _old_words)), [])
    chk("  CONTROL: the phrase as it stood ('the one paper edit since M finalis.. "
        "it, on M's ruling') planted in the ruling cell fails the equality, and "
        "planted in the template would be found by the source scan",
        (_d4[0][3].replace("a paper edit on M's ruling under M's rule for the paper",
                           _old_edit) == m_d65_4_ruling(),
         _old_edit[22:36] in M_D65_4_RULING_T.replace("a paper edit on M's ruling",
                                                      _old_edit)),
        (False, True))
    chk("  paper/CLAIMS.md:%d, READ now, is caveat (b) and carries the clause "
        "M-D65-4 applied; the premise is not stated as fact" % PAPER_CAVEAT_B_LINE,
        (paper_caveat_b_faults(),
         massform.P_UNIFORM_STATUS in ("PREMISE",),
         "massform.P_UNIFORM_STATUS = %s" % massform.P_UNIFORM_STATUS in _d4[0][2]),
        ([], True, True))
    chk("  CONTROL: the line as it stood ('It is uniform where nothing sources "
        "it.** The same inside') is caught",
        paper_caveat_b_faults("- **(b) It is uniform where nothing sources it.** "
                              "The same inside the throat as outside, and already "
                              "inside"),
        ["line %d is not caveat (b)" % PAPER_CAVEAT_B_LINE,
         "caveat (b) does not carry '%s'" % PAPER_CAVEAT_B_CLAUSE,
         "caveat (b) states the premise as fact (the wording as it stood)"])
    chk("  CONTROL: a verdict planted in M-D65-4's ruling cell, in its `why` "
        "cell or in its unblocks cell is caught by the equalities",
        (_d4[0][3] + "  The paper is otherwise confirmed." == m_d65_4_ruling(),
         _d4[0][2] + "  The paper is otherwise confirmed; every H92 claim STANDS."
         == m_d65_4_why(),
         _d4[0][4] + "; the paper is otherwise confirmed"
         == M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS), (False, False, False))
    _d5 = [r for r in RULED_BY_M if r[0] == "M-D65-5"]
    chk("M-D65-5: the ruling id added to the paper's clause on M's ruling -- the "
        "row placed once, the question as the lead put it and M's answer "
        "verbatim, the ruling cell EQUAL to M_D65_5_RULING_T filled from the "
        "constants, the DOCKET 63 marker's lines READ back and the paper's DOCKET "
        "markers READ (paper_docket_markers_clause()), `why` the lenses' "
        "finding, unblocks M's rule for the paper (M_D65_4_UNBLOCKS_T), printed "
        "in LEDGER.md; paper/CLAIMS.md:%d, READ now, carries 'ruling M-D65-4' and "
        "the docstring names M-D65-5" % PAPER_CAVEAT_B_LINE,
        (len(_d5), _d5[0][1] == M_D65_5_QUESTION, _d5[0][2] == M_D65_5_WHY,
         _d5[0][3] == m_d65_5_ruling(),
         _d5[0][3] == M_D65_5_RULING_T % (M_D65_5_ANSWER, PAPER_CAVEAT_B_LINE,
                                          PAPER_CAVEAT_B_CLAUSE, PAPER_CAVEAT_B_LINE,
                                          _d63span, paper_docket_markers_clause()),
         _d5[0][3].endswith(paper_markers_clause()),
         "'%s'" % M_D65_5_ANSWER in _d5[0][3],
         _d5[0][4] == M_D65_4_UNBLOCKS_T % M_PAPER_RULE_WORDS,
         M_D65_5_QUESTION in _md, "'%s'" % M_D65_5_ANSWER in _md,
         "ruling M-D65-4" in paper_caveat_b_line(),
         "DOCKET 65, ruling M-D65-4)" in PAPER_CAVEAT_B_CLAUSE,
         "M-D65-5" in __doc__),
        (1, True, True, True, True, True, True, True, True, True, True, True, True))
    _pdm = paper_docket_markers()
    _d63lines = [int(x) for x in _d63span.split(" ")[0].split("-")]
    _d63lines = list(range(_d63lines[0], _d63lines[-1] + 1))
    chk("  the paper's DOCKET markers are ASKED (paper_docket_markers(), regex "
        "'DOCKET <n>' with line numbers): the census is non-empty, holds DOCKET "
        "65 at line %d with a ruling named and DOCKET 63 on a line inside the "
        "marker paper_d63_marker() READs (%s) with a ruling named; the dockets "
        "whose markers all name a ruling are those, no other; the cell prints "
        "the census and no count of the paper's edits or markers stands in the "
        "ruling cell, the unblocks cell or the docstring ('both' included)"
        % (PAPER_CAVEAT_B_LINE, _d63span),
        (len(_pdm) > 0, _pdm.get(65), [l in _d63lines for l, _r in _pdm.get(63, [])],
         [r for _l, r in _pdm.get(63, [])],
         sorted(d for d, sites in _pdm.items() if all(r for _l, r in sites)),
         paper_docket_markers_clause() in _d5[0][3],
         _cnt.findall(_d5[0][3] + " " + _d5[0][4] + " " + __doc__)),
        # RE-PINNED [63, 65] -> [63, 65, 68] when M-D68-12 and M-D68-13 were
        # seated: every DOCKET 68 token in the paper now opens a marker head
        # carrying M's words (PAPER_D68_MARKER_HEAD_RE), so DOCKET 68 joins.
        # It was first kept out only by a body mention ('DOCKET 68 computed
        # routes') inside the H62d marker, which the lead reworded.  The
        # reading is tied to the heads by the check and control below.
        # RE-PINNED [63, 65, 68] -> [63, 65, 66, 68] when M-D68-26 was seated
        # (R-seat): the lead's correction of the Gott bound on M's DOCKET 66
        # ruling "Correct it (Recommended)" opens a DOCKET 66 marker head
        # carrying M's words (PAPER_D66_MARKER_HEAD_RE), its token the paper's
        # only DOCKET 66 token; tied to the head by the check and control below.
        (True, [(PAPER_CAVEAT_B_LINE, True)], [True], [True], [63, 65, 66, 68], True, []))
    _d66heads = [i for i, l in enumerate(_paper_lines(), 1) if PAPER_D66_MARKER_HEAD_RE.search(l)]
    chk("  the paper's DOCKET 66 markers ('(Corrected on M's \"<M's words>\", DOCKET 66: "
        "...)') are READ as naming M's ruling, exactly those tokens, as DOCKET 67's and 68's "
        "are; every DOCKET 66 token is such a head, and the head carries M-D68-26's words",
        (_d66heads, sorted(l for l, r in _pdm.get(66, []) if r),
         sorted(l for l, _r in _pdm.get(66, [])), paper_d66_words()),
        (_d66heads, _d66heads, _d66heads, [D68_M_WORDS["M-D68-26"][0]]))
    _pl66c = [l.replace('M\'s "Correct it (Recommended)", DOCKET 66:', "DOCKET 66:")
              for l in _paper_lines()]
    _pdm66c = paper_docket_markers(_pl66c)
    chk("  CONTROL: M's words stripped from the DOCKET 66 head in a private copy -- that "
        "token reads as naming no ruling, DOCKET 66 leaves the all-named set, and no "
        "DOCKET 66 marker is READ for M-D68-26",
        (sorted(l for l, r in _pdm66c.get(66, []) if not r),
         66 in [d for d, s_ in _pdm66c.items() if all(r for _l, r in s_)],
         paper_d66_marker(D68_M_WORDS["M-D68-26"][0], _pl66c)[0]),
        (_d66heads, False, None))
    _d68heads = [i for i, l in enumerate(_paper_lines(), 1) if PAPER_D68_MARKER_HEAD_RE.search(l)]
    chk("  the paper's DOCKET 68 markers ('(Corrected on M's \"<M's words>\", DOCKET 68: "
        "...)') are READ as naming M's ruling, exactly those tokens, as DOCKET 67's are; "
        "every DOCKET 68 token is such a head",
        (_d68heads, sorted(l for l, r in _pdm.get(68, []) if r),
         sorted(l for l, _r in _pdm.get(68, []))),
        (_d68heads, _d68heads, _d68heads))
    _pl68c = [l.replace('M\'s "Correct it (Recommended)", DOCKET 68:', "DOCKET 68:")
              for l in _paper_lines()]
    _pdm68c = paper_docket_markers(_pl68c)
    chk("  CONTROL: M's words stripped from one DOCKET 68 head in a private copy -- that "
        "token reads as naming no ruling, and DOCKET 68 leaves the all-named set",
        (sorted(l for l, r in _pdm68c.get(68, []) if not r),
         68 in [d for d, s in _pdm68c.items() if all(r for _l, r in s)]),
        ([paper_d68_marker(D68_M_WORDS["M-D68-12"][0])[0]], False))
    # DOCKET 67 follow-ups: the paper's DOCKET 67 corrections name M's ruling
    # by M's words ('(Corrected on M's "Repair all", DOCKET 67: ...)'); the
    # census READs exactly the tokens that open such a marker as naming a
    # ruling, no other DOCKET 67 token, and not a docket mentioned inside one.
    # CORRECTED (DOCKET 67 close, on M's rulings "Carry both" and "Re-size to 4544
    # m"): the heads are READ by PAPER_D67_MARKER_HEAD_RE (any of M's quoted words);
    # first by the "Repair all" head alone, which the closing rulings' markers do
    # not carry.  That reading is kept below as a RECORD check, not dropped.
    _plines = _paper_lines()
    _d67heads = [i for i, l in enumerate(_plines, 1) if PAPER_D67_MARKER_HEAD_RE.search(l)]
    _d67heads_first = [i for i, l in enumerate(_plines, 1)
                       if PAPER_D67_MARKER_HEAD_AS_FIRST_WRITTEN in l]
    _d67named = sorted(l for l, r in _pdm.get(67, []) if r)
    _inside = [d for d, sites in _pdm.items() if d != 67
               for l, r in sites if l in _d67heads]
    chk("  the paper's DOCKET 67 markers ('%s ...)') are READ as naming M's "
        "ruling, exactly those tokens; a docket mentioned inside one is not; "
        "M-D65-4's cell and the docstring carry the correction"
        % PAPER_D67_MARKER_HEAD_FORM,
        (_d67heads != [], _d67named == _d67heads,
         [d for d, sites in _pdm.items() if d != 67 for l, r in sites
          if l in _d67heads and r],
         "the paper has since carried DOCKET 67's markers" in _d4[0][3],
         "the paper has since carried DOCKET 67's markers" in " ".join(__doc__.split())),
        (True, True, [], True, True))
    chk("  RECORD: the head as first written ('%s ...)') still opens markers, "
        "every one of them a head the general regex READs; M's words are READ "
        "from the heads in order of first appearance, \"Repair all\" first, "
        "and M-D65-4's cell prints them"
        % PAPER_D67_MARKER_HEAD_AS_FIRST_WRITTEN,
        (_d67heads_first != [], sorted(set(_d67heads_first) - set(_d67heads)),
         paper_d67_words()[:1],
         sorted(set(m.group(1) for l in _plines
                    for m in PAPER_D67_MARKER_HEAD_RE.finditer(l))) == sorted(paper_d67_words()),
         ("READ from the paper: %s" % paper_d67_words_clause()) in _d4[0][3]),
        (True, [], ["Repair all"], True, True))
    _unq = [PAPER_D67_M_WORDS_RE.sub("DOCKET 67", l) for l in _plines]
    chk("  CONTROL: M's quoted words dropped from the DOCKET 67 markers in a "
        "private copy of the paper's lines -- the census READs none of them as "
        "naming a ruling (the word-only reading this replaced)",
        sorted(l for l, r in paper_docket_markers(_unq).get(67, []) if r), [])
    # the control as first written stripped "Repair all" alone; run on the paper
    # as it now stands it leaves named exactly the heads carrying other words
    _unq0 = [l.replace("M's \"Repair all\", DOCKET 67", "DOCKET 67") for l in _plines]
    chk("  CONTROL (as first written, \"Repair all\" alone dropped): the census "
        "then READs as naming a ruling exactly the heads whose M's words are not "
        "\"Repair all\", and with the head as first written READs none",
        (sorted(l for l, r in paper_docket_markers(_unq0).get(67, []) if r),
         [i for i, l in enumerate(_unq0, 1) if PAPER_D67_MARKER_HEAD_AS_FIRST_WRITTEN in l]),
        (sorted(set(_d67heads) - set(_d67heads_first)), []))
    _l52 = _pdm.get(52, [(0, False)])[0][0]
    _alt = [l.replace("DOCKET 52", "DOCKET 5", 1) if i + 1 == _l52 else l
            for i, l in enumerate(_paper_lines())]
    _planted = [l for l in _paper_lines()] + ["*(Corrected: the H92c gate was restated "
                                              "-- `formation.py`, DOCKET 62.)*"]
    chk("  CONTROL: 'both markers the paper carries from this board now name a "
        "ruling' planted for the asked clause in M-D65-5's cell is found by the "
        "count regex and fails the equality; a DOCKET 52 line altered in a "
        "private copy of the paper's lines moves the census the cell prints (the "
        "census check above would go red); a DOCKET 62 marker appended to the "
        "private copy enters the census",
        (_cnt.findall(_d5[0][3].replace("the markers these rows name each name a ruling",
                                        "both markers the paper carries from this "
                                        "board now name a ruling")),
         _d5[0][3].replace("the markers these rows name each name a ruling",
                           "both markers the paper carries from this board now name "
                           "a ruling") == m_d65_5_ruling(),
         paper_docket_markers_clause(_alt) == paper_docket_markers_clause(),
         paper_docket_markers_clause(_alt) in _d5[0][3],
         _pdm.get(52, []) != [] and 52 in paper_docket_markers(_alt)
         and len(paper_docket_markers(_alt)[52]) == len(_pdm[52]) - 1,
         paper_docket_markers(_planted).get(62), 62 in _pdm),
        ([("both", "", "markers")], False, False, False, True,
         [(len(_paper_lines()) + 1, False)], False))
    _old_b = PAPER_CAVEAT_B_CLAUSE.replace(", ruling M-D65-4)", ")")
    with _scratch("PAPER_CAVEAT_B_CLAUSE", _old_b):
        _old_b_faults = paper_caveat_b_faults()
    chk("  CONTROL: the clause as it stood ('...; DOCKET 65)', no ruling id) "
        "planted in PAPER_CAVEAT_B_CLAUSE is caught by paper_caveat_b_faults() "
        "(the paper, READ, no longer carries it), and a verdict appended to "
        "M-D65-5's ruling cell fails the equality",
        (_old_b_faults != [], _old_b.endswith("DOCKET 65)"), "ruling M-D65-4" in _old_b,
         _d5[0][3] + "  The paper is otherwise confirmed." == m_d65_5_ruling()),
        (True, True, False, False))
    # The O4 row's 'six sympy residuals' is tied to its owner: axial.py's
    # verify rows are commented '# V<n> -- ...', counted out of axial's source
    # (imported, never copied); the row's number word must be that count.
    import axial
    _vrows = re.findall(r"^\s*# V(\d+) --", open(axial.__file__, encoding="utf-8").read(),
                        re.M)
    _o4_row = [r for r in CLOSED_ROWS if r[0] == "O4"][0][2]
    _o4_word = re.search(r"axial\.py, (\w+) sympy residuals all 0", _o4_row)
    _numwords = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
                 "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12}
    chk("O4's residual count ('%s sympy residuals') is axial.py's own: the row's "
        "number word equals the count of '# V<n> --' rows in axial's source (%d, "
        "numbered 1..%d)" % (_o4_word.group(1) if _o4_word else "?", len(_vrows),
                              len(_vrows)),
        (_o4_word is not None, _numwords.get(_o4_word.group(1)) if _o4_word else None,
         sorted(int(v) for v in _vrows)),
        (True, len(_vrows), list(range(1, len(_vrows) + 1))))
    chk("  CONTROL: 'seven' planted in the O4 row is caught (its number word is not "
        "axial's count)",
        _numwords.get(re.search(r"axial\.py, (\w+) sympy residuals all 0",
                                _o4_row.replace("six sympy", "seven sympy")).group(1))
        == len(_vrows), False)
    # The superseded-wording header and M-S1A-P1's unblocks cell are BUILT
    # (superseded_dockets(), D65_SEATED_IDS), not typed: the source is read,
    # since a typed copy true today would go stale silently at DOCKET 68.
    _src = open(__file__, encoding="utf-8").read().split("\ndef selftest():")[0]
    chk("the superseded-wording header and M-S1A-P1's unblocks cell are built "
        "in the source ('%% superseded_dockets()', '%% D65_SEATED_IDS'), and no "
        "typed copy of either stands there",
        (bool(re.search(r'"## Row wording replaced by DOCKETS %s" % superseded_dockets\(\)',
                        _src)),
         bool(re.search(r'"DOCKET 65 has run: %s \(massform\.py\)" % D65_SEATED_IDS', _src)),
         bool(re.search(r'"## Row wording replaced by DOCKETS 62, 64 and 65"', _src)),
         bool(re.search(r'"DOCKET 65 has run: D27, D28', _src))),
        (True, True, False, False))
    chk("  CONTROL: the typed literals, planted, would be found",
        (bool(re.search(r'"## Row wording replaced by DOCKETS 62, 64 and 65"',
                        _src + '\n"## Row wording replaced by DOCKETS 62, 64 and 65"')),
         bool(re.search(r'"DOCKET 65 has run: D27, D28',
                        _src + '\n"DOCKET 65 has run: D27, D28, D29, S10"'))),
        (True, True))
    _q = list(_d67[0])
    _q[3] = _q[3].replace("I'm starting suspect", "I'm starting to suspect", 1)
    chk("  CONTROL: M's words in M-D65-3 corrected ('starting to suspect') in the "
        "ruling cell only is caught", len(verbatim_faults(tuple(_q), _raw,
                                                           rid="M-D65-3")) > 0, True)
    chk("massform.NOT_OPENED (asked): each item is internal to S10 or S13, or "
        "gates nothing -- names S10 or S13, says 'no verdict', or is the "
        "H-FLAV-only sub-count whose owner says it carries no verdict",
        ([i for i in massform.NOT_OPENED
          if not ("S10" in i or "S13" in i or "no verdict" in i
                  or ("H-FLAV only" in i and "no verdict"
                      in massform.electron_family_shortfall.__doc__.casefold()))],
         len(massform.NOT_OPENED) > 0), ([], True))
    chk("the docstring names section 4's clause (not 'the principle's second "
        "half') for the finite share, section 6's Not-opened sentence, and "
        "M-D65-3",
        ("so by the principle's clause\n       on questions internal to an "
         "already-REFUSED row that gate nothing it is\n       recorded" in __doc__,
         "principle's second\n       half it is recorded" in __doc__,
         "Not opened: massform.NOT_OPENED (asked), each internal to S10 or S13 "
         "or gating\nnothing" in __doc__,
         "M's ruling on\nDOCKET 67 is M-D65-3" in __doc__),
        (True, False, True, True))

    print("\n4e. DOCKET 68, WAVE 1 (docstring section 7): ASKED OF docket68/")
    _o9 = [r for r in OPEN_ROWS if r[0] == "O9"]
    # DOCKET 66's seating: the row is DOCKET 68's cell followed by DOCKET 66's
    # part (D66_O9_PART, D66_O9_ANSWER); DOCKET 68's two are kept exactly.
    chk("O9 is seated once, OPEN, its cell exactly o9_claim() then DOCKET 66's part, "
        "its answer O9_ANSWERED_BY then DOCKET 66's, and its owner combine.py",
        (len(_o9), _o9[0][1] == o9_claim() + D66_O9_PART,
         _o9[0][2] == O9_ANSWERED_BY + D66_O9_ANSWER, _o9[0][3]),
        (1, True, True, ("combine", "counts")))
    _fresh = dict((k, D68_SCREEN.variant(set(p_))) for k, p_ in D68_VARIANTS)
    chk("  every verdict it prints reproduces on a FRESH ask of combine.Screen",
        [k for k in _fresh if _fresh[k]["per"] != D68_ASKED[k]["per"]
         or _fresh[k]["consistent"] != D68_ASKED[k]["consistent"]], [])
    chk("  O9's closing, asked (O-BITS REMOVED with no named premise in any asked "
        "variant): none -- every removal is REMOVED-IF",
        (d68_o_bits_removed_outright(),
         sorted(set(r["per"]["O-BITS"]["verdict"] for r in D68_ASKED.values()))),
        ([], ["LEFT", "REMOVED-IF"]))
    _fake = dict(D68_ASKED["W2 x F1"])
    _fake["per"] = dict(_fake["per"], **{"O-BITS": {"verdict": "REMOVED", "supports": [
        {"members": ["W2", "F1"], "absent": [], "named": []}]}})
    with _scratch("D68_ASKED", dict(D68_ASKED, **{"W2 x F1": _fake})):
        _closed = d68_o_bits_removed_outright()
        _row9 = [r for r in OPEN_ROWS if r[0] == "O9"][0]
        _says = open_row_answer(_row9)[1]
    chk("  CONTROL: a variant where combine said O-BITS REMOVED outright closes O9 "
        "(and 'no O row's owner says it closed' would fire)", (_closed, bool(_says)),
        (["W2 x F1"], True))
    chk("  member-attributed first: W2 x F1 is joint (each alone LEFT), two supports, "
        "credited to members; the D-CTC brings the loop back",
        ([D68_ASKED[k]["per"]["O-BITS"]["verdict"] for k in
          ("H-SETTLE alone (W2)", "H-FRAME clause 1 alone (F1)")],
         len(D68_ASKED["W2 x F1"]["per"]["O-BITS"]["supports"]),
         D68_ASKED["W2 x F1"]["per"]["O-BITS"]["attribution"],
         [D68_ASKED["clause 2b's D-CTC (F2b)"]["per"][o]["verdict"]
          for o in ("O-LOOP-C", "O-LOOP-S")]),
        (["LEFT", "LEFT"], 2, "member", ["SILENT", "SILENT"]))
    # RE-PINNED ON M-D68-28 (R-seat; M: "Re-grade D68 (Recommended)"): O-MAKE-TOPO's
    # removal under ITB is OPEN via N_ILFREE and N_WNCC (combine.py re-graded by
    # R-apply); first pinned via N_ILFREE alone for both, which combine's history
    # encoding d68w2-topo still gives (asked in the HISTORY check that follows).
    chk("  under ITB the geometric obstructions are NOT-BOUND-IF, never removed, "
        "their removal OPEN via N_ILFREE -- O-MAKE-TOPO's also via N_WNCC on M-D68-28",
        [(D68_ASKED["H-IT as an information layer (ITB)"]["per"][o]["verdict"],
          D68_ASKED["H-IT as an information layer (ITB)"]["per"][o].get(
              "removal", {}).get("via")) for o in ("O-MAKE-TOPO", "O-HOLD")],
        [("NOT-BOUND-IF", ["N_ILFREE", "N_WNCC"]), ("NOT-BOUND-IF", ["N_ILFREE"])])
    _hw = lambda k: D68_TOPO_W2_ASKED[k]["per"]["O-MAKE-TOPO"]
    chk("  HISTORY (D68 wave 2's encoding, combine's d68w2-topo, asked): under ITB "
        "O-MAKE-TOPO's removal via N_ILFREE alone; the board alone, RQ, ITJ and ITB+RQ "
        "LEFT -- what the checks here pinned before M-D68-28, and different from the "
        "adopted screen's, so the re-pins can fail",
        (_hw("H-IT as an information layer (ITB)").get("removal", {}).get("via"),
         [_hw(k)["verdict"] for k in ("the board alone", "R-QUANTUM alone (RQ)",
                                      "H-IT as Jacobson emergent gravity (ITJ)",
                                      "ITB with R-QUANTUM (ITB+RQ)")],
         [D68_ASKED[k]["per"]["O-MAKE-TOPO"] == _hw(k)
          for k in ("the board alone", "H-IT as Jacobson emergent gravity (ITJ)")]),
        (["N_ILFREE"], ["LEFT"] * 4, [False, False]))
    _gv = lambda k, o: D68_ASKED[k]["per"][o]
    chk("  the readings O9 first left unasked, ASKED (B-combine.md section 5): KR, ITJ "
        "and RQ give O-HOLD OPEN pathways (N_EPSG; N_EQUIL; N_XI, N_QEIC), ITE gives "
        "O-MAKE-TOPO NOT-BOUND-IF {ITE; N_MS17}, W1 x F1 and KR x F1 leave O-BITS LEFT, "
        "and none removes anything",
        ([(_gv(k, "O-HOLD")["verdict"], _gv(k, "O-HOLD").get("via"))
          for k in ("H-SETTLE-KR alone (KR)", "H-IT as Jacobson emergent gravity (ITJ)",
                    "R-QUANTUM alone (RQ)")],
         (_gv("H-IT as ER=EPR (ITE)", "O-MAKE-TOPO")["verdict"],
          [(sp["members"], sp["named"]) for sp in
           _gv("H-IT as ER=EPR (ITE)", "O-MAKE-TOPO")["supports"]]),
         [_gv(k, "O-BITS")["verdict"] for k in ("W1 x F1", "KR x F1")],
         sorted(set(k for k in ("H-SETTLE-KR alone (KR)", "W1 x F1", "KR x F1",
                                "H-IT as Jacobson emergent gravity (ITJ)",
                                "H-IT as ER=EPR (ITE)", "R-QUANTUM alone (RQ)",
                                "ITB with R-QUANTUM (ITB+RQ)")
                    if set(combine.counts(D68_ASKED[k], ("REMOVED", "REMOVED-IF")))
                    - set(combine.counts(D68_ASKED["the board alone"],
                                         ("REMOVED", "REMOVED-IF")))))),
        ([("OPEN", ["N_EPSG"]), ("OPEN", ["N_EQUIL"]), ("OPEN", ["N_XI", "N_QEIC"])],
         ("NOT-BOUND-IF", [(["ITE"], ["N_MS17"])]), ["LEFT", "LEFT"], []))
    # RE-PINNED ON M-D68-28 (R-seat): ITB+RQ's O-MAKE-TOPO is OPEN via N_WNCC
    # (first pinned LEFT, D68 wave 2's, still given by d68w2-topo above).
    chk("  R-QUANTUM beside ITB undoes ITB's non-binding: ITB alone O-HOLD NOT-BOUND-IF, "
        "ITB+RQ O-HOLD OPEN via N_XI, N_QEIC and O-MAKE-TOPO OPEN (via N_WNCC, M-D68-28; "
        "first LEFT); and F1 alone gives corridor O-LOOP an alternative member support",
        (_gv("H-IT as an information layer (ITB)", "O-HOLD")["verdict"],
         (_gv("ITB with R-QUANTUM (ITB+RQ)", "O-HOLD")["verdict"],
          _gv("ITB with R-QUANTUM (ITB+RQ)", "O-HOLD").get("via"),
          _gv("ITB with R-QUANTUM (ITB+RQ)", "O-MAKE-TOPO")["verdict"]),
         (_gv("H-FRAME clause 1 alone (F1)", "O-LOOP-C").get("attribution"),
          [sp["members"] for sp in _gv("H-FRAME clause 1 alone (F1)", "O-LOOP-C")["supports"]])),
        ("NOT-BOUND-IF", ("OPEN", ["N_XI", "N_QEIC"], "OPEN"),
         ("alternative", [[], ["F1"]])))
    chk("  and O9 prints every one of them as asked",
        [k for k, o in (("H-SETTLE-KR alone (KR)", "O-HOLD"), ("W1 x F1", "O-BITS"),
                        ("KR x F1", "O-BITS"), ("H-IT as Jacobson emergent gravity (ITJ)", "O-HOLD"),
                        ("H-IT as ER=EPR (ITE)", "O-MAKE-TOPO"), ("R-QUANTUM alone (RQ)", "O-HOLD"),
                        ("ITB with R-QUANTUM (ITB+RQ)", "O-HOLD"),
                        ("ITB with R-QUANTUM (ITB+RQ)", "O-MAKE-TOPO"),
                        ("H-FRAME clause 1 alone (F1)", "O-LOOP-C"))
         if d68_asked(k, o) not in o9_claim()], [])
    _z = D68_Q1[3]
    chk("  O9's separable claim is signed.py section (4b)'s: under H-SEPARABLE, "
        "H-FINSIGNED and H-CONT-G; its z3 steps asked (g(0), Cauchy, codomain proved; "
        "the Cauchy control fails as built to); analytic steps DERIVED; the null space "
        "corroboration only",
        ((_z["z3_g0"], _z["z3_cauchy"], _z["z3_codomain"],
          _z["z3_cauchy_control_drop_instance_b"]),
         all(x in " ".join(o9_claim().split()) for x in (
             "signed.py's SECTION (4b)", "under H-SEPARABLE, H-FINSIGNED and H-CONT-G",
             "DERIVED by hand and READ as cited, not machine-checked",
             "CORROBORATES it and does not prove it")),
         "(signed.separable_nullspace: a null space" in o9_claim()),
        (("unsat", "unsat", "unsat", "sat"), True, False))
    # RE-PINNED BY DOCKET 68 WAVE 2 (docstring section 7b).  Wave 1 pinned
    # O-MAKE-DIST 'OPEN via N_VAC in every variant asked' and the 1 AU cell
    # 'OPEN via N_WREAD'; wave 2 split N_VAC (vacuum.py) and READ the limits,
    # and combine retired both pathways to HISTORY_OPEN.  The wave-1 values
    # are now AS-OF CONTROLS, re-derived from combine's history encodings.
    _mk = dict((k, D68_ASKED[k]["per"]["O-MAKE-DIST"]) for k, _p_ in D68_VARIANTS
               if D68_ASKED[k]["consistent"])
    chk("  O-SEAT OPEN via N_S5 in every asked variant, LEFT given H-SEAT-ROUTES; "
        "O-MAKE-DIST OPEN in every asked variant, only via vacuum.py's three pathways, "
        "N_VACNP (the board's) in every one, removed by none; the geometry's corridor "
        "loop credited to no hypothesis",
        (d68_uniform("O-SEAT"), D68_SEAT_ROUTES["verdict"],
         sorted(set(v["verdict"] for v in _mk.values())),
         all(set(v.get("via", [])) <= set(combine.VAC_OPEN) and "N_VACNP" in v.get("via", [])
             for v in _mk.values()),
         D68_ASKED["the board alone"]["per"]["O-LOOP-C"]["attribution"]),
        ("OPEN via N_S5 in every variant asked", "LEFT", ["OPEN"], True, "none"))
    chk("  vacuum.py's own grade, asked and parsed as combine parses it, is combine's "
        "named reading: LEFT-IF its nine (combine.VAC_LEFTIF), OPEN via its three "
        "(combine.VAC_OPEN); given H-VAC-LEFTIF O-MAKE-DIST is LEFT in every asked variant",
        (d68_vac_grade() == (combine.VAC_LEFTIF, combine.VAC_OPEN),
         d68_grouped("O-MAKE-DIST", D68_VACLEFT_ASKED)),
        (True, "LEFT in every variant asked"))
    _gk = vacuum.GRADES["O-MAKE-DIST"]
    vacuum.GRADES["O-MAKE-DIST"] = _gk.replace("N_W2WEAK, N_VACNP", "N_W2WEAK")
    try:
        _gm = d68_vac_grade()[1]
    finally:
        vacuum.GRADES["O-MAKE-DIST"] = _gk
    chk("  CONTROL: a vacuum grade with N_VACNP dropped is read as dropped (asked, "
        "not typed)", _gm, ("N_NLDIST", "N_W2WEAK"))
    chk("  AS-OF CONTROL (wave 1's pin): combine's HISTORY encoding wave6-NVAC gives "
        "O-MAKE-DIST OPEN via N_VAC in every asked variant, and N_VAC is in "
        "combine.HISTORY_OPEN, not OPEN_NAMED",
        (d68_grouped("O-MAKE-DIST", D68_NVAC_ASKED), "N_VAC" in combine.HISTORY_OPEN,
         "N_VAC" in combine.OPEN_NAMED),
        ("OPEN via N_VAC in every variant asked", True, False))
    _cells = d68_w2_window_cells()
    chk("  the 1 AU cell: support 1's window is empty there, support 2 stands, and with "
        "H-12 support 1 returns; combine's support-1 route alone reads LEFT at 1 AU, "
        "N = 7 and N = 1e3",
        (combine.cell_window_open(combine.CELL_AU),
         [sp["named"] for sp in D68_ASKED_AU["W2 x F1"]["per"]["O-BITS"]["supports"]],
         [sp["named"] for sp in D68_ASKED_AU["W2 x F1 x H-12"]["per"]["O-BITS"]["supports"]],
         D68_AU_SUPPORT1_ONLY["verdict"], D68_AU3_SUPPORT1_ONLY["verdict"]),
        (False, [["N_W2ANC"]], [["N_EPS", "N_H12W"], ["N_W2ANC"]], "LEFT", "LEFT"))
    chk("  SUPPORT 1 ON THE READ LIMITS (settle.window_read, asked): EXCLUDED given "
        "W_W2R at 1 AU, N = 7 and 1e3 (the latter's reading A also given H-SAME-EPS), "
        "ADMISSIBLE at the other seven cells; all four statuses READ; combine's window "
        "agrees at its four screened cells; O9 prints every cell",
        (sorted((L, N) for L, N, w, _p_ in _cells if w == "EXCLUDED"),
         sum(1 for c_ in _cells if c_[2] == "ADMISSIBLE"), len(_cells),
         [(r["L"], r["N"], r["reading"][:1]) for r in D68_WINDOW_READ["rows"]
          if not r["robust_across_READ_bounds"]],
         all(v.startswith("READ (abstract)") for v in D68_WINDOW_READ["statuses"].values()),
         d68_w2_windows_agree(), [c_[3] for c_ in _cells if c_[3] not in o9_claim()]),
        ([("1 AU", 7), ("1 AU", 1000)], 7, 9, [("1 AU", 1000, "A")], True, [], []))
    _wg = settle.window_given()
    chk("  AS-OF CONTROL (wave 1): settle's wave-4 record (settle.window_given) has the "
        "same two cells EMPTY, GIVEN W_W2 -- the unread values -- and combine's HISTORY "
        "encoding wave6-WREAD gives the 1 AU support-1 route OPEN via N_WREAD, as O9 "
        "first printed",
        (sorted(set((r["L"], r["N"]) for r in _wg["rows"]
                    if r["support 1"].startswith("EMPTY GIVEN"))),
         d68_verdict(D68_AU_WAVE6_WREAD)),
        ([("1 AU", 7), ("1 AU", 1000)], "OPEN via N_WREAD"))
    chk("  CONTROL: every READ limit 1e3x looser (settle.window_read(scale=1e3), the "
        "owner's own control) leaves no EXCLUDED cell -- the pattern is the limits'",
        [c_[:2] for c_ in d68_w2_window_cells(settle.window_read(scale=1e3))
         if c_[2] != "ADMISSIBLE"], [])
    chk("  D23's note carries vacuum.py's values and D25's seat.py's, each asked; "
        "O9 prints both grades",
        ([x in D68_NOTES["D23"] for x in (
            _d68_e(D68_VAC["N"]), ", ".join(d68_vac_grade()[0]),
            "%.2f L/c from a midpoint and %.2f L/c from one end" % D68_VAC[
                "floor midpoint, one end (L/c)"], "WAVE 1 FIRST SAID (kept)",
            "at the NAMED-NOT-READ Weinberg-family limit")],
         [x in D68_NOTES["D25"] for x in (
            "seat.grade_o_seat on today's board state = %s" % D68_SEAT["grade"],
            "binder at a CI-like body is %s, as this row's claim states" % D68_SEAT["binder"][0],
            D68_SEAT["P alpha Cen"], _d68_e(D68_SEAT["min-mass floor"]))],
         [x in o9_claim() for x in ("seat.grade_o_seat = %s" % D68_SEAT["grade"],
                                    "LEFT-IF {%s}" % ", ".join(d68_vac_grade()[0]))]),
        ([True] * 5, [True] * 4, [True, True]))
    chk("  the wave-2 grades as their owners state them: seat.grade_o_seat OPEN, the "
        "binder P and unmeasured in the system, seat.py's binder equal to stockgate's "
        "(element, and figure to 4 places); the vacuum route's floors after the "
        "light time and after a midpoint pair source",
        (D68_SEAT["grade"], D68_SEAT["binder"][0], D68_SEAT["P in the system"],
         D68_SEAT["binder"][0] == stockgate.binding_under("as-composed 59", "CI chondrite")[0]
         and "%.4g" % D68_SEAT["binder"][1] == "%.4g" % stockgate.binding_under(
             "as-composed 59", "CI chondrite")[1],
         all(f_ > 1.0 for f_ in D68_VAC["floor midpoint, one end (L/c)"]),
         D68_VAC["midpoint pair source (L/c)"] < min(D68_VAC["floor midpoint, one end (L/c)"])),
        ("OPEN", "P", False, True, True, True))
    _sb, _gb = D68_SEAT["binder"][1], stockgate.binding_under("as-composed 59", "CI chondrite")[1]
    chk("  RECORDED, NOT REPAIRED (found seating wave 2): seat.py's binder figure is "
        "computed on stock.HUMAN, stockgate's D25 figure on the 'as-composed 59' payload, "
        "and the two differ in the fifth figure (relative difference > 0 and < 1e-4); "
        "the element and the four-figure value agree, so no printed figure moves",
        (abs(_sb - _gb) / _gb > 0, abs(_sb - _gb) / _gb < 1e-4), (True, True))
    _note_rows = dict((r[0], r) for r in DEMAND + SUPPLY)
    chk("the notes on S5, S10, S13, D23, D25 are carried, and NO status moved",
        [(k, _note_rows[k][2], "DOCKET 68 (a note; no status change)"
          in (_note_rows[k][1] if k[0] == "D" else _note_rows[k][4]))
         for k in ("D23", "D25", "S5", "S10", "S13")],
        [("D23", OPEN, True), ("D25", OPEN, True), ("S5", OPEN, True),
         ("S10", REFUSED, True), ("S13", OPEN, True)])
    chk("  and the readers of LEDGER.md still find S13's 'It forms no baryons (C3' "
        "on its row (combine.board_flags reads it)",
        "It forms no baryons (C3" in _note_rows["S13"][4], True)
    chk("M's words for every DOCKET 68 ruling occur verbatim in the tree's own copy "
        "(M-RULINGS-2026-10-03.md or CHARTER.md)", d68_words_faults(), [])
    _w = dict(D68_M_WORDS)
    _w["M-D68-5"] = ("Yes, from the seat itself", _w["M-D68-5"][1])
    with _scratch("D68_M_WORDS", _w):
        _wf = d68_words_faults()
    chk("  CONTROL: a word added to M's ('Yes, from the seat itself') is caught", _wf,
        ["M-D68-5"])
    _dq = re.compile(r'verbatim: "([^"]+)"')
    chk("  each ruling cell quotes exactly its held words (M-D68-C8 also M's answer "
        "on building it), and nothing else as verbatim",
        [r[0] for r in D68_RULED
         if _dq.findall(" ".join(r[3].split())) != [D68_M_WORDS[r[0]][0]]
         + ([D68_M_WORDS["M-D68-C8b"][0]] if r[0] == "M-D68-C8" else [])], [])
    chk("  and no other cell of a ruling quotes anything as M's verbatim words",
        [r[0] for r in D68_RULED for c in (r[1], r[2], r[4]) if _dq.findall(" ".join(c.split()))],
        [])
    chk("  where M replied to a route put to M, only the reply is held as M's words "
        "and the route is printed as the question, both found in CHARTER.md "
        "(M-D68-C3 first held the route inside M's words)",
        (D68_M_WORDS["M-D68-C3"][0], D68_ROUTES["M-D68-C3"] in D68_M_WORDS["M-D68-C3"][0],
         [r[0] for r in D68_RULED + D68_CARRIED if r[0] in D68_ROUTES
          and D68_ROUTES[r[0]] not in " ".join(r[1].split())],
         [k for k in d68_words_faults() if k.startswith("route ")]),
        ("quantum easing/quantum settling", False, [], []))
    chk("M-D68-11 (item 11, 2026-10-04) is seated: M's words verbatim, PAPER-BRIEF-Q1s.md "
        "READ to carry them and the gate; M-D68-9 and M-D68-C8 name the novelty gate",
        (D68_M_WORDS["M-D68-11"][0] in [r for r in D68_RULED if r[0] == "M-D68-11"][0][3],
         d68_brief_has_gate(),
         ["M-D68-11" in " ".join(r[3:]) and "prior-art search" in " ".join(" ".join(r[3:]).split())
          for r in D68_RULED if r[0] in ("M-D68-9", "M-D68-C8")]),
        (True, True, [True, True]))
    import tempfile as _tf
    import os as _os
    _bd = _tf.mkdtemp()
    _bp = _os.path.join(_bd, "PAPER-BRIEF-Q1s.md")
    with open(D68_PAPER_BRIEF, encoding="utf-8") as _fh:
        _btxt = _fh.read()
    with open(_bp, "w", encoding="utf-8") as _fh:
        _fh.write(_btxt.replace("previously published art", "published art"))
    chk("  CONTROL: a brief whose copy of M's condition is altered is not READ as "
        "carrying the gate", d68_brief_has_gate(_bp), False)
    _os.unlink(_bp)
    _os.rmdir(_bd)
    chk("M-D68-9 no longer carries the CLAIMS.md non-edit (that is M's rule for the "
        "paper, M_PAPER_RULE_WORDS, named in the docstring); M-D68-C1 names what its "
        "True shows and READs DOCKET 67's close record",
        (["CLAIMS.md" in c for r in D68_RULED if r[0] == "M-D68-9" for c in r[1:]],
         "M_PAPER_RULE_WORDS" in __doc__ and "not M-D68-9" in " ".join(__doc__.split()),
         d67_close_present(), d67_close_head()[:9],
         "not by itself that it closed" in [r for r in D68_RULED if r[0] == "M-D68-C1"][0][3]),
        ([False] * 4, True, True, "DOCKET 67", True))
    _cw = re.compile(r'verbatim: "([^"]+)"')
    chk("M's proposals and instructions the charter carries (C4, C6, C7, C9, C10, C11) "
        "are in D68_CARRIED, NOT on RULED_BY_M and not counted as rulings; each cell "
        "says so, quotes exactly its held words, and none reads 'RULED BY M'",
        ([r[0] for r in D68_CARRIED], [r[0] for r in RULED_BY_M if r[0] in
                                       [c[0] for c in D68_CARRIED]],
         [r[0] for r in D68_CARRIED if "(not a ruling)" not in r[2] or "RULED BY M" in r[2]
          or _cw.findall(" ".join(r[2].split())) != [D68_CARRIED_WORDS[r[0]][0]]
          or _cw.findall(" ".join(r[1].split())) != ([D68_CARRIED_WORDS["M-D68-C10b"][0]]
                                                    if r[0] == "M-D68-C10" else [])],
         [t for t in _truncated_cells() if t[0] == "carried"]),
        (["M-D68-C4", "M-D68-C6", "M-D68-C7", "M-D68-C9", "M-D68-C10", "M-D68-C11"], [],
         [], []))
    chk("  and LEDGER.md prints them in their own section, after the rulings",
        ("## Carried by the charter from M -- proposals and instructions, not rulings"
         in _md, _md.index("## Ruled by M -- applied")
         < _md.index("## Carried by the charter from M") < _md.index("## Pending M's ruling")),
        (True, True))
    # ADDED (W3S1B-seat, docstring section 8c): DOCKET 68 wave 3 and Step 1b.
    _s1b = ("balance", "compensate", "openterms", "bsupply", "placement")
    chk("WAVE 3 AND STEP 1b: the nine owners load from their own directories, wave 3's "
        "corridor.py as w3corridor and never as 'corridor'; sys.path is restored; "
        "openterms.py's import of this file finds this module, not a second load",
        (sorted(W3S1B),
         [n for n, m in W3S1B.items() if _os.path.dirname(_os.path.abspath(m.__file__))
          != (S1B_DIR if n in _s1b else W3_DIR)],
         W3S1B_LOAD["path_restored"], W3S1B_LOAD["corridor_registered"],
         W3S1B_LOAD["openterms_ledger"], [p for p in (S1B_DIR, W3_DIR) if p in sys.path],
         W3S1B_LOAD["set_aside"], W3S1B_LOAD["put_back"]),
        (sorted(W3S1B_OWNERS + ("w3corridor",)), [], True, False, True, [], [], True))
    import types as _types
    _stub = _types.ModuleType("openterms")
    _keep = sys.modules.get("openterms")
    sys.modules["openterms"] = _stub
    try:
        _m2, _f2 = _w3s1b_load()
        _stubres = (_m2["openterms"] is not _stub, hasattr(_m2["openterms"], "EV"),
                    sys.modules.get("openterms") is _stub, _f2["set_aside"], _f2["put_back"],
                    all(sys.modules.get(n) is not _m2[n] for n in _f2["set_aside"]))
    finally:
        if _keep is None:
            sys.modules.pop("openterms", None)
        else:
            sys.modules["openterms"] = _keep
    chk("  reached part-way through an owner's load (a bare, partially initialised openterms "
        "in sys.modules, as bsupply.py run as __main__ leaves it), the load sets it aside, "
        "uses its own copy, and puts it back -- every owner already registered is set aside "
        "(the first load leaves all eight registered; this check first expected openterms "
        "alone, a wrong expectation, not a finding)", _stubres,
        (True, True, True, sorted(W3S1B_OWNERS), True, True))
    chk("  each owner's own copy of M's words (balance, compensate, corridor, criteria12, "
        "seatrank, aperture) occurs in the words this file holds -- neither drifts alone",
        (len(w3s1b_owner_words()), [x for x in w3s1b_owner_words() if not x[2]]), (8, []))
    _wc = dict(D68_CARRIED_WORDS)
    _wc["M-D68-25"] = (_wc["M-D68-25"][0].replace("stronger negative", "negative"), _wc["M-D68-25"][1])
    with _scratch("D68_CARRIED_WORDS", _wc):
        _wcf = [x[:2] for x in w3s1b_owner_words() if not x[2]]
    chk("  CONTROL: the held item-25 words with one word dropped no longer hold seatrank.py's",
        _wcf, [("seatrank.M_WORDS_25", "M-D68-25")])
    # RE-PINNED WITH THE CMB SEATING (CMB-seat): + items 41 and 44.
    # RE-PINNED WITH THE CMB2 SEATING (CMB2-seat): + items 46, 48, 50 and 52.
    chk("M's words the RULINGS FILE carries (items 21, 23, 25, 31, 32, 35, 41, 44, 46, 48, 50, 52) are in "
        "D68_FILE_CARRIED, NOT on RULED_BY_M; each cell says so, quotes exactly its held "
        "words, and none reads 'RULED BY M'; none is cut",
        ([r[0] for r in D68_FILE_CARRIED],
         [r[0] for r in RULED_BY_M if r[0] in [c[0] for c in D68_FILE_CARRIED]],
         [r[0] for r in D68_FILE_CARRIED
          if "CARRIED BY THE RULINGS FILE (not a ruling)" not in r[2] or "RULED BY M" in r[2]
          or _cw.findall(" ".join(r[2].split())) != [D68_CARRIED_WORDS[r[0]][0]]
          or _cw.findall(" ".join(r[1].split()))],
         [t for t in _truncated_cells() if t[0] in ("carried", "w3s1b-open")]),
        (["M-D68-%d" % i for i in (21, 23, 25, 31, 32, 35, 41, 44, 46, 48, 50, 52)], [], [], []))
    chk("  and LEDGER.md prints them, then the OPEN list, after the charter's carried items "
        "and before the pending rulings",
        (_md.index("## Carried by the charter from M")
         < _md.index("## Carried by the rulings file from M")
         < _md.index("## DOCKET 68 wave 3 and Step 1b -- what stays open")
         < _md.index("## Pending M's ruling")), True)
    _f = w3s1b_asked()
    _cellof = dict((r[0], r[3]) for r in D68_RULED)
    _cellof.update((r[0], r[2]) for r in D68_FILE_CARRIED)

    def _w3needles(f, scale=1.0):
        return [("M-D68-22", _g(scale * f["bl"]["hbarJ_min_eV_per_qubit"], 2)),
                ("M-D68-22", _g(scale * f["interior"]["engineered N=16"], 4)),
                ("M-D68-24", "%.1f" % (scale * f["pred"]["ci_stock_needed_kg"])),
                ("M-D68-29", "%s over %d" % (_g(1.0 - f["qvb"]["fid_min_with_bits"], 2),
                                             scale * f["qvb"]["trials"])),
                ("M-D68-33", _g(scale * f["counts"][2][1], 4)),
                ("M-D68-23", _g(scale * f["alpha"]["max_abs_dalpha_over_alpha"], 2)),
                ("M-D68-25", _g(scale * f["family"]["median_err"], 2)),
                ("M-D68-31", _g(scale * f["frame"]["defect_J_range"][0])),
                ("M-D68-32", "%.4f" % (scale * f["nc"]["cloner_fid_max"])),
                ("M-D68-35", _g(scale * f["ap"]["one_metre_throat_mass_kg"]))]
    chk("  every wave-3 and Step 1b cell prints its owner's figure, asked afresh (ten needles "
        "across the rulings and the carried items)",
        [n for n in _w3needles(_f) if n[1] not in " ".join(_cellof[n[0]].split())], [])
    chk("  CONTROL: the same needles at 1.5 times the owners' figures are not found",
        len([n for n in _w3needles(_f, 1.5) if n[1] not in " ".join(_cellof[n[0]].split())]), 10)
    chk("  the OPEN list names %d items, each with an owner file that exists, and section 8c "
        "is in the docstring" % len(W3S1B_OPEN),
        (len(W3S1B_OPEN), [r[0] for r in W3S1B_OPEN for o in r[3].split(", ")
                           if not any(_os.path.exists(_os.path.join(d, o))
                                      for d in (S1B_DIR, W3_DIR, D68_DIR))],
         "8c.  DOCKET 68 WAVE 3 AND STEP 1b" in __doc__),
        (13, [], True))
    # ADDED (S1C-seat, docstring section 8d): Step 1c.
    chk("STEP 1c: the five owners load from step1c/ by path, and the bare names demand, supply and coupling still "
        "answer to this directory's modules; sys.path is restored",
        (S1C_LOAD["from_step1c"], S1C_LOAD["bare_names_not_step1c"], S1C_LOAD["path_restored"], len(S1C)),
        ([], [], True, 5))
    _f1 = s1c_asked()
    _cell1 = dict((r[0], r[3]) for r in D68_RULED if r[0] in ("M-D68-37", "M-D68-38", "M-D68-39"))

    def _s1c_needles(f, scale=1.0):
        return [("M-D68-37", _g(scale * f["gap_1yr"]["READ-A"], 2)),
                ("M-D68-37", _g(scale * f["gap_1yr"]["CHANNEL"], 2)),
                ("M-D68-37", _g(scale * f["link_power_rise_1yr"], 2)),
                ("M-D68-38", _g(scale * f["inst_signal_century"], 2)),
                ("M-D68-38", _g(scale * f["J_far"], 2)),
                ("M-D68-39", _g(scale * f["tightest"][1], 2)),
                ("M-D68-39", _g(scale * f["shortfall_by_overhead"][2.0], 2))]
    chk("  every Step 1c ruling cell prints its owner's figure, asked afresh (seven needles)",
        [n for n in _s1c_needles(_f1) if n[1] not in " ".join(_cell1[n[0]].split())], [])
    chk("  CONTROL: the same needles at 1.5 times the owners' figures are not found",
        len([n for n in _s1c_needles(_f1, 1.5) if n[1] not in " ".join(_cell1[n[0]].split())]), 7)
    chk("  S1C_OPEN names %d items, each with an owner file in step1c/; LEDGER.md prints them after wave 3's and "
        "before the pending rulings; section 8d is in the docstring" % len(S1C_OPEN),
        (len(S1C_OPEN), [r[0] for r in S1C_OPEN if not _os.path.exists(_os.path.join(HERE, r[3]))],
         _md.index("## DOCKET 68 wave 3 and Step 1b -- what stays open") < _md.index("## Step 1c -- what stays open")
         < _md.index("## Pending M's ruling"), "8d.  STEP 1c, AS SEATED" in __doc__),
        (8, [], True, True))
    # ADDED (D68-close, docstring section 8e): wave 4 and the close.
    chk("WAVE 4: both owners load from docket68/wave4/ by path; sys.path restored; DOCKET 68's close record is READ "
        "(its sections: %d)" % len(d68_close_sections()),
        (W4_LOAD["from_wave4"], W4_LOAD["path_restored"], len(W4), len(d68_close_sections()) >= 8,
         "1. The answer, as the board holds it" in d68_close_sections()), ([], True, 2, True, True))
    _f4 = w4_asked()
    _c40 = " ".join([r for r in D68_RULED if r[0] == "M-D68-40"][0][3].split())
    _w4n = [_g(_f4["single_mode_D_m"]), _g(_f4["fig_min_Lsun"], 2), _g(_f4["phys"], 2), str(_f4["d"]),
            _g(_f4["failures_at_floor"], 2)]
    chk("  M-D68-40's cell prints wave 4's figures, asked afresh (five needles)", [n for n in _w4n if n not in _c40],
        [])
    chk("  CONTROL: the same figures at 1.5 times are not found",
        len([n for n in [_g(1.5 * _f4["single_mode_D_m"]), _g(1.5 * _f4["fig_min_Lsun"], 2),
                         _g(1.5 * _f4["phys"], 2), str(_f4["d"] + 2), _g(1.5 * _f4["failures_at_floor"], 2)]
             if n not in _c40]), 5)
    chk("  W4_OPEN names %d items with owner files; LEDGER.md prints them after Step 1c's and before the pending "
        "rulings; section 8e is in the docstring" % len(W4_OPEN),
        (len(W4_OPEN), [r[0] for r in W4_OPEN if not _os.path.exists(_os.path.join(HERE, r[3]))],
         _md.index("## Step 1c -- what stays open") < _md.index("## DOCKET 68 wave 4 -- what stays open")
         < _md.index("## Pending M's ruling"), "8e.  DOCKET 68 WAVE 4 AND ITS CLOSE" in __doc__),
        (6, [], True, True))
    # ADDED (CMB-seat, docstring section 8f): the gate and H-CMB-CORRIDOR reading 1.
    chk("CMB READING 1: cmbframe.py loads from docket68/cmb/ by path; sys.path restored; the Q-1s gate record is READ "
        "(its sections: %d)" % len(q1s_gate_sections()),
        (CMB_LOAD["from_cmb"], CMB_LOAD["path_restored"], len(CMB), len(q1s_gate_sections()) >= 6,
         "1. The verdict, item by item" in q1s_gate_sections()), ([], True, 1, True, True))
    _fc = cmb_asked()
    _c45 = " ".join([r for r in D68_RULED if r[0] == "M-D68-45"][0][3].split())
    chk("  M-D68-45's cell prints reading 1's figures, asked afresh (five needles)",
        [n for n in _cmb_fig(_fc).values() if n not in _c45], [])
    chk("  CONTROL: the same figures at 1.5 times are not found",
        len([n for n in _cmb_fig(_fc, 1.5).values() if n not in _c45]), 5)
    chk("  CMB_OPEN names %d items with owner files; LEDGER.md prints them after wave 4's and before the pending "
        "rulings; section 8f is in the docstring" % len(CMB_OPEN),
        (len(CMB_OPEN), [r[0] for r in CMB_OPEN if not _os.path.exists(_os.path.join(HERE, r[3]))],
         _md.index("## DOCKET 68 wave 4 -- what stays open") < _md.index("## H-CMB-CORRIDOR reading 1 -- what stays open")
         < _md.index("## Pending M's ruling"), "8f.  THE Q-1s GATE, AND H-CMB-CORRIDOR READING 1" in __doc__),
        (4, [], True, True))
    # ADDED (CMB2-seat, docstring section 8g): readings 2 and 3 and the local clocks.
    chk("CMB READINGS 2 AND 3, LOCAL CLOCKS: medium.py, unobserved.py and localclock.py load from docket68/cmb/ by "
        "path; sys.path restored; no module key the load added is left behind",
        (CMB2_LOAD["from_cmb"], CMB2_LOAD["path_restored"], CMB2_LOAD["keys_left"], sorted(CMB2)),
        ([], True, [], ["localclock", "medium", "unobserved"]))
    _fc2 = cmb2_asked()
    _c54 = " ".join([r for r in D68_RULED if r[0] == "M-D68-54"][0][3].split())
    chk("  M-D68-54's cell prints the three owners' figures, asked afresh (five needles)",
        [n for n in _cmb2_fig(_fc2).values() if n not in _c54], [])
    chk("  CONTROL: the same figures at 1.5 times are not found",
        len([n for n in _cmb2_fig(_fc2, 1.5).values() if n not in _c54]), 5)
    _c53 = " ".join([r for r in D68_RULED if r[0] == "M-D68-53"][0][3].split())
    chk("  M-D68-53's cell prints the local clocks' 0.708 +- 0.014 s per year and the CMB frame's 1.640, asked",
        ("%.3f +- %.3f s per year" % (_fc2["clock_s"], _fc2["clock_sigma"]) in _c53,
         "%.3f" % _fc2["cmb_frame_s"] in _c53, "%.3f" % _fc2["clock_s"], "%.3f" % _fc2["clock_sigma"]),
        (True, True, "0.708", "0.014"))
    chk("  CMB2_OPEN names %d items with owner files; LEDGER.md prints them after reading 1's and before the pending "
        "rulings; section 8g is in the docstring" % len(CMB2_OPEN),
        (len(CMB2_OPEN), [r[0] for r in CMB2_OPEN if not _os.path.exists(_os.path.join(HERE, r[3]))],
         _md.index("## H-CMB-CORRIDOR reading 1 -- what stays open")
         < _md.index("## H-CMB-CORRIDOR readings 2 and 3, and the local clocks -- what stays open")
         < _md.index("## Pending M's ruling"), "8g.  H-CMB-CORRIDOR READINGS 2 AND 3, AND THE LOCAL CLOCKS" in __doc__),
        (6, [], True, True))
    # ADDED (CMB3-seat, docstring section 8h): support.py and bias.py.
    chk("M-SUPPORT'S DYNAMICS AND READING (b)'S PRICE: support.py and bias.py load from docket68/cmb/ by path; "
        "sys.path restored; no module key the load added is left behind",
        (CMB3_LOAD["from_cmb"], CMB3_LOAD["path_restored"], CMB3_LOAD["keys_left"], sorted(CMB3)),
        ([], True, [], ["bias", "support"]))
    _fc3 = cmb3_asked()
    _c55 = " ".join([r for r in D68_RULED if r[0] == "M-D68-55"][0][3].split())
    chk("  M-D68-55's cell prints the two owners' figures, asked afresh (five needles)",
        [n for n in _cmb3_fig(_fc3).values() if n not in _c55], [])
    chk("  CONTROL: the same figures at 1.5 times are not found",
        len([n for n in _cmb3_fig(_fc3, 1.5).values() if n not in _c55]), 5)
    chk("  the toy's record agreement is printed as consistency: the record-free weighting is inside the same "
        "ambiguity, and the no-recombination weight is outside it",
        (_fc3["toy_free"] < _fc3["toy_amb"], _fc3["toy_rec"] < _fc3["toy_amb"], _fc3["toy_norec"] > _fc3["toy_amb"],
         "consistency, not proof" in _c55), (True, True, True, True))
    chk("  CMB3_OPEN names %d items with owner files; LEDGER.md prints them after section 8g's and before the pending "
        "rulings; section 8h is in the docstring" % len(CMB3_OPEN),
        (len(CMB3_OPEN), [r[0] for r in CMB3_OPEN if not _os.path.exists(_os.path.join(HERE, r[3]))],
         _md.index("## H-CMB-CORRIDOR readings 2 and 3, and the local clocks -- what stays open")
         < _md.index("## M-SUPPORT's dynamics and reading (b)'s price -- what stays open")
         < _md.index("## Pending M's ruling"), "8h.  M-SUPPORT'S DYNAMICS AND READING (b)'S PRICE" in __doc__),
        (5, [], True, True))
    chk("EVERY QUOTATION in a DOCKET 68 cell (here, and index3.py's DOCKET 68 rows) is the "
        "tree's words, or declared otherwise: M's thesis and the question included, the "
        "D23 note's quotation exact ('because is already exists everywhere')",
        (d68_quote_faults(), [k for k in ("D68_THESIS", "D68_QUESTION")
                              if k in d68_words_faults()],
         "M's \"because is already exists everywhere\"" in D68_NOTES["D23"]), ([], [], True))
    _pl = dict(_d68_cells())
    _pl["note D23"] = _pl["note D23"].replace(
        "M's \"because is already exists everywhere\"", "M's \"it already exists everywhere\"")
    chk("  CONTROL: the D23 note's quotation as first printed (emended, in double "
        "quotes) is caught", [m for _s, m in d68_quote_faults(cells=_pl)],
        ["it already exists everywhere"])
    _ht = dict(_d68_held_texts())
    _ht["D68_THESIS"] = (D68_THESIS.replace("costs little", "is cheap"), D68_CHARTER_FILE)
    chk("  CONTROL: M's thesis altered by two words is caught",
        d68_words_faults(held=_ht), ["D68_THESIS"])
    _qi = [f if f[0] != "D68-O-SEAT-OPEN-VIA-S5-AND-THE-D25-GATE"
           else f[:5] + (f[5].replace("'from the seat'", "'from the seat itself'"),)
           for f in __import__("index3").FINDINGS if f[0].startswith("D68-")]
    chk("  CONTROL: a word added to M's in index3's row ('from the seat itself') is caught",
        [m for _s, m in d68_quote_faults(rows=_qi)], ["from the seat itself"])
    chk("  every DOCKET 68 ruling is on the board with question, ruling and "
        "unblocks, uncut", ([r[0] for r in D68_RULED if not all(r[1:])],
                            [t for t in _truncated_cells() if t[0] == "ruled"
                             and t[1].startswith("M-D68")]), ([], []))
    # CONVERTED: this check first pinned M-D68-P1 as PENDING (CHARTER.md: asked
    # of M and unanswered).  M had answered before DOCKET 68 opened; the row is
    # now the ruling M-D68-C12, and nothing is pending.
    _c12 = [r for r in D68_RULED if r[0] == "M-D68-C12"]
    _c12c = " ".join(" ".join(_c12[0][3].split()).split()) if _c12 else ""
    _er = _emtension_record()
    chk("M-D68-C12 (first recorded as pending, M-D68-P1) is RULED and on RULED_BY_M: "
        "the question as item 14 records it, M's words verbatim, the owner values "
        "ASKED of emtension and printed, the P1 text kept as history; nothing pending",
        ([p_[0] for p_ in PENDING_RULINGS], len(_c12),
         [r[0] for r in RULED_BY_M].count("M-D68-C12"),
         ('"%s"' % D68_C12_QUESTION) in " ".join(_c12[0][1].split()) if _c12 else None,
         _c12c.startswith("RULED BY M: RECORD IT -- " + d68_words("M-D68-C12")),
         _er,
         all(("%s = %s" % (k, _er[k])) in _c12c for k in
             ("ER_EPR_SOURCE", "ER_EPR_SOURCE_STATUS", "ER_EPR_NONTRAVERSABLE_IS_ASSUMED",
              "ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION", "ENTANGLED_BRIDGE_IS_TRAVERSABLE")),
         "FIRST RECORDED AS PENDING (M-D68-P1)" in _c12c,
         all(" ".join(h.split()) in _c12c for h in D68_P1_AS_FIRST_RECORDED),
         [k for k in d68_words_faults() if "C12" in k]),
        ([], 1, 1, True, True,
         {"ER_EPR_SOURCE": "arXiv:1306.0533v2", "ER_EPR_SOURCE_STATUS": "READ",
          "ER_EPR_NONTRAVERSABLE_IS_ASSUMED": True, "ER_EPR_FOOTNOTE_1 whole": True,
          "ER_EPR_PARTICLE_PAIR_FORM_IS_SPECULATION": True,
          "ENTANGLED_BRIDGE_IS_TRAVERSABLE": False},
         True, True, True, []))
    _ht12 = dict(_d68_held_texts())
    _k12 = "M-D68-C12: the question put, as item 14 records it"
    _ht12[_k12] = (D68_C12_QUESTION.replace("today's", "yesterday's"), D68_RULINGS_FILE)
    chk("  CONTROL: M-D68-C12's question altered by one word is caught against item 14",
        [k for k in d68_words_faults(held=_ht12) if "C12" in k], [_k12])
    with contextlib.redirect_stdout(io.StringIO()):
        import emtension as _em
    _keep = _em.ER_EPR_SOURCE_STATUS
    _em.ER_EPR_SOURCE_STATUS = "CITED"
    try:
        _er2 = _emtension_record()["ER_EPR_SOURCE_STATUS"]
    finally:
        _em.ER_EPR_SOURCE_STATUS = _keep
    chk("  CONTROL: the owner values are asked of emtension, not typed (a scratch "
        "status reaches the record)", _er2, "CITED")
    _m12 = paper_d68_marker(D68_M_WORDS["M-D68-12"][0])
    _m13 = paper_d68_marker(D68_M_WORDS["M-D68-13"][0])
    _r1213 = {r[0]: [" ".join(c.split()) for c in r] for r in D68_RULED
              if r[0] in ("M-D68-12", "M-D68-13")}
    chk("M-D68-12 and M-D68-13 (items 12-13, M's rulings on the paper) are seated: the "
        "question as each item records it, M's words verbatim, and what was applied -- "
        "the paper's marked line READ back from M's words in its DOCKET 68 head, the "
        "heads' words exactly the held words",
        (sorted(_r1213), [r[0] for r in RULED_BY_M].count("M-D68-12"),
         [r[0] for r in RULED_BY_M].count("M-D68-13"),
         [('"%s"' % D68_PAPER_QUESTIONS[k]) in _r1213[k][1] for k in sorted(_r1213)],
         [_r1213[k][3].startswith("RULED BY M: %s -- %s" % (o, d68_words(k)))
          for k, o in (("M-D68-12", "CORRECT IT"), ("M-D68-13", "SCOPE IT"))],
         _m12[0] is not None and _m13[0] is not None,
         ("paper/CLAIMS.md:%s carries %s" % _m12) in _r1213["M-D68-12"][3],
         ("paper/CLAIMS.md:%s carries %s" % _m13) in _r1213["M-D68-13"][3],
         D68_PAPER_FIRST_WORDING in _m12[1], "linear quantum mechanics" in _m13[1],
         sorted(paper_d68_words()), sorted(paper_docket_markers().get(68, []))
         == sorted((_m, True) for _m in (_m12[0], _m13[0]))),
        (["M-D68-12", "M-D68-13"], 1, 1, [True, True], [True, True], True, True, True,
         True, True, sorted([D68_M_WORDS["M-D68-12"][0], D68_M_WORDS["M-D68-13"][0]]),
         True))
    _pl68 = [l.replace('M\'s "Scope it (Recommended)", DOCKET 68:', "M's ruling, DOCKET 68:")
             for l in _paper_lines()]
    chk("  CONTROL: a private copy of the paper whose H62d marker head drops M's words is "
        "not READ as carrying M-D68-13's marker",
        (paper_d68_marker(D68_M_WORDS["M-D68-13"][0], _pl68)[0], paper_d68_words(_pl68)),
        (None, [D68_M_WORDS["M-D68-12"][0]]))
    _r1516 = dict((r[0], [" ".join(c.split()) for c in r]) for r in D68_RULED
                  if r[0] in ("M-D68-15", "M-D68-16"))
    chk("M-D68-15 and M-D68-16 (items 15-16, the retrieval route) are seated after "
        "M-D68-13: M's words verbatim; 15 marked SUPERSEDED by 16 and kept; 16's applied "
        "routes asked of the owners, every one naming alphaXiv or Firecrawl",
        ([r[0] for r in D68_RULED].index("M-D68-15")
         == [r[0] for r in D68_RULED].index("M-D68-13") + 1,
         [k for k in d68_words_faults() if k in ("M-D68-15", "M-D68-16")],
         _r1516["M-D68-15"][3].startswith(
             "RULED BY M: CORPUS INSTRUMENTS -- SUPERSEDED BY M-D68-16 -- "
             + d68_words("M-D68-15")),
         _r1516["M-D68-16"][3].startswith(
             "RULED BY M: WEB-RETRIEVAL INSTRUMENTS, OPEN CONTENT ONLY -- "
             + d68_words("M-D68-16")),
         " ".join(d68_w2_routes().split()) in _r1516["M-D68-16"][3],
         d68_w2_routes().endswith("routes naming neither instrument: none")),
        (True, [], True, True, True, True))
    _sk = dict(seat.KERVELLA_2017)
    seat.KERVELLA_2017["route"] = "READ through a library copy"
    try:
        _rt = d68_w2_routes()
    finally:
        seat.KERVELLA_2017.clear()
        seat.KERVELLA_2017.update(_sk)
    chk("  CONTROL: a source whose recorded route names neither instrument is listed, "
        "not dropped (a scratch route on seat.KERVELLA_2017)",
        _rt.endswith("['READ through a library copy']"), True)
    chk("M-D68-9: the paper brief stays in the tree; M-D68-4: index3.py's held rows "
        "are named in the ruling, asked",
        (d68_paper_brief_present(),
         all(k in [r for r in D68_RULED if r[0] == "M-D68-4"][0][3]
             for k in _d68_index3_held())), (True, True))
    chk("index3.py's DOCKET 68 rows type their owners' CURRENT values (each needle "
        "asked of combine, frame, signed, measure, stockgate, massform)",
        d68_index3_faults(), [])
    import index3 as _i3
    _planted = [f if f[0] != "D68-ONE-MEMBER-REMOVAL-AND-IT-IS-CONDITIONAL"
                else f[:5] + (f[5].replace("0.50153", "0.50200"),) for f in _i3.FINDINGS]
    chk("  CONTROL: a drifted figure planted in index3's row (0.50153 -> 0.50200) is "
        "caught", d68_index3_faults(_planted),
        [("D68-ONE-MEMBER-REMOVAL-AND-IT-IS-CONDITIONAL", "the midpoint first read")])
    _pl3 = [f if f[0] != "D68-O-SEAT-OPEN-VIA-S5-AND-THE-D25-GATE"
            else f[:5] + (f[5].replace("(C3, under H-C3)", "(C3)"),) for f in _i3.FINDINGS]
    chk("  CONTROL: S13's named hypothesis dropped from index3's O-SEAT row ('(C3)' for "
        "'(C3, under H-C3)', the row as first seated) is caught",
        d68_index3_faults(_pl3),
        [("D68-O-SEAT-OPEN-VIA-S5-AND-THE-D25-GATE",
          "S13's named hypothesis, as combine's B-S13 states it")])
    chk("  index3's signed-entropy row is gone (Q-1 and Q-1s carried on O9 only), and "
        "no needle asks for it",
        ([f[0] for f in _i3.FINDINGS if "SIGNED-ENTROPY" in f[0]],
         [k for k in d68_index3_needles() if "SIGNED-ENTROPY" in k]), ([], []))
    chk("the docstring states section 7 and names its limitations",
        all(x in __doc__ for x in ("7.  DOCKET 68, WAVE 1, AS M RULED IT",
                                   "7b.  DOCKET 68, WAVE 2, AS SEATED",
                                   "H-LEDGER-ASKS-REPRESENTATIVES", "H-LEDGER-DEPS",
                                   "CARRIED, NOT RULED", "WHAT IS CHECKED",
                                   "are cited from their owners, not checked")), True)

    print("\n4f. DOCKET 66, WAVE 1 (docstring section 8): ASKED OF docket66/")
    import os as _os66       # section 6 binds 'os' locally; this section must not use it
    chk("combine's vocabulary is restored after every DOCKET 66 ask (combine66's "
        "E-EXTEND is in-process only): combine.LIT_NAMES is combine's own and "
        "combine66 reports it unextended",
        (list(combine.LIT_NAMES) == combine66._ORIG["LIT_NAMES"],
         combine66._STATE["extended"]), (True, False))
    with combine66.vocabulary(True):
        _ext = (len(combine.LIT_NAMES), combine66._STATE["extended"])
    chk("  CONTROL: inside combine66.vocabulary(True) the vocabulary IS extended (so "
        "the restore check can fail)",
        (_ext[0] > len(combine66._ORIG["LIT_NAMES"]), _ext[1]), (True, True))
    _f66 = _d66_ask()
    chk("  every DOCKET 66 verdict this board prints reproduces on a FRESH ask of "
        "combine66.D66Screen (both cells and the readings)",
        [(c, k) for c in ("main", "au", "readings") for k in _f66[c]
         if (_f66[c][k]["consistent"], _f66[c][k].get("per"), _f66[c][k].get("seat"))
         != (_D66[c][k]["consistent"], _D66[c][k].get("per"), _D66[c][k].get("seat"))], [])
    chk("MEMBER-ATTRIBUTED FIRST: no D66 literal is load-bearing in any removal or "
        "non-binding in any variant asked (combine66.d66_attributed), and B-combine66.md "
        "(READ) reports 0 in its full screen at both cells",
        (d66_load_bearing(), D66_CENSUS["load-bearing"][0], D66_CENSUS["load-bearing"][2]),
        ([], "0", "0"))
    with contextlib.redirect_stdout(io.StringIO()), combine66.vocabulary(True):
        _planted = combine66.D66Screen(mutate=("defb-asserted",)).screen({"DSTR"})
    chk("  CONTROL: combine66's planted D66 removal (defb-asserted: a string seat "
        "supplies the baryons) IS credited to DSTR (the load-bearing test can fail)",
        combine66.d66_attributed(_planted), ["O-SEAT"])
    chk("  R-LIT sits in an O-BITS support only by entailing W2 -- in a support, "
        "load-bearing nowhere -- at both cells; alone it is inconsistent (its clash "
        "core holds B66-ARR, B66-LIN and C-QLIT)",
        (d66_in_support_only(), D66_ASKED["H-QET-EXOTIC: R-LIT (QLIT)"]["consistent"],
         all(x in d66_core(D66_ASKED["H-QET-EXOTIC: R-LIT (QLIT)"])
             for x in ("B66-ARR", "B66-LIN", "C-QLIT"))),
        (["R-LIT with W2 x F1", "1 AU: R-LIT with W2 x F1"], False, True))
    chk("  the only member removal stays D68's: with a string seat, O-BITS REMOVED-IF "
        "by W2 x F1 (credited to members, DSTR in no support), its supports those of "
        "combine.py's own W2 x F1",
        (D66_ASKED["DSTR with W2 x F1"]["per"]["O-BITS"]["verdict"],
         D66_ASKED["DSTR with W2 x F1"]["per"]["O-BITS"]["attribution"],
         any("DSTR" in sp["members"] for sp in D66_ASKED["DSTR with W2 x F1"]["per"]["O-BITS"]["supports"]),
         [(sp["members"], sp["named"]) for sp in D66_ASKED["DSTR with W2 x F1"]["per"]["O-BITS"]["supports"]]
         == [(sp["members"], sp["named"]) for sp in D68_ASKED["W2 x F1"]["per"]["O-BITS"]["supports"]]),
        ("REMOVED-IF", "member", False, True))
    chk("  the extended screen with no D66 literal is combine.py's board alone on every "
        "obstruction (conservative extension, one variant here; B-combine66.md READ: "
        "its full run, 0 differ)",
        (d66_d68_board_agrees(), D66_CENSUS["conservative"][1]), ([], "0"))
    _cmp = [(o, d68_verdict(D66_ASKED["H-DEFECT-SEAT: static string seat (DSTR)"]["per"][o]))
            for o in D68_ASKED["the board alone"]["per"]
            if d68_verdict(D66_ASKED["H-DEFECT-SEAT: static string seat (DSTR)"]["per"][o])
            != d68_verdict(D68_ASKED["the board alone"]["per"][o])]
    chk("  CONTROL: the same comparison against a string seat differs (O-SEAT gains "
        "N_DEFB), so the comparator can fail", [o for o, _v in _cmp], ["O-SEAT"])
    chk("WHAT THE D66 READINGS ADD IS OPEN PATHWAYS, NONE A REMOVAL: against its D68 "
        "context (combine.py's own variant, D68_ASKED), no asked D66 variant lifts an "
        "obstruction its context does not, and every pathway it adds is combine66's "
        "(D66_OPEN)", (d66_added_lifts(), d66_added_foreign_pathways()), ([], []))
    _fake66 = dict(D66_ASKED["H-DEFECT-SEAT: static string seat (DSTR)"])
    _fake66["per"] = dict(_fake66["per"], **{"O-SEAT": {"verdict": "REMOVED", "supports": [
        {"members": ["DSTR"], "absent": [], "named": []}]}})
    with _scratch("D66_ASKED", dict(D66_ASKED, **{"H-DEFECT-SEAT: static string seat (DSTR)": _fake66})):
        _al = d66_added_lifts()
    chk("  CONTROL: a string seat that removed O-SEAT would be caught as an added lift",
        _al, [("H-DEFECT-SEAT: static string seat (DSTR)", ["O-SEAT"])])
    chk("  per reading, the pathway each opens is its owner's (combine66.PATHWAY_OWNER): "
        "O-SEAT N_DEFB for the four defect seats; O-HOLD N_NEGT (DTHR), N_PINCH (TBHOLO, "
        "TBTSH), N_GJWPAY (TBTEL), N_QETHAD alone (QET); O-MAKE-TOPO N_WNCC for every D66 "
        "throat",
        ([D66_ASKED[k]["per"]["O-SEAT"].get("via") for k in D66_DEFECT_SEATS],
         [D66_ASKED[k]["per"]["O-HOLD"].get("via") for k in (
             "H-DEFECT-SEAT: string-supported throat (DTHR)", "H-THROAT-BITS: R-HOLO (TBHOLO)",
             "H-THROAT-BITS: R-THINSHELL (TBTSH)", "H-THROAT-BITS: R-TELEPORT (TBTEL)",
             "H-QET-EXOTIC: R-QET (QET)")],
         [D66_ASKED[k]["per"]["O-MAKE-TOPO"].get("via") for k in (
             "H-DEFECT-SEAT: string-supported throat (DTHR)", "H-THROAT-BITS: R-HOLO (TBHOLO)",
             "H-THROAT-BITS: R-THINSHELL (TBTSH)", "H-THROAT-BITS: R-TELEPORT (TBTEL)")]),
        ([["N_S5", "N_DEFB"]] * 4,
         [["N_NEGT"], ["N_PINCH"], ["N_PINCH"], ["N_GJWPAY"], ["N_QETHAD"]],
         [["N_WNCC"]] * 4))
    chk("  INTERFERENCE: beside ITB a D66 throat makes {N_QTOPO} a premise clash and "
        "ITB's two non-bindings fall (DTHR with ITB: O-MAKE-TOPO and O-HOLD OPEN, not "
        "NOT-BOUND-IF); R-ITB keeps ITB's own",
        (D66_ASKED["DTHR with ITB"]["premise_clash_named"],
         [D66_ASKED["DTHR with ITB"]["per"][o]["verdict"] for o in ("O-MAKE-TOPO", "O-HOLD")],
         D66_ASKED["H-THROAT-BITS: R-ITB with ITB (TBITB)"]["per"]["O-HOLD"]["verdict"]),
        ([("N_QTOPO",)], ["OPEN", "OPEN"], "NOT-BOUND-IF"))
    chk("  DEFEASIBLE ONLY THROUGH A HELD STRING-SUPPORTED THROAT: of the variants "
        "asked, removals or the seat are defeasible only where DTHR is present",
        sorted(k for k, r in D66_ASKED.items() if r["consistent"]
               and (r["defeasible"] or r["seat"].get("defeasible"))
               and "DTHR" not in r["present"]), [])
    chk("  THE SEAT CONDITION M-S1A-P3 (i): VIOLATED in no variant asked; the four "
        "defect seats SATISFIED (the wall under H-VIS-MINKOWSKI), and B-combine66.md "
        "(READ) reports VIOLATED in no consistent variant",
        ([k for k, r in list(D66_ASKED.items()) + list(D66_ASKED_AU.items())
          if r["consistent"] and r["seat"]["verdict"] == "VIOLATED"],
         [D66_ASKED[k]["seat"]["verdict"] for k in D66_DEFECT_SEATS],
         D66_CENSUS["seat violated"]), ([], ["SATISFIED"] * 4, ()))
    # RE-PINNED ON M-D68-28 (R-seat): singok-board and combine.py now AGREE on
    # the board alone (OPEN via N_WNCC); the finding first recorded for the D68
    # board (combine.py LEFT there) is D68 wave 2's, re-asked of combine's
    # history encoding d68w2-topo, which must still give LEFT.
    chk("  READINGS AND HISTORY, asked: H-SEAT-ROUTES leaves O-SEAT LEFT; singok-board "
        "gives the board alone's O-MAKE-TOPO OPEN via N_WNCC and combine.py now gives the "
        "same (M-D68-28), where D68 wave 2's encoding (d68w2-topo) gives LEFT -- the "
        "finding first recorded for the D68 board; D66 wave 1's encodings "
        "reproduce its words (singok-a2: DTHR's O-MAKE-TOPO LEFT; qet-board-paths: QET's "
        "O-HOLD via N_XI, N_QEIC, N_QETHAD)",
        (D66_READ_ASKED["H-SEAT-ROUTES on DSTR"]["per"]["O-SEAT"]["verdict"],
         (D66_READ_ASKED["singok-board on the board alone"]["per"]["O-MAKE-TOPO"]["verdict"],
          D66_READ_ASKED["singok-board on the board alone"]["per"]["O-MAKE-TOPO"].get("via"),
          D68_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]["verdict"],
          D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]["verdict"]),
         D66_READ_ASKED["singok-a2 on DTHR (D66 wave 1's encoding)"]["per"]["O-MAKE-TOPO"]["verdict"],
         D66_READ_ASKED["qet-board-paths on QET (D66 wave 1's encoding)"]["per"]["O-HOLD"].get("via")),
        ("LEFT", ("OPEN", ["N_WNCC"], "OPEN", "LEFT"), "LEFT", ["N_XI", "N_QEIC", "N_QETHAD"]))
    chk("O9's closing over DOCKET 66's variants, asked: O-BITS REMOVED outright in none",
        (d66_o_bits_removed_outright(),
         sorted(set(r["per"]["O-BITS"]["verdict"] for r in list(D66_ASKED.values())
                    + list(D66_ASKED_AU.values()) if r["consistent"]))),
        ([], ["LEFT", "REMOVED-IF"]))
    _row9 = [r for r in OPEN_ROWS if r[0] == "O9"][0]
    chk("  and O9's DOCKET 66 part prints every verdict it names as asked",
        [x for x in (d66_asked("DSTR with W2 x F1", "O-BITS"),
                     d66_asked("DSTR with W2 x F1", "O-BITS", au=True),
                     d66_asked("QET with R-QUANTUM (RQ)", "O-HOLD"),
                     d66_asked("DTHR with ITB", "O-MAKE-TOPO"),
                     d66_asked("singok-board on the board alone", "O-MAKE-TOPO", reading=True),
                     d66_seat("H-DEFECT-SEAT: string-supported throat (DTHR)"),
                     d66_group(D66_DEFECT_SEATS, "O-SEAT"))
         if x not in _row9[1]], [])
    chk("  B-combine66.md READ: the figures this board cites from combine66's runs "
        "(variants, load-bearing census, selftest, controls, conservative extension)",
        (D66_CENSUS["variants"], D66_CENSUS["load-bearing"], D66_CENSUS["selftest"],
         D66_CENSUS["controls"], D66_CENSUS["conservative"]),
        (("3,496", "32", "1,748", "16"), ("0", "2,492", "0", "1,332"), ("68", "68"),
         ("24",), ("8,192", "0")))
    import tempfile
    _tdir = tempfile.mkdtemp()
    _tb = _os66.path.join(_tdir, "B.md")
    with open(D66_B_FILE, encoding="utf-8") as _fh, open(_tb, "w", encoding="utf-8") as _fo:
        _fo.write(_fh.read().replace("The count is 0 in", "The count was 0 in"))
    try:
        d66_census_read(_tb)
        _raised = False
    except ValueError:
        _raised = True
    _os66.unlink(_tb)
    _os66.rmdir(_tdir)
    chk("  CONTROL: a B-combine66.md that no longer states the load-bearing census "
        "makes the seat refuse (raises)", _raised, True)
    _nr = dict((r[0], r) for r in SUPPLY)
    chk("the DOCKET 66 notes on S5 and S13 are carried AFTER each DOCKET 68 note, and "
        "NO status moved (S5 and S13 OPEN); S13 still carries 'It forms no baryons (C3' "
        "(combine.board_flags reads it)",
        [(k, _nr[k][2], "DOCKET 66 (a note; no status change)" in _nr[k][4],
          _nr[k][4].index("DOCKET 68 (a note") < _nr[k][4].index("DOCKET 66 (a note"))
         for k in ("S5", "S13")] + ["It forms no baryons (C3" in _nr["S13"][4]],
        [("S5", OPEN, True, True), ("S13", OPEN, True, True), True])
    chk("  the defect-core link is massform's, asked as combine66 asks it: TEMPLATE "
        "REFUSED on C1 alone, STANDS with C1's link, no new baryon number, and the "
        "held-seat route forms none",
        (_d66_massform_link()["TEMPLATE"], _d66_massform_link()["TEMPLATE, C1 holding"],
         "no new baryon number" in _d66_massform_link()["C3 reason"],
         _d66_massform_link()["forms baryons"]), ("REFUSED", "STANDS", True, False))
    _fig2 = _d66_figures(spec={"S-1": "other", "S-2": "other", "S-3": "other", "Rec": "other"})
    chk("  qet.grades' fields read here do not use specthm's verdicts (re-asked with a "
        "second placeholder: identical)",
        [k for k in ("R-QET own content", "R-LIT own content", "R-QET O-HOLD head",
                     "R-QET O-SEAT head") if _fig2[k] != D66_FIG[k]], [])
    chk("  the owners' QET and MMP facts the notes print: arrival alone |E| < 1e-12; "
        "supremum E_B/E_A below 1/4; the injection 4 x the rest energy; MMP's binding "
        "equals the payload only below l_P",
        (abs(D66_FIG["QET arrival alone"]) < 1e-12, D66_FIG["QET sup E_B/E_A"] < 0.25,
         abs(D66_FIG["QET payload rest J, injection J"][1]
             / D66_FIG["QET payload rest J, injection J"][0] - 4.0) < 1e-12,
         D66_FIG["MMP binding = payload at r_e (max), l_P"][0]
         < D66_FIG["MMP binding = payload at r_e (max), l_P"][1]),
        (True, True, True, True))
    chk("the literature named to M is READ by qet.py, item by item, from its own "
        "sources; M_D65_1_LITERATURE is exactly those items",
        ([i for i, e in d66_qet_literature() if e is None],
         "; ".join(M_D65_1_LITERATURE_ITEMS) == M_D65_1_LITERATURE), ([], True))
    with _scratch("M_D65_1_LITERATURE_ITEMS", M_D65_1_LITERATURE_ITEMS + ("Hotta 2009",)):
        _lit = d66_qet_literature()
    chk("  CONTROL: an item qet.py heads no entry for ('Hotta 2009') reads None",
        _lit[-1], ("Hotta 2009", None))
    chk("the DOCKET 66 charter's quotations of M are held verbatim in the ledger's "
        "constants (M-S1A-P3, M-D65-1, D68_M_WORDS), each one named",
        d66_charter_quote_faults(), [])
    with open(D66_CHARTER_FILE, encoding="utf-8") as _fh:
        _ch = _fh.read()
    chk("  CONTROL: the charter with M's 'Fold into D66' emended, and with an "
        "unattributed quotation added, is caught each time",
        [len(d66_charter_quote_faults(c_)) > 0 for c_ in (
            " ".join(_ch.split()).replace('"Fold into D66"', '"Fold into DOCKET 66"'),
            _ch + '\nM said: "seat it now".\n')], [True, True])
    chk("every quotation in a DOCKET 66 cell is the tree's words (M's words held, or "
        "docket66/'s own files)", d66_quote_faults(), [])
    chk("  CONTROL: a quotation docket66/ never wrote, planted in a DOCKET 66 cell, is caught",
        d66_quote_faults({"planted": "A1 says 'a defect supplies the seat' here"}),
        [("planted", "a defect supplies the seat")])
    chk("index3.py seats no row citing docket66/ (H-NO-D66-ROW: DOCKET 66's answer reads "
        "(0, 0, 0); its priced requirements stay on O9 and S5's note, pending M)",
        d66_index3_faults(), [])
    chk("  CONTROL: a planted index3 row citing docket66/ is caught",
        d66_index3_faults([("D66-PLANTED", 0, 0, 1, "docket66/throatbits.py", "x")]),
        [("D66-PLANTED", "cites docket66/throatbits.py")])
    _tq = d66_turn_question()
    # KEPT AS HISTORY (R-seat): M has ruled the TURN question (M-D68-27, "Any
    # crossing"); the question stays in O9's DOCKET 66 answer and in M-D68-27's
    # row as FIRST RECORDED, and this check still asks its values.
    chk("the TURN question for M (RULED since: M-D68-27) is kept in O9's DOCKET 66 answer as "
        "first carried (never on PENDING_RULINGS, which specthm.py pins empty), its values "
        "asked of defects.py: both TURN readings "
        "named in defects.HYPOTHESES, the global monopole's Jacobi zero at the axis "
        "recrossing (to 1e-6), the gauge monopole's S-1 conditions holding, and A1's clause "
        "that only the string is crossing-only",
        (all(" ".join(c_.split()) in " ".join(D66_O9_ANSWER.split()) for c_ in _tq),
         PENDING_RULINGS,
         all(h in defects.HYPOTHESES for h in ("H-TURN-CONJUGATE", "H-TURN-CROSSING")),
         abs(D66_FIG["global monopole Jacobi zero / axis recrossing"] - 1) < 1e-6,
         D66_FIG["gauge monopole lens"]["S-1 conditions hold"]),
        (True, [], True, True, True))
    # ----- M's DOCKET 66 rulings (docstring section 8b), seated by R-seat -----
    import os as _osr        # section 6 binds 'os' locally; this block must not use it
    _r66 = dict((r[0], [" ".join(c.split()) for c in r]) for r in D68_RULED
                if r[0] in ("M-D68-26", "M-D68-27", "M-D68-28"))
    _rf = _d68_norm(open(D68_RULINGS_FILE, encoding="utf-8").read())
    chk("M's DOCKET 66 rulings (items 26-28) are seated after M-D68-C12, each once: M's words "
        "verbatim in the rulings file under its 'DOCKET 66 rulings' heading, the question and "
        "the file's own applied sentence as the file records them, the ruling cell opening "
        "with the option taken and M's words",
        # RE-PINNED (W3S1B-seat): first pinned as D68_RULED's LAST three; the
        # wave-3 and Step 1b rulings now follow them, so the three are pinned
        # as the ones directly after M-D68-C12, as the label says.
        ([r[0] for r in D68_RULED][[r[0] for r in D68_RULED].index("M-D68-C12") + 1:][:3],
         [[r[0] for r in RULED_BY_M].count(k) for k in sorted(_r66)],
         [k for k in d68_words_faults() if k.startswith("M-D68-2") or "item 2" in k],
         _rf.index("DOCKET 66 rulings (2026-10-04), M's answers verbatim")
         < min(_rf.index(D68_M_WORDS[k][0]) if k != "M-D68-26"
               else _rf.rindex(D68_M_WORDS[k][0]) for k in sorted(_r66)),
         [('"%s"' % D66_RULING_QUESTIONS[k]) in _r66[k][1] for k in sorted(_r66)],
         [('"%s"' % D66_RULING_CARRIED[k]) in _r66[k][3] for k in sorted(_r66)],
         [_r66[k][3].startswith("RULED BY M: %s -- %s" % (o, d68_words(k))) for k, o in (
             ("M-D68-26", "CORRECT IT"), ("M-D68-27", "ANY CROSSING: H-TURN-CROSSING"),
             ("M-D68-28", "RE-GRADE D68"))]),
        (["M-D68-26", "M-D68-27", "M-D68-28"], [1, 1, 1], [], True, [True] * 3, [True] * 3,
         [True] * 3))
    _w66 = dict(D68_M_WORDS)
    _w66["M-D68-27"] = ("Any crossing of light paths", _w66["M-D68-27"][1])
    with _scratch("D68_M_WORDS", _w66):
        _wf66 = d68_words_faults()
    chk("  CONTROL: M's 'Any crossing' lengthened by the question's words is caught",
        [k for k in _wf66 if k == "M-D68-27"], ["M-D68-27"])
    _mk26 = paper_d66_marker(D68_M_WORDS["M-D68-26"][0])
    _nums = lambda t: re.findall(r"\d+(?:\.\d+)?e[-\u2212]?\d+", t)
    chk("M-D68-26: what was applied is the paper's marked line, READ back from M's words in "
        "its DOCKET 66 head (never typed); the line prints defects.py's Gott figures (gamma "
        "at the Planck Nambu-Goto and Abelian-Higgs bounds, and the bounds); the paper's own "
        "first wording carries item 26's numbers, in its typography",
        (_mk26[0] is not None, ("paper/CLAIMS.md:%s carries %s" % _mk26) in _r66["M-D68-26"][3],
         [f for f, ok_ in d66_paper_gott_figures() if not ok_], len(d66_paper_gott_figures()),
         paper_d66_first_wording(D68_M_WORDS["M-D68-26"][0])
         == D66_PAPER_FIRST_WORDING_AS_PRINTED,
         [x.replace("\u2212", "-") for x in _nums(D66_PAPER_FIRST_WORDING_AS_PRINTED)]
         == _nums(D66_PAPER_FIRST_WORDING)),
        (True, True, [], 4, True, True))
    _pl26 = [l.replace("1.5e\u22127", "1.6e\u22127") for l in _paper_lines()]
    chk("  CONTROL: a private copy of the paper whose line prints another bound is caught "
        "(the figure check can fail)", [f for f, ok_ in d66_paper_gott_figures(_pl26) if not ok_],
        [_paper_e(D66_GOTT["NG"][0])])
    _st = D66_TURN["string"]
    _lit = specthm_seat_class_literals()
    import tempfile as _tf66
    with open(_osr.path.join(HERE, "specthm.py"), encoding="utf-8") as _fh:
        _sth = _fh.read()
    _tdir66 = _tf66.mkdtemp()
    _tsp = _osr.path.join(_tdir66, "specthm.py")
    with open(_tsp, "w", encoding="utf-8") as _fh:
        _fh.write(_sth.replace('"lits": {"wl": False, "ball": False}',
                               '"lits": {"wl": False, "ball": False, "turn": True}'))
    _lit_c = specthm_seat_class_literals(_tsp)
    _osr.unlink(_tsp)
    _osr.rmdir(_tdir66)
    chk("M-D68-27: H-TURN-CROSSING adopted, H-TURN-CONJUGATE kept on record, M's words in "
        "defects.TURN_RULING; the straight string TURNs at a finite computed range under the "
        "ruling and not under the alternative (no conjugate point); the line-intersection "
        "cross-check agrees (a consistency check on the same geometry, not an independent "
        "derivation); spec.py carries the ruling's note; specthm's seat classes are defined by "
        "wl and ball only (READ), so no class verdict moves; the cell prints them as asked",
        (D66_TURN["ruling"]["M"] == D68_M_WORDS["M-D68-27"][0],
         (D66_TURN["ruling"]["adopted"], D66_TURN["ruling"]["alternative on record"]),
         (_st["H-TURN-CROSSING"][0], _st["H-TURN-CONJUGATE"][0], _st["conjugate point"]),
         D66_TURN["L AU"] > 0 and math.isfinite(D66_TURN["L AU"]),
         abs(D66_TURN["L AU (line intersection)"] / D66_TURN["L AU"] - 1) < 1e-9,
         spec_turn_note() is not None, sorted(_lit), sorted(set(x for v in _lit.values() for x in v)),
         ("%.0f AU" % D66_TURN["L AU"]) in _r66["M-D68-27"][3],
         " ".join(d66_turn_question()[0].split()) in _r66["M-D68-27"][1]),
        (True, ("H-TURN-CROSSING", "H-TURN-CONJUGATE"), ("TURN", "NO TURN", None), True, True,
         True, ["S-1", "S-2", "S-3"], ["ball", "wl"], True, True))
    chk("  CONTROL: a 'turn' literal planted in a private copy of specthm.py's S-3 class is "
        "READ (the class-literal check can fail)", _lit_c.get("S-3"), ["ball", "turn", "wl"])
    _g0 = defects.string_turn(0.0, 1.0)
    chk("  CONTROL: with no deficit (G mu = 0) the string does not TURN under either reading "
        "(the verdict is carried by the deficit, not by the reading)",
        (_g0["H-TURN-CROSSING"][0], _g0["H-TURN-CONJUGATE"][0]), ("NO TURN", "NO TURN"))
    _k28 = ("the board alone", "R-QUANTUM alone (RQ)", "H-IT as Jacobson emergent gravity (ITJ)",
            "ITB with R-QUANTUM (ITB+RQ)")
    chk("M-D68-28: combine.py's O-MAKE-TOPO reads OPEN via exactly N_WNCC on the board alone, "
        "RQ, ITJ and ITB+RQ, and under ITB its removal gains N_WNCC -- never removed; D68 wave "
        "2's encoding (d68w2-topo) gives LEFT there; the census is READ from B-combine.md "
        "(3,840 of 5,760 and 960 of 1,152, the same 20 contexts) and B-combine66.md (174 moved "
        "back, 20 context-only; singok-board now 0); the cell prints every value as asked",
        ([D68_ASKED[k]["per"]["O-MAKE-TOPO"] for k in _k28],
         [D68_TOPO_W2_ASKED[k]["per"]["O-MAKE-TOPO"]["verdict"] for k in _k28],
         [k for k in D68_ASKED if "REMOVED" in D68_ASKED[k]["per"]["O-MAKE-TOPO"]["verdict"]],
         D68_TOPO_CENSUS["moved"][:4], D68_TOPO_CENSUS["contexts"][:2],
         D66_TOPO_READ["d68w2-topo"], D66_TOPO_READ["singok-board"],
         [x for x in [d68_asked(k, "O-MAKE-TOPO") for k in _k28]
          + [d68_verdict(D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"])]
          if x not in _r66["M-D68-28"][3]]),
        ([{"verdict": "OPEN", "via": ["N_WNCC"]}] * 4, ["LEFT"] * 4, [],
         ("3,840", "5,760", "960", "1,152"), ("20", "32"), ("174", "20"), ("0",), []))
    import tempfile as _tf68
    _tdir68 = _tf68.mkdtemp()
    _tb68 = _osr.path.join(_tdir68, "B.md")
    with open(D68_B_FILE, encoding="utf-8") as _fh, open(_tb68, "w", encoding="utf-8") as _fo:
        _fo.write(_fh.read().replace("(board alone included)", "(board alone excluded)"))
    try:
        d68_topo_census_read(_tb68)
        _raised68 = False
    except ValueError:
        _raised68 = True
    _osr.unlink(_tb68)
    _osr.rmdir(_tdir68)
    chk("  CONTROL: a B-combine.md that no longer states the re-grade census makes the seat "
        "refuse (raises)", _raised68, True)
    _ans = " ".join(O9_ANSWERED_BY.split())
    _ans66 = " ".join(D66_O9_ANSWER.split())
    _part66 = " ".join(D66_O9_PART.split())
    chk("O9's answers carry M's DOCKET 66 rulings, asked: DOCKET 68's names the re-graded "
        "O-MAKE-TOPO (board alone, RQ, ITJ, ITB) and its history verdict, and the adopted TURN "
        "reading; DOCKET 66's says the TURN reading is RULED (string L as asked) with the "
        "question kept after it; DOCKET 66's part says the D68 board is re-graded, keeping "
        "'RECORDED FOR THE D68 BOARD, NOT REPAIRED' after it as first said",
        ([x for x in [d68_asked(k, "O-MAKE-TOPO") for k in (
            "the board alone", "R-QUANTUM alone (RQ)", "H-IT as Jacobson emergent gravity (ITJ)",
            "H-IT as an information layer (ITB)")] if x not in _ans],
         "d68w2-topo (the board alone %s, asked)" % d68_verdict(
             D68_TOPO_W2_ASKED["the board alone"]["per"]["O-MAKE-TOPO"]) in _ans,
         d68_words("M-D68-27") in _ans and D66_TURN["ruling"]["adopted"] in _ans,
         ("THE TURN READING, RULED BY M (M-D68-27, %s)" % d68_words("M-D68-27")) in _ans66,
         ("L = %.0f AU" % D66_TURN["L AU"]) in _ans66,
         _ans66.index("THE TURN READING, RULED BY M") < _ans66.index(
             "FIRST CARRIED HERE AS A QUESTION FOR M"),
         _part66.index("THE D68 BOARD, RE-GRADED ON M'S RULING (M-D68-28")
         < _part66.index("RECORDED FOR THE D68 BOARD, NOT REPAIRED")),
        ([], True, True, True, True, True, True))
    chk("the charter's 'with M's throat-compression mechanism' is the ledger's words: the "
        "charter attributes it to the ledger (READ), it is still checked verbatim, and it is "
        "not among M's quotations (d66_charter_m_quotes)",
        (d66_charter_attribution_faults(),
         [k for k in D66_CHARTER_LEDGER_WORDS if k in d66_charter_m_quotes()],
         all(k in _d66_charter_holders() for k in D66_CHARTER_LEDGER_WORDS)),
        ([], [], True))
    with open(D66_CHARTER_FILE, encoding="utf-8") as _fh:
        _ch66 = _fh.read()
    chk("  CONTROL: the charter without its attribution is caught, and a DOCKET 66 cell "
        "double-quoting the ledger's words as M's is caught",
        (d66_charter_attribution_faults(" ".join(_ch66.split()).replace(
            D66_CHARTER_LEDGER_ATTRIBUTION, "is M's")),
         d66_quote_faults({"planted": 'M said "with M\'s throat-compression mechanism" here'})),
        (list(D66_CHARTER_LEDGER_WORDS),
         [("planted", "with M's throat-compression mechanism")]))
    _m10 = [r for r in D68_RULED if r[0] == "M-D68-10"][0]
    chk("M-D68-10 says step (4), DOCKET 66, is RUN and seated and step (3)'s comments "
        "are written (COMMENTS-INDEX.md present), keeping the wave-2 seat's and wave 1's "
        "NOT YET RUN as history",
        ("(4) DOCKET 66 wave 1 is RUN" in _m10[3], d67_comments_present(),
         "SEATED AT D68 WAVE 2 (kept): (3) and (4) are NOT YET RUN" in _m10[3],
         "FIRST APPLIED (wave 1, kept): (2), (3) and (4) are NOT YET RUN" in _m10[3]),
        (True, True, True, True))
    chk("the docstring states section 8 and names its limitations",
        all(x in __doc__ for x in ("8.  DOCKET 66, WAVE 1, AS SEATED",
                                   "H-NO-D66-ROW", "H-LEDGER-ASKS-REPRESENTATIVES grows",
                                   "THE TURN QUESTION", "RECORDED FOR THE D68 BOARD",
                                   "8b.  M'S DOCKET 66 RULINGS")), True)

    print("\n5. THE BALANCE REFUSES TO INVENT A LADDER")
    chk("every balance row whose mechanism fails carries NO gap number",
        all(g is None for _i, _w, _d, _s, g in balance()), True)
    chk("and there are four such rows", len(balance()), 4)

    print("\n6. THE GENERATED DOCUMENT ROUND-TRIPS, AND THE DRIFT CHECK BITES")
    # MUTATED ON A SCRATCH COPY, never on LEDGER.md itself.  A --check that has
    # never been shown to fail is decoration, and this tree has just finished
    # removing nine z3 probes that could not fire.
    import os
    import tempfile
    md = to_markdown()
    chk("the document is generated, not typed -- it re-renders identically",
        to_markdown() == md, True)
    d = tempfile.mkdtemp()
    good, bad = os.path.join(d, "G.md"), os.path.join(d, "B.md")
    with open(good, "w", encoding="utf-8") as fh:
        fh.write(md)
    with open(bad, "w", encoding="utf-8") as fh:
        fh.write(md.replace("1.348948e+26", "1.348949e+26"))
    chk("--check passes on a faithful copy", check(good), 0)
    chk("and FAILS on one digit of the exchange rate", check(bad), 1)
    chk("and fails on an absent file", check(os.path.join(d, "nope.md")), 1)
    # LEDGER.md IS FOUND FROM ANY CWD.  It was resolved against the cwd, and
    # --check from the repository root reported a tracked file missing.  Run
    # from a directory holding no LEDGER.md: the default path must find the
    # real one and pass, and the old cwd-relative path must not find it.
    here = os.getcwd()
    try:
        os.chdir(d)
        from_elsewhere = check()
        old_relative = check("LEDGER.md")
    finally:
        os.chdir(here)
    chk("--check from another cwd finds LEDGER.md beside ledger.py, passes",
        (from_elsewhere, LEDGER_MD == os.path.join(HERE, "LEDGER.md")),
        (0, True))
    chk("  CONTROL: the cwd-relative path, from there, does not find it",
        old_relative, 1)
    for f in (good, bad):
        os.unlink(f)
    os.rmdir(d)

    print("\n7. WHAT THIS FILE CLAIMS ABOUT ITSELF")
    chk("it derives nothing -- every row is asked or cited",
        DERIVES_NOTHING, True)
    chk("it does not total the gaps", TOTALS_THE_GAPS, False)
    chk("it does not rank the open questions", RANKS_THE_OPEN, False)
    chk("the conjunction of DOCKET 55's limbs is a SURVEY, never a theorem",
        [r[2] for r in DEMAND if r[0] == "D12"], [SURVEY])
    chk("nothing is repaired and no peer is edited",
        (NOTHING_IS_REPAIRED, NO_PEER_IS_EDITED), (True, True))

    print("\n  SELFTEST %s" % ("OK" if ok else "FAILED"))
    return 0 if ok else 1


DERIVES_NOTHING = True
TOTALS_THE_GAPS = False
RANKS_THE_OPEN = False
NOTHING_IS_REPAIRED = True
NO_PEER_IS_EDITED = True


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--md" in sys.argv:
        sys.exit(write_md())
    if "--check" in sys.argv:
        sys.exit(check())
    sys.exit(report())
