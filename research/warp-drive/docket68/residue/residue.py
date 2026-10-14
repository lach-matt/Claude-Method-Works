#!/usr/bin/env python3
"""residue.py -- every open row on the board, read against M's later rulings (M-RULINGS item 135, step 1).

M's order (item 135): "Older waves first, then read/search outside art for sources and measurements, computable
loose ends next, then reassess the questions only for me and present them. After all that, reassess the walls".

This instrument is step 1.  It takes every open row ledger.py carries -- imported from ledger.py, never copied --
and gives each exactly one disposition, with the M ruling that decides it and a fragment of that ruling's recorded
text, which the selftest finds in the ruling.  A disposition that cites a ruling it cannot quote fails.  The search runs over the item's whole record -- your words and
the board's text around them -- so that a fragment is YOUR word was checked by the verifier by hand, not by code.

Dispositions
  RULED     an M ruling answers the row's question.
  OFF-PATH  an M ruling removes the premise the row rested on.  Kept as the boundary (item 82), never dropped.
  SUBSUMED  the same question now stands as a live row (the target), which carries it.
  CARRIED   an M ruling answers it with a premise of physics that is carried, not measured.  It goes to the walls.
  OFF-CHAIN a thread no link of the current chain uses (its tags are absent from every front owner), with no ruling
            withdrawing it.  Kept, not on the chain.
  INPUT     an input's value, which M ruled the user gives per trip (items 119, 130).  No chain link waits on it;
            every result is a formula in the input.
  LIVE      still open on the chain, with its route: COMPUTE, READ, or M (a ruling only M can give).

New rows (RES-N*) are opened where the audit finds a question no row asked.

Stdlib only; imports ledger.py (about 75 s, ledger computes its cells on import).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")

OLDER_LISTS = ("W3S1B_OPEN", "S1C_OPEN", "W4_OPEN", "CMB_OPEN", "CMB2_OPEN", "CMB3_OPEN", "BULK_OPEN",
               "BULK2_OPEN", "BULK3_OPEN", "BULK4_OPEN", "BULK5_OPEN")
FRONT_LISTS = ("COPY_OPEN", "CHAIN8O_OPEN", "CHAIN8P_OPEN")

# The current chain's owners: an OFF-CHAIN tag must appear in none of them.
def _front_owners():
    """Every instrument under docket68/copy and docket68/bulk, and what chain.py loads beside them."""
    out = []
    for sub in ("copy", "bulk"):
        dd = os.path.join(D68, sub)
        out += [os.path.join(dd, f) for f in sorted(os.listdir(dd)) if f.endswith(".py")]
    out += [os.path.join(D68, p) for p in ("cmb/cmbframe.py", "frame.py", "measure.py")]
    out += [os.path.join(WD, p) for p in ("create.py", "cosmo.py", "nopath.py")]
    return tuple(out)


FRONT_OWNERS = _front_owners()

KINDS = ("RULED", "OFF-PATH", "SUBSUMED", "CARRIED", "OFF-CHAIN", "INPUT", "LIVE")
ROUTES = ("COMPUTE", "READ", "M")

# Rows the audit opens.  (id, question, route)
NEW_ROWS = (
    ("RES-N1", "items 111 and 133 make the build's energy EQUAL to E(N): does the assembly's free energy at position 2 "
     "equal E(N), and if not, where does the difference go (loose.py L1)", "COMPUTE"),
    ("RES-N2", "whether the original at position 1 stays or is retired (H-RETIRE-A; asked twice: item 32 'I suspect "
     "so', item 89 'Leave it open'; chain.py W11 names it).  Re-presented because step 2 found no read that leaves a "
     "body whole: if the original is retired, a destroying read suffices", "M"),
    ("RES-N3", "what synchronizing two universes' cosmic beats means (item 97: the beat synchronized, readings "
     "relative to each observer; item 114(d): both cosmologies bound the corridor) -- by which quantity each end "
     "reads the shared instant when the ends lie in separate universes (item 101 answer 5)", "M"),
    ("RES-N4", "the build at position 2: where the closing hold's bits go when position 2's horizon ends (item 109 "
     "left it OPEN; item 110 answered only the energy) and how long the build takes (COPY-O9's t_build)", "M"),
    ("RES-N5", "what 'most simplistically exact binary code form' (item 131) means: the shortest possible encoding "
     "(a minimum the board cannot compute in general) or one fixed exact encoding (computable), and so how the device "
     "fixes N (item 101 answer 6: 'assess the README size')", "M"),
)

# id -> (kind, [(item, quote), ...], target-or-route, note)
D = {
    # ---- DOCKET 68 wave 3 and Step 1b (section 8c)
    "S1B-O1": ("RULED", [(130, "read from the object being moved? - yes"),
                         (131, "the size of the throat is dependent on the size of the README")], None,
               "the count is the input N, read from the object each trip, in 'its most simplistically exact binary "
               "code form' (131).  Items 33 and 89(c)'s readings are set aside only on the board's reading of 131; "
               "what 'most simplistically exact' means is RES-N5"),
    "S1B-O2": ("CARRIED", [(111, "that and only that which is provided by the closing of the horizon"),
                           (89, "Stock is stock")], None,
               "the build's energy is your premise H-BUILD-IS-CLOSING-ENERGY, so the stock's form sets no separate "
               "energy term; whether the build's free energy equals E(N) is RES-N1, and the retire energy's sign at "
               "position 1 waits on RES-N2.  To the walls"),
    "S1B-O3": ("SUBSUMED", [(111, "that and only that which is provided by the closing of the horizon")], "RES-N1",
               "the entropy the build exports is part of RES-N1's floor"),
    "S1B-O4": ("CARRIED", [(91, "Position 2 itself"), (101, "information is a form of energy")], None,
               "the placer is position 2 itself by a field reaction, your premise, as COPY-O2; the work per atom is "
               "RES-N1's.  To the walls"),
    "S1B-O5": ("OFF-PATH", [(110, "Into position 2"),
                            (111, "that and only that which is provided by the closing of the horizon")], None,
               "no collector at position 2: the build's energy is the closing hold's"),
    "S1B-O6": ("OFF-PATH", [(110, "Into position 2")], None,
               "fed S1B-O5's collector at Proxima b; the record of the discrepancy is kept"),
    "S1B-O7": ("SUBSUMED", [(130, "read from the object being moved? - yes")], "COPY-O3",
               "the read at position 1; whether its destroying the original matters is RES-N2"),
    "W3-O1": ("SUBSUMED", [(95, "Two places made one")], "C8O-O4",
              "the coupling is the corridor itself; its construction is wall 9"),
    "W3-O2": ("OFF-PATH", [(119, "precision is never a question")], None,
              "H-12-CARRIER read the twelve as carried by state-dependent constants matched between the seats; the "
              "destination is the user's exact input"),
    "W3-O3": ("SUBSUMED", [(89, "Stock is stock")], "COPY-O4",
              "item 89 sets the PRIMITIVE clause aside; what stays is a destination's composition, wall 7"),
    "W3-O4": ("OFF-PATH", [(119, "precision is never a question"), (116, "No, separate")], None,
              "the seats were ranked to choose a destination; the destination is the user's input, exact"),
    "W3-O5": ("OFF-PATH", [(119, "precision is never a question")], None,
              "complex binary entered item 25's ranking of seats, which the user's exact input replaces"),
    "W3-O6": ("SUBSUMED", [(118, "Yes: law and history")], "C8O-O7",
              "spatial bounds on the constants are the range C8O-O7 asks of each law trajectory"),
    # ---- Step 1c (section 8d)
    "S1C-O1": ("SUBSUMED", [(130, "read from the object being moved? - yes")], "COPY-O3", "the read"),
    "S1C-O2": ("CARRIED", [(91, "Position 2 itself")], None,
               "placement is position 2's own build, as COPY-O2 (chain.py W5 lists S1C-O2 in the builder wall).  To "
               "the walls"),
    "S1C-O3": ("OFF-PATH", [(90, "not by light"), (94, "their is no movement in warp travel")], None,
               "no optical link carries the README"),
    "S1C-O4": ("SUBSUMED", [(101, "distance is irrelevant"), (95, "Two places made one")], "C8O-O4",
               "distance-freedom is M's (H-DISTANCE-IRRELEVANT); its physics is wall 9"),
    "S1C-O5": ("OFF-PATH", [(94, "their is no movement in warp travel")], None,
               "the Bell-test tables priced a speed of influence"),
    "S1C-O6": ("OFF-PATH", [(87, "A faithful copy")], None, "a quantum payload: the boundary of the faithful copy"),
    "S1C-O7": ("OFF-PATH", [(87, "A faithful copy")], None, "the quantum payload's storage"),
    "S1C-O8": ("OFF-PATH", [(90, "not by light")], None, "the link's transmitted power"),
    # ---- wave 4 (section 8e)
    "W4-O1": ("OFF-PATH", [(90, "not by light")], None, "the link's optic"),
    "W4-O2": ("OFF-PATH", [(90, "not by light")], None, "the link's source"),
    "W4-O3": ("OFF-PATH", [(90, "not by light"), (94, "their is no movement in warp travel")], None,
              "the link's power"),
    "W4-O4": ("OFF-PATH", [(87, "A faithful copy")], None, "the quantum memory"),
    "W4-O5": ("OFF-PATH", [(87, "A faithful copy")], None, "a quantum payload: the boundary of the faithful copy"),
    "W4-O6": ("OFF-PATH", [(87, "A faithful copy"), (90, "not by light")], None,
              "the link's and the memory's dissipation"),
    # ---- H-CMB-CORRIDOR (sections 8f-8h)
    "CMB-O1": ("RULED", [(96, "My CMB preferred frame is cosmic background radiation")], None,
               "the frame is the background's rest frame, yours.  Whether that frame is exact FRW's cosmic frame "
               "(H-FRW-EXACT, item 97) is what the dipole anomaly bears on, and stays with RES-N3"),
    "CMB-O2": ("SUBSUMED", [(97, "synchronization of the cosmic")], "RES-N3",
               "the multi-spacetime clause becomes: whose beat, across two universes"),
    "CMB-O3": ("OFF-PATH", [(96, "My CMB preferred frame is cosmic background radiation")], None,
               "the background is the frame, not the medium, register or carrier"),
    "CMB-O4": ("OFF-PATH", [(94, "their is no movement in warp travel")], None, "a speed of influence"),
    "CMB2-O1": ("OFF-CHAIN", [], ("H-CONTRACT",), "a contracting universe; no link uses it"),
    "CMB2-O2": ("OFF-CHAIN", [], ("H-M-SUPPORT",), "observation extending the clock's support; item 97 keeps local clocks and takes them off the joining"),
    "CMB2-O3": ("OFF-CHAIN", [], ("H-CLOCK-WEIGHT",), "the clock weighting"),
    "CMB2-O4": ("OFF-CHAIN", [], ("H-CONSCIOUS-SELECTS",), "conscious selection; no link uses it"),
    "CMB2-O5": ("OFF-CHAIN", [], ("relational-time",), "interacting local clocks"),
    "CMB2-O6": ("OFF-CHAIN", [], ("Page & Wootters",), "the local-clock thread's sources"),
    "CMB3-O1": ("OFF-CHAIN", [], ("H-SUPPORT-IS-RECORDS", "H-RECORD-DURABLE"), "M-SUPPORT's records"),
    "CMB3-O2": ("OFF-CHAIN", [], ("LAST-RECORD", "M-SUPPORT"), "M-SUPPORT's support; asked only if revived"),
    "CMB3-O3": ("OFF-CHAIN", [], ("H-CONSCIOUS-SELECTS",), "bias.py's sources"),
    "CMB3-O4": ("OFF-CHAIN", [], ("H-Z-PER-SESSION",), "bias.py's channel model"),
    "CMB3-O5": ("OFF-CHAIN", [], ("M-SUPPORT",), "support.py's recombination"),
    # ---- the bulk (sections 8i-8m)
    "BULK-O1": ("SUBSUMED", [(126, "it is realized in the same place the position 1 occupies"), (127, "1 - yes")],
                "C8P-O2", "the destination is not brought close; it is realized in the same place"),
    "BULK-O2": ("SUBSUMED", [(115, "The README itself"), (91, "Inside, during the hold")], "C8O-O1",
                "entering is the README as the inflow, inside the hold; no rate (item 94); its join is C8O-O1"),
    "BULK-O3": ("CARRIED", [(123, "A second plane exists")], None,
                "M's premise; no observation has reached it.  To the walls"),
    "BULK-O4": ("LIVE", [], "READ", "Randall-Sundrum's printed k r_c, a text check"),
    "BULK-O5": ("SUBSUMED", [(122, "1 - likely yes")], "C8P-O6",
                "a time-delay theorem read as a censorship theorem (H-DELAY-AS-CENSORSHIP, the board's)"),
    "BULK2-O1": ("OFF-PATH", [(126, "it is realized in the same place the position 1 occupies")], None,
                 "the shapes brought a distant destination close"),
    "BULK2-O2": ("SUBSUMED", [(117, "An NEC is never violated"), (123, "A second plane exists")], "C8P-O6",
                 "M's H-NEC-NEVER-VIOLATED against the plane's computed reading"),
    "BULK2-O3": ("SUBSUMED", [(127, "these are coefficients")], "C8P-O3", "the 5D scale is k's"),
    "BULK2-O4": ("OFF-PATH", [(101, "distance is irrelevant"),
                              (126, "it is realized in the same place the position 1 occupies")], None,
                 "how close through the bulk a star can be"),
    "BULK2-O5": ("SUBSUMED", [(127, "these are coefficients")], "C8P-O3", "a collider bound on k"),
    "BULK2-O6": ("OFF-PATH", [(126, "it is realized in the same place the position 1 occupies")], None,
                 "Chung-Freese's shape"),
    "BULK2-O7": ("SUBSUMED", [(127, "these are coefficients")], "C8P-O3", "lighter gravitons; torsion bounds on k"),
    "BULK3-O1": ("RULED", [(87, "A faithful copy"), (131, "binary code form")], None,
                 "classical: a faithful copy from an exact binary README.  A classical pattern is copied unless the "
                 "original is erased: RES-N2"),
    "BULK3-O2": ("OFF-PATH", [(106, "Three distinct holds in one fluid wave motion")], None,
                 "the README is held on the horizons, not in a zero-mode stasis"),
    "BULK3-O3": ("SUBSUMED", [(132, "as well as the throat? - yes")], "C8O-O4",
                 "no separate carrier for the README; the stabilisation scalar stays as wall 9's dynamics (chain.py W9)"),
    "BULK3-O4": ("SUBSUMED", [(127, "1 - yes")], "C8P-O2", "the two tensions meet at the coinciding junction"),
    "BULK3-O5": ("OFF-PATH", [(126, "it is realized in the same place the position 1 occupies")], None,
                 "Chung-Freese's fluid"),
    "BULK3-O6": ("SUBSUMED", [(127, "1 - yes")], "C8P-O2",
                 "the junction re-run is C8P-O2; the light bending on our plane rides with k (C8P-O3)"),
    "BULK3-O7": ("OFF-PATH", [(126, "it is realized in the same place the position 1 occupies")], None,
                 "the fit was of Chung-Freese's deviation (H-PERCENT), off the path with BULK2-O6"),
    "BULK4-O1": ("OFF-PATH", [(106, "Three distinct holds in one fluid wave motion")], None, "a stasis with rest"),
    "BULK4-O2": ("SUBSUMED", [(124, "Both A and B")], "C8P-O2",
                 "the 1e60 scaling is H-TWO-PERSPECTIVE-TENSION's, which meets at the coinciding junction"),
    "BULK4-O3": ("SUBSUMED", [(109, "The horizon of position ends as well"), (115, "When fully realized")],
                 "C8O-O2", "the enclosure is position 2's horizon, which arises and ends with the corridor"),
    "BULK4-O4": ("SUBSUMED", [(132, "a black hole in and a white hole out")], "C8O-O1",
                 "the README leaves through the white-hole side, not a mirror"),
    "BULK4-O5": ("SUBSUMED", [(120, "matter is neither created nor destroyed")], "C8P-O1", "a horizon in the bulk"),
    "BULK4-O6": ("SUBSUMED", [(121, "we build it under closed index criteria")], "C8P-O1",
                 "locally answered (closedbulk.py, umbilic.py); globally C8P-O1"),
    "BULK4-O7": ("OFF-PATH", [(94, "their is no movement in warp travel")], None, "a moving bubble"),
    "BULK4-O8": ("SUBSUMED", [(121, "we build it under closed index criteria")], "C8P-O1",
                 "the bulk Weyl part is fixed at the plane (E_kk = -G_kk); its global source is C8P-O1"),
    "BULK4-O9": ("SUBSUMED", [(122, "1 - likely yes")], "C8P-O6", "time-delay theorems (H-DELAY-AS-CENSORSHIP)"),
    "BULK4-O10": ("SUBSUMED", [(127, "these are coefficients")], "C8P-O3", "G on the plane rides with k"),
    "BULK5-O1": ("SUBSUMED", [(101, "The mouths can be in separate universes")], "C8P-O1",
                 "the one-universe clause is dropped on M's path"),
    "BULK5-O2": ("OFF-PATH", [(94, "their is no movement in warp travel")], None, "a moving shape"),
    "BULK5-O3": ("OFF-PATH", [(94, "their is no movement in warp travel")], None,
                 "the normal stress a moving bubble's routes needed"),
    "BULK5-O4": ("OFF-PATH", [(94, "their is no movement in warp travel")], None, "above light strength"),
    "BULK5-O5": ("OFF-PATH", [(94, "their is no movement in warp travel")], None, "a moving bubble's residue"),
    "BULK5-O6": ("SUBSUMED", [(121, "we build it under closed index criteria")], "C8P-O1",
                 "Anderson's objection is C8P-O1's well-posedness"),
    "BULK5-O7": ("SUBSUMED", [(127, "these are coefficients")], "C8P-O3", "G_obs against G_N rides with k"),
    "BULK5-O8": ("SUBSUMED", [(121, "we build it under closed index criteria")], "C8P-O1",
                 "alternative bulks, READ only if the vacuum bulk fails"),
    # ---- the faithful copy (section 8n)
    "COPY-O1": ("INPUT", [(130, "read from the object being moved? - yes"),
                          (101, "Position 2 cannot know what identity completeness is beyond")], None,
                "what a person's README holds is the input N's content"),
    "COPY-O2": ("CARRIED", [(91, "Position 2 itself"), (101, "information is a form of energy")], None,
                "the recipe's size is the input N (item 130); the builder is position 2 by a field reaction, M's "
                "premise.  To the walls"),
    "COPY-O3": ("LIVE", [], "READ", "the read at position 1; RES-N2 decides whether a destroying read suffices"),
    "COPY-O4": ("LIVE", [], "READ",
                "a destination's composition: wall 7 (chain.py W7); position 2 builds with what it has (item 86 "
                "answer 7).  Proxima is the board's example"),
    "COPY-O5": ("RULED", [(131, "the throat size only needs to carry the binary information defining the object")],
                None, "the README defines the object; the site is not in it"),
    "COPY-O6": ("OFF-PATH", [(95, "Two places made one"),
                             (126, "it is realized in the same place the position 1 occupies")], None,
                "no route to shorten"),
    "COPY-O7": ("OFF-PATH", [(94, "their is no movement in warp travel"), (132, "as well as the throat? - yes")],
                None, "no port: the README is held in the throat and on the horizons"),
    "COPY-O8": ("RULED", [(90, "No device is need at position 2")], None, "no device at position 2, so no m_set"),
    "COPY-O9": ("CARRIED", [(111, "that and only that which is provided by the closing of the horizon"),
                            (90, "not by light")], None,
                "E_fab is the closing energy, your premise (RES-N1 checks it); no link; t_read stands with COPY-O3, "
                "t_build with RES-N4.  To the walls"),
    # ---- the whole chain under M's theory (section 8o)
    "C8O-O1": ("LIVE", [], "COMPUTE",
               "the joins through the throat, and where the APPARENT violation of the null condition sits on the plane "
               "(items 117, 120: never violated, only appears to be)"),
    "C8O-O2": ("LIVE", [], "COMPUTE", "the time-dependent geometry of items 109 and 115"),
    "C8O-O3": ("LIVE", [], "READ", "M carries universal entanglement (item 100); whether it gives geometry is READ"),
    "C8O-O4": ("LIVE", [(122, "The rules apply, but do not restrict information")], "READ",
               "wall 9.  Your item 122(4) answers it for information (H-RULES-NOT-INFORMATION, carried); the sources "
               "read in step 2 bound the information itself"),
    "C8O-O5": ("SUBSUMED", [(121, "we build it under closed index criteria")], "C8P-O1", "the global bulk"),
    "C8O-O6": ("CARRIED", [(111, "one energy read from two sides")], None,
               "M's accounting: one entangled state.  To the walls"),
    "C8O-O7": ("LIVE", [], "COMPUTE",
               "the trajectories set the corridor's length (items 116, 117); what length means on the r0 = 2m member"),
    "C8O-O8": ("LIVE", [], "READ", "a maximum power against an instantaneous opening (item 94)"),
    "C8O-O9": ("LIVE", [], "READ", "completeness (current.py X7 in part) and white-hole stability"),
    # ---- the bulk and the corridor fixed by its input (section 8p)
    "C8P-O1": ("LIVE", [], "READ", "the global bulk"),
    "C8P-O2": ("LIVE", [], "COMPUTE", "the coinciding junction"),
    "C8P-O3": ("LIVE", [], "READ", "k: measured bounds first, then item 127's current value"),
    "C8P-O4": ("LIVE", [], "M", "the ends of an open extra dimension (item 128)"),
    "C8P-O5": ("LIVE", [(132, "different views of the same object")], "COMPUTE",
               "r0 = 2m: stability and fine-tuning; item 132 bears on whether the chain's copies are one object"),
    "C8P-O6": ("LIVE", [], "READ", "a 5D censorship theorem"),
    "C8P-O7": ("LIVE", [], "COMPUTE", "rays leaving the plane"),
    "C8P-O8": ("LIVE", [], "M", "the passage readings' ray normalization"),
    "C8P-O9": ("LIVE", [(134, "Seat them and then compute E")], "M",
               "your one exact energy as E(N) at the bound.  Item 134 ordered E computed after the identification was "
               "reported; the board does not read an order to compute as a ruling on the identification"),
}


def _norm(s):
    return re.sub(r"\s+", " ", s).strip()


def ruling_items(path=RULINGS):
    """{item number: whitespace-normalized text of that item}."""
    items, cur, buf = {}, None, []
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^(\d+)\. \*\*", line)
            if m:
                if cur is not None:
                    items[cur] = _norm("".join(buf))
                cur, buf = int(m.group(1)), [line]
            elif line.startswith("## "):
                if cur is not None:
                    items[cur] = _norm("".join(buf))
                cur, buf = None, []
            elif cur is not None:
                buf.append(line)
    if cur is not None:
        items[cur] = _norm("".join(buf))
    return items


def ledger_rows():
    """[(list name, id, text)] from ledger.py's open lists, imported."""
    sys.path.insert(0, WD)
    import ledger  # noqa: E402
    out = []
    for name in OLDER_LISTS + FRONT_LISTS:
        for row in getattr(ledger, name):
            out.append((name, row[0], row[1]))
    return out


def ledger_source():
    with open(os.path.join(WD, "ledger.py"), encoding="utf-8") as f:
        return f.read()


def front_text():
    t = []
    for p in FRONT_OWNERS:
        with open(p, encoding="utf-8") as f:
            t.append(f.read())
    return "\n".join(t)


def check(D, rows, items, front, ledger_src, new_rows=NEW_ROWS):
    """Return a list of failures (empty when the audit holds)."""
    fails = []
    ids = [r[1] for r in rows]
    if len(set(ids)) != len(ids):
        fails.append("duplicate ids in the ledger's open lists")
    missing = sorted(set(ids) - set(D))
    extra = sorted(set(D) - set(ids))
    if missing:
        fails.append("rows with no disposition: %s" % ", ".join(missing))
    if extra:
        fails.append("dispositions for rows the ledger does not carry: %s" % ", ".join(extra))
    new_ids = {n[0] for n in new_rows}
    live = {k for k, v in D.items() if v[0] == "LIVE"} | new_ids
    for k, (kind, cites, tgt, note) in D.items():
        if kind not in KINDS:
            fails.append("%s: unknown kind %s" % (k, kind))
            continue
        if kind in ("RULED", "OFF-PATH", "SUBSUMED", "CARRIED", "INPUT") and not cites:
            fails.append("%s: %s with no ruling cited" % (k, kind))
        for it, q in cites:
            if it not in items:
                fails.append("%s: cites item %d, which the rulings do not hold" % (k, it))
            elif _norm(q) not in items[it]:
                fails.append("%s: item %d does not contain %r" % (k, it, q))
        if kind == "SUBSUMED" and tgt not in live:
            fails.append("%s: subsumed into %s, which is not a live row" % (k, tgt))
        if kind == "LIVE" and tgt not in ROUTES:
            fails.append("%s: LIVE with no route" % k)
        if kind == "OFF-CHAIN":
            if not tgt:
                fails.append("%s: OFF-CHAIN with no tag" % k)
            for tag in tgt or ():
                if tag in front:
                    fails.append("%s: tag %s appears in a front owner" % (k, tag))
                if tag not in ledger_src:
                    fails.append("%s: tag %s occurs nowhere in ledger.py (vacuous)" % (k, tag))
    for nid, q, route in new_rows:
        if route not in ROUTES:
            fails.append("%s: no route" % nid)
    return fails


def tally(D, new_rows=NEW_ROWS, only=None):
    from collections import Counter
    c = Counter(v[0] for k, v in D.items() if only is None or k in only)
    return c


def report(rows, D=D):
    older = [r[1] for r in rows if r[0] in OLDER_LISTS]
    front = [r[1] for r in rows if r[0] in FRONT_LISTS]
    print("residue.py -- every open row on the board against M's rulings (item 135, step 1)")
    print("  rows: %d (older waves %d, current front %d)" % (len(rows), len(older), len(front)))
    for label, ids in (("older waves", older), ("current front", front)):
        c = tally(D, only=set(ids))
        print("  %-14s " % label + "  ".join("%s %d" % (k, c[k]) for k in KINDS if c[k]))
    print()
    print("%-10s %-9s %-10s %s" % ("id", "kind", "to", "why"))
    for name, rid, _ in rows:
        kind, cites, tgt, note = D[rid]
        to = tgt if kind in ("SUBSUMED", "LIVE") else ("" if kind != "OFF-CHAIN" else "-")
        cs = ",".join(str(i) for i, _ in cites)
        print("%-10s %-9s %-10s %s%s" % (rid, kind, to or "", ("[item %s] " % cs) if cs else "", note))
    print()
    live = [k for k, v in D.items() if v[0] == "LIVE"]
    print("LIVE after the audit: %d rows + %d new" % (len(live), len(NEW_ROWS)))
    for route in ROUTES:
        ks = [k for k in live if D[k][2] == route] + [n[0] for n in NEW_ROWS if n[2] == route]
        print("  %-8s %s" % (route, ", ".join(ks)))
    print("CARRIED (to the walls): %s" % ", ".join(k for k, v in D.items() if v[0] == "CARRIED"))
    print("INPUT: %s" % ", ".join(k for k, v in D.items() if v[0] == "INPUT"))
    print()
    for nid, q, route in NEW_ROWS:
        print("%s [%s] %s" % (nid, route, q))


def selftest():
    items = ruling_items()
    rows = ledger_rows()
    front = front_text()
    lsrc = ledger_source()
    ok = 0
    n = 0

    def chk(name, cond):
        nonlocal ok, n
        n += 1
        ok += bool(cond)
        print("  [%s] %s" % ("ok" if cond else "FAIL", name))

    fails = check(D, rows, items, front, lsrc)
    for f in fails:
        print("    " + f)
    chk("the audit holds: one disposition per open row, every cited ruling quoted at source", not fails)
    chk("the ledger carries 106 open rows, 79 of them older-wave", len(rows) == 106 and
        sum(r[0] in OLDER_LISTS for r in rows) == 79)
    chk("the rulings hold items 1-135 without a gap", sorted(items) == list(range(1, 136)))
    # controls: each mutation must be caught
    bad = dict(D)
    k, (kind, cites, tgt, note) = "COPY-O8", D["COPY-O8"]
    bad[k] = (kind, [(90, "A device is needed at position 2")], tgt, note)
    chk("control: a misquoted ruling is caught", any("does not contain" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    del bad["W4-O3"]
    chk("control: a dropped row is caught", any("no disposition" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["S1B-O7"] = ("SUBSUMED", D["S1B-O7"][1], "S1C-O2", "")
    chk("control: a row subsumed into a closed row is caught",
        any("not a live row" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["CMB2-O1"] = ("OFF-CHAIN", [], ("H-ONE-EXACT-ENERGY",), "")
    chk("control: an OFF-CHAIN tag the front uses is caught",
        any("appears in a front owner" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["COPY-O8"] = ("RULED", [(136, "x")], None, "")
    chk("control: a cite to a ruling not yet given is caught",
        any("do not hold" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["W4-O3"] = ("DROPPED", D["W4-O3"][1], None, "")
    chk("control: an unknown kind is caught", any("unknown kind" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["W4-O3"] = ("OFF-PATH", [], None, "")
    chk("control: a closure with no ruling cited is caught",
        any("no ruling cited" in f for f in check(bad, rows, items, front, lsrc)))
    bad = dict(D)
    bad["C8P-O7"] = ("LIVE", [], None, "")
    chk("control: a live row with no route is caught", any("no route" in f for f in check(bad, rows, items, front, lsrc)))
    chk("control: a duplicated ledger row is caught",
        any("duplicate" in f for f in check(D, rows + rows[:1], items, front, lsrc)))
    bad = dict(D)
    bad["CMB2-O1"] = ("OFF-CHAIN", [], ("H-CONTRCT",), "")
    chk("control: a misspelt OFF-CHAIN tag is caught (vacuity)",
        any("vacuous" in f for f in check(bad, rows, items, front, lsrc)))
    print("selftest: %d/%d (%d controls)" % (ok, n, 10))
    return ok == n


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    rows = ledger_rows()
    fails = check(D, rows, ruling_items(), front_text(), ledger_source())
    if fails:
        print("\n".join(fails))
        sys.exit(1)
    report(rows)
