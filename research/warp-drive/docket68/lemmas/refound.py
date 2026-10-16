#!/usr/bin/env python3
"""refound.py -- item 441: the re-foundation program, put to M before any of it is run (414).  Under 441 M's rulings
are not first principles and each definition must be proved; pass_audit P5 finds three rows passing (I2, R3, Z3a).
This instrument inventories the 62 rulings that the other rows name among their premises (pass_audit's RULED), sorts
each by what would prove it, and counts which rows each kind gates.  Labels: deduced (every class is the board's
reading, put to M), M's (the rulings), computed (the counts).  Worked in the conversation; not verified; not seated.

  F0 (read) M's words, verbatim: 441's "1 - no" and "2 - no. Each definition must be proved"; 414's "let's discuss the
     approach as to not spend days failing".
  F1 (deduced) Three kinds.
     S -- a specification: what the device or the theorem is to do (the README sizes the throat, one exact energy, the
          passage one way, the planes coincident, ...).  It is part of what the theorem claims, not a premise about
          nature.  Proved by realizability: a solution of established physics, computed, that meets it, with no
          contradiction of established law or measurement.
     N -- a statement about nature (everything entangled, information as energy triggering a field, the null condition
          kept as a pair, every plane with our structure, ...).  Proved only by derivation from established physics,
          computed.  Where established physics does not contain it, a row resting on it cannot pass unless re-derived
          without it.
     P -- process, scope or confirmation ("for the math", a direction to read, a reading of the board's confirmed, an
          assumption).  Not content: dropped as a premise.  A confirmed reading is the board's, and is proved as the
          board's; an assumption (422) is replaced by computation.
  F2 (computed) Every ruling in RULED is classed; the counts by kind; the rows each kind gates.
  F3 (deduced; flags) Where the standard cannot be met by established physics as it stands:
     (a) 273, the quantum bounce: a black-to-white tunnelling model (Haggard-Rovelli), quantum gravity, outside
         established physics; ten rows rest on it.  Realizable only in that model, not by a solution of established
         physics: classically Penrose's theorem forbids the continuation without giving up a condition.
     (b) B6', our universe a plane in a five-dimensional bulk: established physics contains no fifth dimension, so B6'
         can be proved consistent, realizable and in agreement with measurement -- not derived as true.
     (c) RECON's "any position 2": the reconstructible region (433, bearing26 G4) is computed; outside it the labels
         do not build.  RECON is provable inside it, not for every position 2.
     (d) The ten N rulings, none in established physics as stated: 100 (QFT's vacuum is entangled across every
         pair of regions -- Reeh-Schlieder, standard -- a candidate derivation of a weaker form), 183's pair (quantum
         fields can make null energy negative locally; the averaged condition holds on complete achronal geodesics,
         standard -- a candidate for a weaker form), 86, 109, 122, 140, 155, 177, 202, 320.  [101's answers 3-4 and
         432's "information is energy" are N too (Landauer prices erasing a bit at kT ln2; it does not make
         information an energy), but the rows use 101's answers 1 and 6 and 432's specification, not those parts.]
  F4 (deduced) The order: B6' first (it gates 71 rows, the two deferred among them); then R0, R1, R2, R6 and
     RECON; then the S rulings by the rows they gate; then the N rulings, derived or set aside; B7 by the bulk's geometry (its N premises 86, 100, 122, 140
     dropped: before the opening the warped Vaidya bulk of settle_arrival A4 is the vacuum, horizon-free, computed);
     O1b and O1c by computing the large-end core (the approved approach).

python3 refound.py [--selftest | --mutants]
"""
import collections
import importlib.util
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ("1 - no", "2 - no. Each definition must be proved", "let's discuss the approach as to not spend days failing")

# F1: each ruling's kind and what in it the rows use (the board's reading, put to M)
KIND = {
    86: ("N", "answer 3: natural throats common and regular occurrences"),
    100: ("N", "everything entangled with everything until refuted"),
    101: ("S", "answers 1 and 6: a corridor made under the conditions of a larger one; the device widens the "
               "corridor to the README's size, no more and no less [answers 3-4, information as energy, N, unused]"),
    109: ("N", "a horizon cannot exist without its object"),
    110: ("S", "the closing hold's energy goes into position 2"),
    111: ("S", "the build uses exactly the closing energy [(b), one energy read from two sides, N]"),
    122: ("N", "censorship likely binds the bulk; the two sides time-reversed images; ER=EPR's reach"),
    127: ("S", "the planes coincide in the extra dimension"),
    131: ("S", "the throat sized by the README's shortest exact binary form"),
    132: ("S", "the horizons hold the README; one way by nature"),
    133: ("S", "one exact energy for any given README"),
    136: ("S", "released at position 2 at the closing; one fixed exact encoding"),
    137: ("S", "the passage's exact entanglement is N bits"),
    139: ("S", "position 2's plane and ours; the energy positive, to be proved; the information the trigger"),
    140: ("N", "k dependent on the work; position 2's plane entangled with ours"),
    146: ("S", "no tolerance; the encoding written in what every universe shares"),
    147: ("S", "the copy's motion not in the README; labels and values both"),
    148: ("S", "position 2's matter rearranges to the README, then its laws govern"),
    155: ("N", "the rest of E absorbed by position 2's expansion"),
    158: ("S", "the hold lasts as long as the write needs"),
    160: ("S", "the corridor and the opening one object"),
    162: ("S", "one black-hole-like object, of the README's size, holding it once and at once"),
    163: ("S", "'at once' is all together, one whole"),
    166: ("S", "the corridor spans both planes"),
    177: ("N", "negative null energy from coupling the entangled ends is the appearance"),
    179: ("S", "the corridor exclusive to the bulk"),
    183: ("N", "the null condition never violated, as a pair along each ray"),
    198: ("S", "the README forms the corridor (M's guess)"),
    200: ("S", "position 2's plane counted once"),
    201: ("S", "our universe defined by its plane's tension and its dark-energy offset -- B6'"),
    202: ("N", "every plane with our structure and definitions, perhaps different values"),
    226: ("S", "each position 2 carries its own universe's values"),
    229: ("S", "the destination a position 2 like 2a-2P"),
    230: ("S", "the bulk does all the work; position 2 absorbs the energy read at position 1"),
    239: ("S", "the build's need is what the closing energy activates"),
    240: ("S", "the copy built under position 2's laws; its mass position 2's"),
    259: ("P", "scope: the hole's interior singularity admitted under 232 (e)"),
    270: ("S", "the passage one-way only"),
    273: ("S", "the one object's continuation a quantum bounce to position 2 [flag (a)]"),
    275: ("S", "the planes coincident everywhere"),
    276: ("S", "the passage one-way in all aspects"),
    277: ("S", "the passage one-way only, again"),
    282: ("S", "C1, C4, C5, C7 re-posed one-way; B7's join through the bulk with no horizons"),
    284: ("S", "the room: the rebuilt content, displacing, staying"),
    285: ("S", "an exact copy obeying position 2's laws; the room the new whole"),
    318: ("P", "273 against 183: for the math"),
    320: ("N", "no bulk is ever empty [the order to prove the pointwise condition, P]"),
    322: ("P", "direction: read the vacuum decay boundary and the Higgs mass"),
    328: ("P", "confirmation: the board's reading M-ONE-LIGHT-CONE"),
    334: ("P", "confirmation: the board's reading H-HOLD-IS-THE-FACE"),
    336: ("S", "the energy stays in our universe; our face closes by Hawking emission"),
    340: ("S", "for the math, with M's guess: the README forms the face as it arrives"),
    353: ("P", "confirmation: the board's reading H-PLANCK-ENDS (regularity asked below the Planck curvature)"),
    386: ("S", "what crosses is information, not matter"),
    390: ("S", "position 2's face closes when the corridor holds nothing"),
    414: ("P", "process: proof first, the computation discussed before it runs"),
    422: ("P", "assumption H-CORE-DELIVERS, to be replaced by computing the core (approved at 441)"),
    426: ("S", "the write long; the object standing from the opening"),
    427: ("S", "a destination of any tension reachable"),
    432: ("S", "the energy is the README, there at the opening; exact, on a navigational lattice [information as "
               "'energy in the form of a binary interaction', N]"),
    437: ("S", "reconstruction obeys position 2's 26 -- RECON"),
    438: ("S", "the geometry as labels; the isotope out, the last state in [the delivery for the math, P]"),
}
FLAGGED_N = tuple(n for n, (c, _) in KIND.items() if c == "N")      # F3 (d)
DEFS = {"B6'": "an exact plane of tension sigma with its offset in an anti-de Sitter bulk (a de Sitter plane), its "
               "four-dimensional G and Lambda by the effective equations, matched to measurement with ell inside "
               "the table-top bound; a smooth wall realising it (b5b_wall's construction, de Sitter sliced)",
        "R0": "the README's energy as a null shell forming the face of its size (settle_arrival A2, A4; b4d_large "
              "K12), N a function of the README (encode_labels C0-C7)",
        "R1": "exact decoding of the labels (encode_labels); no-cloning not crossed, the read destroying (136)",
        "R2": "the labelled structures exist under position 2's laws (p2_matter's atoms and solids under three laws)",
        "R6": "displacement's work inside the energy the build is given (the ledger, E3)",
        "RECON": "the labels built under a position 2's 26 -- inside the reconstructible region only [flag (c)]"}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def ruled():
    return _load(os.path.join(HERE, "pass_audit.py"), "rf_pa").RULED


def kinds():
    k = dict(KIND)
    if "drop" in MUT:
        k.pop(273)
    if "bounce_P" in MUT:
        k[273] = ("P", k[273][1])
    return k


def gates(R, k):
    """for each kind, the rows naming a ruling of it; and the rows naming 273, and a flagged N"""
    by = collections.defaultdict(set)
    for row, ns in R.items():
        for n in ns:
            by[k[n][0] if n in k else "?"].add(row)
    bounce = sorted(r for r, ns in R.items() if 273 in ns)
    flagged = sorted(r for r, ns in R.items() if set(ns) & set(FLAGGED_N))
    only_s = sorted(r for r, ns in R.items() if all(k.get(n, ("?",))[0] in ("S", "P") for n in ns))
    return by, bounce, flagged, only_s


def report():
    R, k = ruled(), kinds()
    used = sorted({n for ns in R.values() for n in ns})
    cnt = collections.Counter(k[n][0] for n in used if n in k)
    print("F0 M's words:", words())
    print("F2 %d rulings named as premises: %s" % (len(used), ", ".join("%s %d" % kv for kv in sorted(cnt.items()))))
    for kind in "SNP":
        print("  %s:" % kind)
        for n in used:
            if k.get(n, ("?",))[0] == kind:
                print("    %3d  %s" % (n, k[n][1]))
    by, bounce, flagged, only_s = gates(R, k)
    print("F3 (a) rows on 273's bounce (%d): %s" % (len(bounce), ", ".join(bounce)))
    print("F3 (d) rows naming an N ruling (%d): %s" % (len(flagged), ", ".join(flagged)))
    print("F4 rows whose rulings are all S or P (%d) -- these pass once B6' and their S rulings are proved realizable"
          % len(only_s))
    print("     " + ", ".join(only_s))
    print("F4 each definition, how it would be proved:")
    for d, how in DEFS.items():
        print("    %-6s %s" % (d, how))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    R, k = ruled(), kinds()
    used = {n for ns in R.values() for n in ns}
    r = words(); ok.append(r); say("F0 words: %s" % r)
    r = used <= set(k) and len(used) == 62; ok.append(r); say("F2 all 62 rulings classed: %s" % r)
    cnt = collections.Counter(k[n][0] for n in used if n in k)
    r = set(cnt) == {"S", "N", "P"} and sum(cnt.values()) == 62; ok.append(r)
    say("F2 three kinds, %s: %s" % (dict(sorted(cnt.items())), r))
    by, bounce, flagged, only_s = gates(R, k)
    r = len(bounce) == 10 and k[273][0] == "S"; ok.append(r)
    say("F3 (a) ten rows rest on 273's bounce, classed S and flagged: %s" % r)
    r = len(FLAGGED_N) == 10 and not set(flagged) & set(only_s); ok.append(r)
    say("F3 (d) ten N rulings; no row both all-S and on an N: %s" % r)
    r = set(DEFS) == {"B6'", "R0", "R1", "R2", "R6", "RECON"}; ok.append(r); say("F4 each definition planned: %s" % r)
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("drop", "bounce_P"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-9s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/2 caught" % caught)
    return caught == 2


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
