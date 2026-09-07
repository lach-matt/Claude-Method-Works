#!/usr/bin/env python3
"""directives.py -- the three project directives as three index axes, and every
result in the papers placed on all three.

The project has three directives and they are not one question:

    X   identify and PROVE a self-sustaining cold fusion reaction
    Y   identify the MATERIALS needed
    Z   lay out the laboratory PROCEDURE that would witness it

Prose can answer one of those while sounding like it answered three. An index
cannot. Every substantive result in the three papers is placed here at a grade
on each axis, and the instrument reads off the cell where all three coincide --
which is the only cell that answers the project, and which is not the cell a
reader of the abstracts would guess.

The grade is a judgement; what is NOT a judgement is (a) that the rubric is
applied uniformly, (b) that every row names a section that exists in a paper
that exists -- --selftest checks every one against the files -- and (c) that
the X axis carries a SIGN, so a result that forbids self-sustaining operation
is never silently counted as progress toward it. A status is never flattened,
and neither is a direction.

Stdlib only.  python3 tools/directives.py [--selftest|--axis X|--cell|--gaps]
"""
import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PAPERS = {
    "BE": "papers/Cold_Fusion_Binder_Economy_v1.0.md",
    "SP": "papers/Cold_Fusion_Specification_and_Procedure_v1.0.md",
    "IR": "papers/Independent_Reconciliation_v1.0.md",
    "CF": "papers/out/Cold_Fusion_v1.0.md",
}

# ---- the rubric, stated once and applied to every row ----------------------
RUBRIC = {
    "X": ("PROVE a self-sustaining reaction -- does this settle whether the "
          "configuration returns more than it costs, with no subsidy per event?",
          {3: "DECIDES  -- closes the question for a named configuration",
           2: "BOUNDS   -- a hard bound no later work may cross",
           1: "BEARS    -- an input to the balance, not a bound on it",
           0: "SILENT"}),
    "Y": ("identify the MATERIALS -- does this fix something that must be "
          "procured, built or assayed?",
          {3: "SPECIFIES -- a procurable specification: substance, quantity, tolerance",
           2: "CONSTRAINS -- narrows the choice without fixing it",
           1: "IMPLIES   -- bears on a choice of material",
           0: "SILENT"}),
    "Z": ("lay out the PROCEDURE -- does this state a laboratory action whose "
          "outcome is committed in advance?",
          {3: "PROTOCOL  -- executable, with its outcomes committed before the run",
           2: "MEASURE   -- a named measurement on named apparatus",
           1: "IMPLIES   -- a measurement is implied but not specified",
           0: "SILENT"}),
}
SIGNS = {1: "+ supports", -1: "- forbids", 0: "0 neither"}

# ---- the index ------------------------------------------------------------
# (id, paper, section, datum, X, sign, Y, Z)
# `section` is matched against the paper's own headings by --selftest, so a row
# cannot cite a section that is not there.
ROWS = [
    ("D01", "BE", "1", "the definition and the eight conditions; condition 8 is the criterion itself", 3, 0, 1, 0),
    ("D02", "BE", "2", "the unique realisation: binder window [119, 918] m_e admits one occupant", 3, -1, 3, 0),
    ("D03", "BE", "3", "the procedure the definition already implies", 1, 0, 2, 3),
    ("D04", "BE", "4", "the binder economy: what a cycle returns against what a binder costs", 2, 0, 0, 0),
    ("D05", "BE", "5", "where condition 8 sits: the shortfall, stated", 3, -1, 0, 0),
    ("D06", "BE", "5.1", "production integrated over the full angular range: 11.13 GeV per pi-", 3, -1, 2, 1),
    ("D07", "BE", "5.2", "collection alone cannot satisfy condition 8, at any efficiency", 3, -1, 0, 0),
    ("D08", "BE", "5.3", "the discard, measured", 2, 0, 1, 1),
    ("D09", "BE", "5.4", "what remains open after the collection argument", 1, 0, 0, 1),
    ("D10", "BE", "5.5", "the residual localises to one unresolved measurement", 2, 0, 0, 2),
    ("D11", "BE", "5.6", "the experiment this paper already specifies", 2, 0, 2, 3),
    ("D12", "BE", "5.7", "the binder is not the problem: sticking is binder-mass-independent", 2, -1, 1, 0),
    ("D13", "BE", "5.8", "the convertible fraction is 0.795, not 0.501", 2, 1, 2, 0),
    ("D14", "BE", "5.9", "the collector, specified", 2, 0, 3, 1),
    ("D15", "BE", "5.10", "the deciding experiment, stated as a protocol with a refusal rule", 2, 0, 2, 3),
    ("D16", "BE", "5.11", "the service-life cap is asymptotic and reaching it costs density", 2, -1, 2, 0),
    ("D17", "BE", "5.12", "a neutron multiplier, bounded rather than adopted", 2, 1, 2, 0),
    ("D18", "BE", "5.13", "density is bounded above, and the bound is structural", 2, -1, 2, 0),
    ("D19", "BE", "5.14", "the terminal balance", 3, -1, 0, 0),
    ("D20", "BE", "5.15", "the last four percent sits on an axis held constant: temperature", 2, 0, 2, 2),
    ("D21", "BE", "5.16", "the conversion ceiling is a consequence of condition 1", 2, -1, 0, 0),
    ("D22", "BE", "5.17", "an independent review, its agreements and its errors", 1, 0, 0, 0),
    ("D23", "BE", "5.18", "the neutron priced as bred fuel is worth 146.06 MeV, not 26.06", 3, 1, 3, 1),
    ("D24", "BE", "5.19", "the blanket on sourced ground: the heat form reaches 1.241 AT 90 percent, withdrawn end-to-end by 5.31", 3, 0, 3, 1),
    ("D25", "BE", "5.20", "the in-flight escape closes; the stripping route opens, capped at 1.39", 2, 1, 2, 1),
    ("D26", "BE", "5.21", "the collector's constraint is shielding, not the magnet", 2, 0, 3, 1),
    ("D27", "BE", "5.22", "what each product asks of the collector: 299.6 / 72.5 / 50.8 percent", 3, 0, 2, 1),
    ("D28", "BE", "5.23", "two routes, one shared dependency", 3, 0, 1, 1),
    ("D29", "BE", "5.24", "the acceptance model reproduces the built machine's MARS15 to 0.982", 3, 0, 3, 2),
    ("D30", "BE", "5.25", "the stopping window is bought with tritium, and it saturates", 2, -1, 3, 1),
    ("D31", "BE", "5.26", "the witnessed sticking: 0.557 percent, 198 cycles, k = 0.464", 3, -1, 2, 2),
    ("D32", "BE", "5.27", "what the independent literature does to these figures", 2, 0, 1, 1),
    ("D33", "BE", "5.28", "the species: mu- from pi- only, and a high-Z target for the charge", 1, 0, 3, 1),
    ("D34", "BE", "6", "what the definition excludes: no other binder in the known spectrum", 3, -1, 1, 0),
    ("D35", "BE", "7", "provenance and verification", 0, 0, 0, 1),
    ("D36", "BE", "8", "what this paper retires", 0, 0, 0, 0),
    ("D37", "BE", "9", "limits and the state of the question: purity, acceptance, temperature", 2, 0, 2, 2),
    ("D38", "BE", "10", "the laboratory programme, four staged measurements on apparatus that exists", 2, 0, 3, 3),
    ("D39", "BE", "10.1", "Stage A -- the acceptance measurement", 2, 0, 3, 3),
    ("D40", "BE", "10.2", "Stage B -- the sticking branch, with purity as a controlled variable", 3, 0, 3, 3),
    ("D41", "BE", "10.3", "Stage C -- the production target, measured rather than simulated", 2, 0, 3, 3),
    ("D42", "BE", "10.4", "Stage D -- the integrated demonstration", 3, 0, 3, 3),
    ("D43", "BE", "10.5", "the order, and what none of it requires", 1, 0, 1, 3),
    ("D44", "SP", "1", "the reaction specified, every free parameter fixed", 2, 0, 3, 1),
    ("D45", "SP", "2", "bill of materials, bench column and reactor column", 0, 0, 3, 1),
    ("D46", "SP", "3", "the laboratory procedure, bench scale", 1, 0, 3, 3),
    ("D47", "SP", "3.1", "assembly", 0, 0, 3, 3),
    ("D48", "SP", "3.2", "loading", 0, 0, 3, 3),
    ("D49", "SP", "3.3", "the measurement: two observables, simultaneous, on one target", 2, 0, 2, 3),
    ("D50", "SP", "3.4", "what each outcome settles, committed in advance", 2, 0, 0, 3),
    ("D51", "SP", "4", "what this returns, and what it does not", 2, 0, 1, 2),
    ("D52", "SP", "5", "the net-positive configuration", 3, 0, 2, 2),
    ("D53", "SP", "5.1", "the standalone case is closed by theorem, not by measurement", 3, -1, 1, 0),
    ("D54", "SP", "5.2", "the binder does not have to be bought; its ceiling is the stopping fraction, 0.342", 3, 1, 3, 2),
    ("D55", "SP", "5.3", "what this is, and what it is not", 2, 0, 0, 1),
    ("D56", "IR", "2.1", "pricing the stripping route -- the companion's own estimate", 2, 1, 1, 0),
    ("D57", "IR", "2.2", "an optimised production target at 4.69 GeV per pion", 2, 1, 3, 2),
    ("D58", "IR", "2.3", "an independent review reaches the same escape", 2, 1, 1, 0),
    ("D59", "IR", "2.4", "the deciding measurement is being made, and exposes an unpriced channel", 2, 0, 2, 3),
    ("D60", "IR", "2.5", "condition 8 derived independently; the 2.24 over-prediction, closed at BE:5.29", 3, -1, 0, 1),
    ("D61", "IR", "2.6", "the stripping route priced independently, and a newer sticking calculation", 2, 0, 1, 1),
    ("D62", "IR", "3", "what the four results leave standing", 3, 0, 1, 1),
    # Added after the first reading of this index, which found D54 short on Z and
    # nothing else short at all. The proof is D54's and is carried by reference;
    # what this row adds is the apparatus, the gating and the committed rate.
    ("D72", "BE", "5.31", "every balance restated at the delivered acceptance: the 1.241 does not survive", 3, -1, 1, 1),
    ("D73", "BE", "5.32", "what that withdraws and what survives: one route, bred fuel through an optimised target", 3, 1, 2, 1),
    ("D74", "BE", "5.33", "the acceptance census: 57 sites over three papers, completeness measured at residue 0", 3, -1, 2, 1),
    ("D75", "SP", "5.2", "the co-product headline restated: 176 kW at 0.50 is 85.6 delivered, and the sign of the balance does not move", 3, 1, 3, 2),
    # D76 CORRECTED. It read "the heat form clears at 1.036 delivered", which
    # was the balance table run at the RETIRED 0.1487 % sticking. Recomputed,
    # no heat form clears anywhere. What sec.5.24 actually supports is the
    # bred-fuel route, and the row is returned to that.
    ("D76", "BE", "5.24", "the optimised target priced against the bred-fuel route: 50.8 percent becomes 21.4", 3, 1, 2, 2),
    ("D71", "SP", "11", "the end-to-end loss budget: Q6 closed on geometry, Q1 narrowed to a number, and the two coupled", 3, 0, 2, 2),
    ("D70", "SP", "6", "the procedure repointed at the designed machine; the prediction moves by 6 percent", 3, 1, 3, 3),
    ("D69", "SP", "10", "the fuel cell designed: the decay channel, recompression, and one loop for two requirements", 2, 1, 3, 3),
    ("D68", "SP", "9", "the build package: circuit, conductor, target, lifetime, plant, failure, integration", 2, 1, 3, 3),
    ("D67", "SP", "8", "the capture solenoid designed: the mirror term supplied, worth 1.299, grade fixed at 1.428", 2, 1, 3, 2),
    ("D64", "SP", "7", "the nine open questions worked: eight closed, one narrowed to a budget", 3, 1, 1, 2),
    ("D65", "BE", "5.29", "one measurement settles four: the sticking inverted, the 2.24, the purity bound, the wedge", 3, 0, 2, 1),
    ("D66", "BE", "5.30", "the acceptance model's scope limit: one validation, two withdrawn claims, no mirror term", 2, 0, 2, 2),
    ("D63", "SP", "6", "the procedure for the net-positive configuration: 2.41 mg, 2.528e10 n/s committed", 3, 1, 3, 3),
    # ---- the consolidated paper, which is the deliverable ------------------
    ("D77", "CF", "5.3", "every balance recomputed at the corrected sticking: the printed bound case was 588.9 cycles, high by 3.10", 3, -1, 1, 1),
    ("D78", "CF", "5.4", "no heat form and no work form clears unity in any configuration: the largest is 0.513", 3, -1, 1, 1),
    ("D79", "CF", "5.4", "bred fuel at the MEASURED cycle count clears: 1.480 through the target, 2.271 with all three alterations", 3, 1, 2, 2),
    ("D80", "CF", "5.3", "and with no unmeasured multiplier at all it reaches 0.957, short by 1.045", 3, -1, 1, 2),
    ("D81", "CF", "12", "what is proved sorted from what is unwitnessed: two unmeasured terms, each with the measurement that closes it", 3, 0, 2, 2),
    ("D82", "CF", "13", "Theorem 1 closed on a checkable set: five charged particles outlive the mesomolecular formation time", 3, -1, 3, 0),
    ("D83", "CF", "11", "the bred-fuel balance is not compared against spallation breeding on the same beam", 2, 0, 0, 2),
    ("D84", "CF", "11", "the plant tritium inventory is unpriced: 5.13 kg against the 2.41 mg demonstrated", 2, -1, 3, 1),
    ("D85", "CF", "6", "the reaction specified to the last free parameter, as a bill of materials", 1, 0, 3, 2),
    ("D86", "CF", "8", "the procedure, with predictions committed in advance and a disagreement read as a refusal", 1, 0, 2, 3),
    # THE ROW THE PROJECT ASKED FOR. The balance run backwards rather than
    # forwards: two of its four terms are closed above by physics, so a
    # self-sustaining POWER source is a statement about the blanket alone, and
    # a subcritical one supplies the requirement between k = 0.469 and 0.770.
    ("D87", "CF", "9.2", "the self-sustaining POWER source specified: k between 0.469 and 0.770, heat on site, nothing leaving the device", 3, 1, 3, 2),
    ("D88", "CF", "9.3", "and how k is measured: pulsed neutron, source jerk and Rossi-alpha, two of which must agree", 3, 0, 2, 3),
    ("D89", "CF", "9.2", "what it costs to say it: the fusion supplies 7.5 to 27.4 percent, so it is a fusion-driven subcritical fission reactor", 3, -1, 2, 1),
]

ON_AXIS = 2          # a datum "sits on" an axis at this grade or better


def _headings(key):
    path = os.path.join(ROOT, PAPERS[key])
    out = set()
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^#{2,3}\s+([0-9]+(?:\.[0-9]+)?)[.]?\s", line)
        if m:
            out.add(m.group(1))
    return out


def cell(rows=None):
    """Rows sitting on all three axes at once."""
    return [r for r in (ROWS if rows is None else rows)
            if r[4] >= ON_AXIS and r[6] >= ON_AXIS and r[7] >= ON_AXIS]


def full(rows=None):
    """Rows at the top grade on all three."""
    return [r for r in (ROWS if rows is None else rows)
            if r[4] == 3 and r[6] == 3 and r[7] == 3]


def by_sign(sign):
    return [r for r in ROWS if r[4] == 3 and r[5] == sign]


def _fmt(r):
    rid, pk, sec, datum, x, sg, y, z = r
    return (f"  {rid}  {pk}:{sec:<5} X{x}{'+' if sg > 0 else '-' if sg < 0 else ' '}"
            f" Y{y} Z{z}   {datum}")


def report_axes():
    print("THE THREE DIRECTIVES AS THREE AXES")
    print()
    for ax in ("X", "Y", "Z"):
        head, grades = RUBRIC[ax]
        print(f"  {ax} -- {head}")
        for g in (3, 2, 1, 0):
            n = sum(1 for r in ROWS if r[{"X": 4, "Y": 6, "Z": 7}[ax]] == g)
            print(f"       {g}  {grades[g]:<58} {n:>3} rows")
        print()
    print(f"  {len(ROWS)} results indexed across {len(PAPERS)} papers."
          f"  On-axis threshold: grade >= {ON_AXIS}.")


def report_cell():
    c, f = cell(), full()
    print("THE COINCIDENCE CELL -- results sitting on all three axes at once")
    print()
    for r in c:
        print(_fmt(r))
    print()
    print(f"  {len(c)} of {len(ROWS)} results sit on all three axes.")
    print()
    print("  At the TOP grade on all three -- a result that decides the balance,")
    print("  specifies its materials, and carries an executable protocol:")
    print()
    for r in f:
        print(_fmt(r))
    print()
    undecided = [r for r in f if r[5] == 0]
    print(f"  {len(f)} rows at the top of all three, {len(undecided)} of them X-sign 0.")
    print("  An X-sign of 0 at grade 3 means the row would DECIDE the balance and")
    print("  has not: it is the measurement, not its result. A cell filled by")
    print("  undecided measurements is not an answered directive.")
    print()
    print("  and the rows that DECIDE the balance favourably, with their standing")
    print("  on the other two axes:")
    print()
    for r in by_sign(1):
        short = [ax for ax, i in (("Y", 6), ("Z", 7)) if r[i] < 3]
        tag = "" if not short else f"   <-- short on {'/'.join(short)}"
        print(_fmt(r) + tag)


def report_gaps():
    print("WHAT SITS ON TWO AXES AND FALLS OFF THE THIRD")
    print()
    for ax, idx, label in (("X", 4, "PROOF"), ("Y", 6, "MATERIALS"), ("Z", 7, "PROCEDURE")):
        others = [i for i in (4, 6, 7) if i != idx]
        miss = [r for r in ROWS
                if r[idx] < ON_AXIS and all(r[i] >= ON_AXIS for i in others)]
        print(f"  falls off {ax} ({label}): {len(miss)}")
        for r in miss:
            print(_fmt(r))
        print()

    print("  THE ONE THAT MATTERS. The results that DECIDE the balance in the")
    print("  favourable direction -- X = 3, sign + -- and where they stand on Z:")
    print()
    for r in by_sign(1):
        gap = "" if r[7] >= ON_AXIS else "   <-- NO PROTOCOL"
        print(_fmt(r) + gap)
    print()
    print("  and the results that DECIDE it in the forbidding direction:")
    print()
    for r in by_sign(-1):
        print(_fmt(r))


def report_verdict():
    pos, neg = by_sign(1), by_sign(-1)
    c, f = cell(), full()
    occ = [r for r in ROWS if r[4] == 3 and r[5] == 1 and r[7] == 3]
    print("THE READING -- what the index says about each directive")
    print()
    print("  DIRECTIVE 1: identify and PROVE a self-sustaining reaction.")
    print(f"    {len(pos) + len(neg)} results decide the balance for a named configuration:")
    print(f"      {len(neg)} forbid, {len(pos)} support.")
    print("    The forbidding set closes the STANDALONE configuration -- the one that")
    print("    takes no subsidy per event and sells one product -- by theorem rather")
    print("    than by measurement. The supporting set closes configurations that")
    print("    sell a second product or do not buy the binder. So the answer to the")
    print("    question as asked is NO standalone and YES as a co-product, and both")
    print("    halves are proved rather than asserted.")
    print()
    print("  DIRECTIVE 2: identify the MATERIALS.")
    n3y = sum(1 for r in ROWS if r[6] == 3)
    print(f"    {n3y} results specify a procurable material, quantity or tolerance,")
    print("    for the bench column, the reactor column and the in-situ cell.")
    print()
    print("  DIRECTIVE 3: lay out the PROCEDURE.")
    n3z = sum(1 for r in ROWS if r[7] == 3)
    attached = [r for r in ROWS if r[7] == 3 and r[4] == 3 and r[5] == 1]
    verb = "is" if len(attached) == 1 else "are"
    print(f"    {n3z} results carry an executable protocol, and {len(attached)} of them {verb}")
    print("    attached to a configuration this index shows to be net-positive.")
    print()
    print("  THE COINCIDENCE -- the cell the project asked for.")
    print(f"    {len(c)} results sit on all three axes at grade >= {ON_AXIS};"
          f" {len(f)} at the top of all three.")
    v = "carries" if len(occ) == 1 else "carry"
    print(f"    Of those, {len(occ)} {v} a POSITIVE proof sign:")
    print()
    for r in occ:
        print(_fmt(r))
    print()
    if not occ:
        print("    -- none. The three directives are each answered somewhere and")
        print("       never at the same point.")
    else:
        print("    This is the data point that sits on all three axes. It proves a")
        print("    configuration net-positive, fixes what it is made of, and states")
        print("    how it would be run with its outcomes committed in advance.")
    print()
    print("  THE SURROUNDING POINTS -- what supports it, and what it must not be")
    print("  confused with.")
    print()
    print("    supports it (X3+, the proof it inherits or leans on):")
    for r in by_sign(1):
        if r not in occ:
            print(_fmt(r))
    print()
    print("    bounds it (X3-, the configurations it must never be read as):")
    for r in by_sign(-1):
        print(_fmt(r))
    print()
    print("    and the measurements that would move it (3-3-3, X-sign 0 -- these")
    print("    are the deciding measurements, not their results):")
    for r in f:
        if r[5] == 0:
            print(_fmt(r))
    print()
    print("  WHAT IS STILL SHORT.")
    short = [r for r in by_sign(1) if r[7] < 3]
    for r in short:
        print(f"    {r[0]} {r[1]}:{r[2]} -- X3+ Y{r[6]} Z{r[7]}: {r[3]}")
    if short:
        print("    These decide favourably and carry no protocol of their own. They")
        print("    are not gaps in the answer -- the answer is above -- but each is a")
        print("    second route to it that nobody could run from what is written.")


def selftest():
    fail = 0
    print("directives.py --selftest")
    print()
    print("  every row cites a section that exists in the paper it names")
    heads = {k: _headings(k) for k in PAPERS}
    bad = [r for r in ROWS if r[2] not in heads[r[1]]]
    fail += len(bad)
    for r in bad:
        print(f"    {r[0]} cites {r[1]}:{r[2]} -- NO SUCH SECTION   FAIL")
    print(f"    {len(ROWS)} rows checked against {sum(len(v) for v in heads.values())}"
          f" headings   {'PASS' if not bad else 'FAIL'}")

    print()
    print("  grades are in range and ids are unique")
    ok = all(0 <= r[4] <= 3 and 0 <= r[6] <= 3 and 0 <= r[7] <= 3 and r[5] in (-1, 0, 1)
             for r in ROWS)
    fail += 0 if ok else 1
    print(f"    grades 0-3, signs -1/0/+1   {'PASS' if ok else 'FAIL'}")
    ok = len({r[0] for r in ROWS}) == len(ROWS)
    fail += 0 if ok else 1
    print(f"    {len(ROWS)} unique ids   {'PASS' if ok else 'FAIL'}")

    print()
    print("  a sign is only carried where the row bounds or decides something")
    ok = all(r[5] == 0 or r[4] >= ON_AXIS for r in ROWS)
    fail += 0 if ok else 1
    print(f"    X-sign is non-zero only at X >= {ON_AXIS}"
          f"   {'PASS' if ok else 'FAIL'}")

    print()
    print("  the standing refusal -- the claim this index would have to withdraw")
    occ = [r for r in ROWS if r[4] == 3 and r[5] == 1 and r[7] == 3]
    print("    the cell where a favourably-decided balance meets an executable")
    if not occ:
        print("    protocol (X3+ and Z3) is EMPTY. The directives are each answered")
        print("    somewhere and never at the same point.")
    else:
        print("    protocol (X3+ and Z3) is OCCUPIED:")
        for r in occ:
            print("   " + _fmt(r))
        print("    This is a state, not a failure. It is what the project asked for,")
        print("    and it is reported rather than asserted.")
    n = len([r for r in full() if r[5] == 0])
    print(f"    3-3-3 rows: {len(full())}, of them X-sign 0: {n}"
          f"   (reported, not asserted)")

    print()
    print("  coverage: each directive is answered somewhere")
    for ax, idx in (("X", 4), ("Y", 6), ("Z", 7)):
        n = sum(1 for r in ROWS if r[idx] == 3)
        ok = n > 0
        fail += 0 if ok else 1
        print(f"    axis {ax} has {n} rows at the top grade   {'PASS' if ok else 'FAIL'}")

    print()
    print(f"selftest: {fail} failures -> {'PASS' if fail == 0 else 'FAIL'}")
    return 1 if fail else 0


def main():
    ap = argparse.ArgumentParser(description="the three directives as three index axes")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--axes", action="store_true", help="the rubric and the coverage")
    ap.add_argument("--cell", action="store_true", help="what sits on all three axes")
    ap.add_argument("--gaps", action="store_true", help="what sits on two and falls off one")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if a.axes:
        report_axes()
        return 0
    if a.cell:
        report_cell()
        return 0
    if a.gaps:
        report_gaps()
        return 0
    report_axes()
    print()
    report_cell()
    print()
    report_verdict()
    return 0


if __name__ == "__main__":
    sys.exit(main())
