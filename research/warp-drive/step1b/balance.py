#!/usr/bin/env python3
"""
balance.py -- Step 1b, the balanced equation, as M defined it.

Not seated.  Nothing here edits the board: every figure is IMPORTED from the instrument that owns it (measure, seat,
transit, massform, stock, nopath), never retyped.  It reads the research tree and writes nothing.

    python3 balance.py              report
    python3 balance.py --selftest   checks, with CONTROLS (cases built to fail, which must fail) and STRUCTURAL
                                    items (true by construction: printed, never counted)
    python3 balance.py --json       the equation's rows as JSON

M'S DEFINITION (docket68/M-RULINGS-2026-10-03.md items 29-30, verbatim)
  29. "Balanced means that the value of the object at first position must equal the value of the object at the second
      position. And any variable input must be accounted for in output".
  30. Asked what makes up that value, M: "Information only".

So the equation is
      I(A, before)  =  I(B, after)                                                         [the value]
with every variable input -- all matter and energy, at A, at B and in the channel -- appearing in an output term.

WHAT IT COMPUTES
  (1) The value, I.  The object is the board's 70 kg payload (stock.HUMAN).  I is counted four ways, each under the
      hypotheses measure.py names (species sequence, 1 A grid, 0.1 A grid, thermal entropy): measure.price_table,
      imported.  Which count is "the object's definable condition information" is not fixed by M's words, so all four
      are carried (H-WHICH-COUNT).
  (2) Whether the value balances, on two readings of how I is carried:
        R-CLASSICAL  I is a classical description: I bits sent; a classical record can be copied, so I(A) does NOT
                     fall to zero by sending it -- the instance at A must be retired as an OUTPUT term if the object
                     is to be at one position only (M: "It is either at the beginning or end position, never in
                     between them").
        R-QUANTUM    I is carried as quantum state (teleportation; transit.py, imported): 2 classical bits per qubit
                     and 1 pre-shared ebit per qubit.  COMPUTED here over random states with transit.teleport: B's
                     fidelity is 1 with the bits, A's four outcomes are equiprobable whatever the state (so the record
                     alone holds no I about it), and with the bits withheld B's fidelity is 1/2 for every state (B
                     holds I/2; a CONTROL: the value does not balance without the channel).  What teleportation moves is STATE; the atoms at A
                     stay atoms of the same species (transit.CARRIES_SUBSTANCE = False), so the CLASSICAL part of I
                     (the species sequence) is not retired at A by teleporting -- on this reading too, A's instance
                     leaves only through an output term.
  (3) The equation's terms, each with its side (INPUT / OUTPUT), site (A, B, channel), what it is, its value where an
      instrument computes one, its status (COMPUTED, READ via its owner, OPEN), and -- for every input -- the output
      term(s) that account for it.  Every input must be accounted for in output (M, item 29): checked, with a CONTROL
      that drops an output and must fail.
  (4) The conserved quantities as a CONSISTENCY column, not as the value (M: "Information only"): the object's mass
      number (approximated by M/u, H-BARYON-BY-MASS), its electrons (sum of N_e Z_e, Z READ via massform.Z_OF) and its
      charge (0, neutral atoms).  The column closes SITE BY SITE with zero transfer between A and B: A's matter stays at
      A as its residue; B's object is built from B's stock -- so on M's definition no conserved quantity crosses, only
      I does.  The closure at B is exactly D25's stock gate (seat.py): B's stock must hold every element of the object
      (H-SAME-COMPOSITION); isotope ratios differing between A's object and B's stock leave a mass-energy difference
      this file does not compute (H-SAME-ISOTOPES, OPEN).
  (5) What the equation does NOT total.  The energy column has OPEN terms -- reading I at A, retiring A's instance,
      assembling at B (E_rec, OPEN in seat.py) -- so no total energy is printed, and none may be quoted.  The channel's
      energy is priced per schedule only (seat.channel_floor: it falls as the schedule lengthens; S5's transfer has no
      energy floor independent of T), and the erasure terms are floors that apply only if a record is erased (a kept
      record is the output instead).

NAMED HYPOTHESES (every limitation carried by name)
  H-WHICH-COUNT     which of measure.py's four counts is the object's information is not fixed; all four carried.
  H-INFO-SHAPE      (M, item 1) teleportation carries "non physical properties/bounds that give shape to the geometry at
                    the seat"; the substance comes "from the seat" (item 5).  Adopted, as on the board.
  H-SAME-COMPOSITION B's stock supplies the object's elements in the object's proportions (the D25 gate, OPEN at
                    Proxima: seat.P_MEASURED_IN_PROXIMA_SYSTEM = False).
  H-SAME-ISOTOPES   the stock's isotope ratios equal the object's; otherwise a mass-energy difference, not computed.
  H-BARYON-BY-MASS  mass number approximated by M/u (binding and the n-p mass difference make it inexact at the
                    per-cent level); the column's closure does not depend on the approximation (it is site-local).
  H-RESET           B's fabricator register is reset before writing; only then is its erasure an output (Landauer).
  H-ERASE-RECORD    the measurement record (R-QUANTUM, 2 bits per qubit) is erased; otherwise it is kept, as an output.
  H-RETIRE-A        (M, item 32: "I suspect so, to satisfy the no-cloning clause.") A's instance is retired into stock
                    at A (OUT-A-RESIDUE).  Computed beside it (no_cloning): no-cloning binds the QUANTUM state, which
                    teleportation already leaves nowhere at A; it does not bind the CLASSICAL description, which copies
                    freely -- so retiring A's matter is what keeps the classical part at one position.
  H-ONE-POSITION    (M) "The two positions technically exist as one" -- carried as M's hypothesis.  The board's own
                    reading of the channel (transit.BEATS_LIGHT = False: the classical bits arrive no earlier than D/c)
                    is recorded beside it, not graded: M, "speed is not a question in my work".
"""
import contextlib
import io
import json
import math
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WD = os.path.abspath(os.path.join(HERE, ".."))
for _p in (WD, os.path.join(WD, "docket68")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

with contextlib.redirect_stdout(io.StringIO()):
    import measure
    import seat
    import transit
    import massform
    import stock
    import nopath

LN2 = math.log(2.0)
M_WORDS_29 = ("Balanced means that the value of the object at first position must equal the value of the object at "
              "the second position. And any variable input must be accounted for in output")
M_WORDS_30 = "Information only"
M_WORDS_32 = "I suspect so, to satisfy the no-cloning clause."
RULINGS_FILE = os.path.join(WD, "docket68", "M-RULINGS-2026-10-03.md")
T_A = measure.T_BODY            # H-TBODY, measure.py's: the object's own temperature at A
T_FLOOR = nopath.T_CMB          # the coldest bath the board holds: a floor on any erasure at B
SCHEDULES_S = (3.15576e7, 3.15576e9)   # one year, a hundred years (Julian, s): the channel is priced per schedule


# ============================================================================ (1) the value
def counts():
    """[(count name, bits)] from measure.price_table, imported."""
    rows, _, _, _ = measure.price_table()
    return [(r["count"], r["bits"]) for r in rows]


# ============================================================================ (2) does the value balance?
def _rand_state(rng):
    a, b = complex(rng.gauss(0, 1), rng.gauss(0, 1)), complex(rng.gauss(0, 1), rng.gauss(0, 1))
    n = math.sqrt(abs(a) ** 2 + abs(b) ** 2)
    return [a / n, b / n]


def quantum_value_balance(trials=400, seed=1):
    """Over random qubit states, with transit.teleport (imported):
       fid_min       B's least fidelity WITH the two bits (the value balances iff this is 1);
       p_dev_max     the largest deviation of any outcome probability from 1/4 (0 -> the record alone holds no I);
       fid_nobits    B's fidelity with the bits WITHHELD: 1/2 for every state, since B then holds I/2 (the value
                     does not balance without the channel).  First written expecting 2/3 -- that is the best
                     measure-and-prepare fidelity, a different quantity; the check caught it."""
    rng = random.Random(seed)
    fmin, pdev, fnb, fnb_dev = 1.0, 0.0, 0.0, 0.0
    for _ in range(trials):
        psi = _rand_state(rng)
        out = transit.teleport(psi, send_bits=True)
        fmin = min(fmin, sum(p * transit.fidelity(psi, v) for p, v in out))
        pdev = max(pdev, max(abs(p - 0.25) for p, _ in out))
        f0 = sum(p * transit.fidelity(psi, v) for p, v in transit.teleport(psi, send_bits=False))
        fnb += f0
        fnb_dev = max(fnb_dev, abs(f0 - 0.5))
    return {"trials": trials, "fid_min_with_bits": fmin, "p_dev_max_from_quarter": pdev,
            "fid_mean_bits_withheld": fnb / trials, "fid_bits_withheld_dev_max_from_half": fnb_dev}


# ============================================================================ (4) the conserved-quantity column
def object_conserved():
    """The object's mass number (M/u, H-BARYON-BY-MASS), electrons (sum N_e Z_e) and charge, from measure.atom_counts
    and massform.Z_OF (READ, AME2020) -- the CONSISTENCY column, not the value."""
    N, M = measure.atom_counts()
    electrons = sum(n * massform.Z_OF[e] for e, n in N.items())
    return {"kg": M, "atoms": sum(N.values()), "mass_number_approx": M / massform.U_KG, "electrons": electrons,
            "protons": electrons, "charge_e": 0.0, "rest_energy_J": massform.rest_energy_j()}


def conserved_closure():
    """Site by site.  A: object in = residue out.  B: stock incorporated = object out (H-SAME-COMPOSITION).
    Transfer A -> B for each quantity: 0.  Returned per quantity as (in_A, out_A, in_B, out_B, transfer)."""
    o = object_conserved()
    rows = {}
    for q in ("kg", "mass_number_approx", "electrons", "protons", "charge_e"):
        rows[q] = {"A_in": o[q], "A_out_residue": o[q], "B_in_stock": o[q], "B_out_object": o[q], "A_to_B": 0.0}
    return rows


# ============================================================================ (3) the equation
def stock_terms():
    ci = stock.feedstock_kg(massform.PAYLOAD_KG, stock.HUMAN, seat.stockgate.DESTS["CI chondrite"]())
    binder = seat.binders()["CI chondrite"][0]
    return {"ci_feedstock_kg": ci, "ci_residue_kg": ci - massform.PAYLOAD_KG, "ci_binder": binder,
            "P_measured_in_proxima_system": seat.P_MEASURED_IN_PROXIMA_SYSTEM}


def equation(bits, reading):
    """The terms for one count (bits) on one reading ('R-CLASSICAL' / 'R-QUANTUM').  Each term:
    (id, side, site, what, value, unit, status, accounts_for)."""
    o = object_conserved()
    s = stock_terms()
    sent = bits if reading == "R-CLASSICAL" else 2.0 * bits
    ch = [seat.channel_floor(sent, T) for T in SCHEDULES_S]
    t = [
        ("IN-A-OBJECT", "INPUT", "A", "the object at A: value I(A) and its matter (%.4g kg, %.4g J rest energy)"
         % (o["kg"], o["rest_energy_J"]), bits, "bits", "COMPUTED (measure.price_table)", ()),
        ("IN-A-READ", "INPUT", "A", "energy to read I at A", None, "J",
         "OPEN: theorem floor 0, probe floors by carrier under H-PROBE (terms.py T1); no single value", ()),
        ("IN-B-STOCK", "INPUT", "B", "stock consumed at B: CI-chondrite feedstock for the object (binder %s)"
         % s["ci_binder"][0], s["ci_feedstock_kg"], "kg",
         "COMPUTED (stock.feedstock_kg); the gate at Proxima OPEN (P measured: %s)" % s["P_measured_in_proxima_system"],
         ()),
        ("IN-B-ASSEMBLE", "INPUT", "B", "energy to assemble the object at B (E_rec)", None, "J",
         "OPEN (seat.py: E_rec OPEN; its payback ceiling is seat.erec_ceiling); chemistry bounded and placement "
         "OPEN in terms.py T3", ()),
        ("IN-CHANNEL", "INPUT", "channel", "bits sent (%s)" % ("I" if reading == "R-CLASSICAL" else "2 per qubit"),
         sent, "bits", "COMPUTED", ()),
        ("IN-CHANNEL-E", "INPUT", "A->B", "channel energy, emitted at A; the floor is on what B receives, per "
         "schedule (1D one-polarisation, seat.channel_floor): %s" % ", ".join("%.3g J in %.3g s" % (c["E_1d_one_pol_J"], c["T_s"]) for c in ch),
         ch[0]["E_1d_one_pol_J"], "J", "COMPUTED per schedule (no floor independent of T)", ()),
    ]
    if reading == "R-QUANTUM":
        t.append(("IN-EBITS", "INPUT", "A and B", "pre-shared ebits, one per qubit, consumed by use "
                  "(transit.CHANNEL_IS_CONSUMED_BY_USE = %s)" % transit.CHANNEL_IS_CONSUMED_BY_USE, bits, "ebits",
                  "COMPUTED", ()))
    t += [
        ("OUT-B-OBJECT", "OUTPUT", "B", "the object at B: value I(B) = I(A), its matter from B's stock", bits, "bits",
         "the value balances: see (2)", ("IN-A-OBJECT", "IN-CHANNEL", "IN-B-STOCK", "IN-B-ASSEMBLE")
         + (("IN-EBITS",) if reading == "R-QUANTUM" else ())),
        ("OUT-A-RESIDUE", "OUTPUT", "A", "A's matter, retired as stock at A (%.4g kg): the instance at A leaves only "
         "through this term, on both readings" % o["kg"], o["kg"], "kg",
         "COMPUTED mass; energy to retire it OPEN (bounded, and dissolved by a photon or electron read under "
         "H-PROBE/H-ABSORB: terms.py T2); carried under H-RETIRE-A (M, item 32)",
         ("IN-A-OBJECT", "IN-A-READ")),
        ("OUT-B-RESIDUE", "OUTPUT", "B", "stock processed and not incorporated", s["ci_residue_kg"], "kg",
         "COMPUTED (stock.feedstock_kg - payload)", ("IN-B-STOCK",)),
        ("OUT-B-HEAT", "OUTPUT", "B", "heat from resetting B's register before writing I (H-RESET): >= %.3g J at %.4g "
         "K" % (measure.landauer_j(bits, T_FLOOR), T_FLOOR), measure.landauer_j(bits, T_FLOOR), "J",
         "COMPUTED floor (measure.landauer_j) under H-RESET", ("IN-B-ASSEMBLE",)),
        ("OUT-CHANNEL", "OUTPUT", "B", "the channel's energy, absorbed at B", ch[0]["E_1d_one_pol_J"], "J",
         "COMPUTED per schedule", ("IN-CHANNEL-E", "IN-CHANNEL")),
    ]
    if reading == "R-QUANTUM":
        t.append(("OUT-A-RECORD", "OUTPUT", "A", "the measurement record, 2 bits per qubit: kept, or erased with >= "
                  "%.3g J at %.4g K (H-ERASE-RECORD)" % (measure.landauer_j(sent, T_A), T_A), sent, "bits",
                  "COMPUTED; erasure floor measure.landauer_j", ("IN-CHANNEL",)))
        t.append(("OUT-EBITS", "OUTPUT", "A and B", "the ebits, consumed: left as A's Bell-measured pairs and B's "
                  "corrected qubits", bits, "ebits", "COMPUTED", ("IN-EBITS",)))
    else:
        t.append(("OUT-A-COPY", "OUTPUT", "A", "the classical description kept at A after sending (a classical "
                  "record can be copied): retired with OUT-A-RESIDUE, or erased (>= %.3g J at %.4g K)"
                  % (measure.landauer_j(bits, T_A), T_A), bits, "bits",
                  "COMPUTED; erasure floor measure.landauer_j", ("IN-A-OBJECT", "IN-CHANNEL")))
    return t


def unaccounted(terms):
    """Inputs that no output term accounts for (M, item 29: 'any variable input must be accounted for in output')."""
    covered = {a for x in terms if x[1] == "OUTPUT" for a in x[7]}
    return [x[0] for x in terms if x[1] == "INPUT" and x[0] not in covered]


def open_terms(terms):
    return [x[0] for x in terms if x[6].startswith("OPEN")]


def energy_total(terms):
    """None whenever any energy term is OPEN: the equation refuses to total what it cannot compute."""
    e = [x for x in terms if x[5] == "J"]
    if any(x[4] is None for x in e):
        return None
    return sum(x[4] for x in e if x[1] == "INPUT") - sum(x[4] for x in e if x[1] == "OUTPUT")


def no_cloning(trials=400, seed=3):
    """What no-cloning binds, and what it does not.
      quantum: a unitary preserves inner products, so cloning |psi> and |phi> needs <psi|phi> = <psi|phi>^2, true only
               when |<psi|phi>| is 0 or 1 (Wootters-Zurek).  Over random pairs: the least gap ||<psi|phi>| -
               |<psi|phi>|^2| (> 0: no single unitary clones both) -- and teleportation already leaves A with no
               information about psi (quantum_value_balance: outcomes equiprobable).
      classical: CNOT onto a blank |0> copies each basis state exactly (fidelity 1): a classical record copies freely,
               so no-cloning does not bind the species sequence."""
    rng = random.Random(seed)
    gap = 1.0
    for _ in range(trials):
        a, b = _rand_state(rng), _rand_state(rng)
        ov = abs(a[0].conjugate() * b[0] + a[1].conjugate() * b[1])
        gap = min(gap, abs(ov - ov * ov))
    # CNOT |x>|0> = |x>|x> for x in {0, 1}: on basis vectors of C^4 ordered |00>,|01>,|10>,|11>
    cnot = {0: 0, 1: 1, 2: 3, 3: 2}
    copies = [cnot[2 * x + 0] == 2 * x + x for x in (0, 1)]
    return {"trials": trials, "least_overlap_gap": gap, "cnot_copies_basis_states": copies}


def m_words_present():
    with open(RULINGS_FILE, encoding="utf-8") as fh:
        text = " ".join(fh.read().split())
    return M_WORDS_29 in text, ('M: "%s"' % M_WORDS_30) in text, M_WORDS_32 in text


def collect():
    qv = quantum_value_balance()
    out = {"m_words": {"29": M_WORDS_29, "30": M_WORDS_30, "32": M_WORDS_32, "present": m_words_present()},
           "no_cloning": no_cloning(),
           "value_counts": counts(), "quantum_value_balance": qv,
           "conserved": object_conserved(), "closure": conserved_closure(), "stock": stock_terms(),
           "board_channel_reading": {"BEATS_LIGHT": transit.BEATS_LIGHT, "CARRIES_SUBSTANCE": transit.CARRIES_SUBSTANCE,
                                     "IT_IS_A_MOVE_NOT_A_COPY": transit.IT_IS_A_MOVE_NOT_A_COPY},
           "equations": {}}
    for name, bits in counts():
        for r in ("R-CLASSICAL", "R-QUANTUM"):
            t = equation(bits, r)
            out["equations"]["%s | %s" % (name, r)] = {
                "terms": [dict(zip(("id", "side", "site", "what", "value", "unit", "status", "accounts_for"), x))
                          for x in t],
                "unaccounted_inputs": unaccounted(t), "open_terms": open_terms(t), "energy_total": energy_total(t)}
    return out


def report():
    d = collect()
    print("Step 1b -- the balanced equation (M, items 29-30)")
    print('  M: "%s"' % M_WORDS_29)
    print('  M, on the value: "%s"   (both quotations found in the rulings file: %s)' % (M_WORDS_30, d["m_words"]["present"]))
    print("\n  I(A, before) = I(B, after); every input accounted for in an output.\n")
    print("(1) The value I, four counts (measure.price_table; H-WHICH-COUNT):")
    for n, b in d["value_counts"]:
        print("    %-42s %.4g bits" % (n, b))
    q = d["quantum_value_balance"]
    print("\n(2) Does the value balance?  R-QUANTUM, transit.teleport over %d random states:" % q["trials"])
    print("    B's least fidelity with the bits: %.12f   outcome probabilities' largest deviation from 1/4: %.2e"
          % (q["fid_min_with_bits"], q["p_dev_max_from_quarter"]))
    print("    bits withheld: B's fidelity %.12f for every state (largest deviation from 1/2: %.2e) -- no balance "
          "without the channel" % (q["fid_mean_bits_withheld"], q["fid_bits_withheld_dev_max_from_half"]))
    print("    R-CLASSICAL: a classical record copies, so I(A) does not fall by sending; on both readings A's instance")
    print("    leaves only through an output term (teleportation moves state, not species: CARRIES_SUBSTANCE = %s)"
          % d["board_channel_reading"]["CARRIES_SUBSTANCE"])
    nc = d["no_cloning"]
    print('    M, item 32: "%s"  (H-RETIRE-A)' % M_WORDS_32)
    print("    no-cloning binds the QUANTUM part: least overlap gap over %d random pairs %.3g > 0, and teleportation"
          % (nc["trials"], nc["least_overlap_gap"]))
    print("    already leaves A no information about the state; it does NOT bind the CLASSICAL part (CNOT copies basis")
    print("    states: %s) -- retiring A's matter is what keeps the classical description at one position"
          % nc["cnot_copies_basis_states"])
    c = d["conserved"]
    print("\n(4) Conserved quantities -- a consistency column, not the value:")
    print("    object: %.4g kg, %.4g atoms, mass number ~ %.4g (H-BARYON-BY-MASS), %.4g electrons, charge 0, %.4g J"
          % (c["kg"], c["atoms"], c["mass_number_approx"], c["electrons"], c["rest_energy_J"]))
    print("    closes site by site; transfer A -> B of every conserved quantity: %s"
          % sorted({r["A_to_B"] for r in d["closure"].values()}))
    print("    at B this is the D25 gate: CI feedstock %.4g kg, residue %.4g kg, binder %s; P measured in the Proxima "
          "system: %s" % (d["stock"]["ci_feedstock_kg"], d["stock"]["ci_residue_kg"], d["stock"]["ci_binder"][0],
                          d["stock"]["P_measured_in_proxima_system"]))
    print("\n(3) The equation, per count and reading:")
    for k, e in d["equations"].items():
        print("\n  [%s]" % k)
        for x in e["terms"]:
            v = "OPEN" if x["value"] is None else "%.4g %s" % (x["value"], x["unit"])
            print("    %-14s %-6s %-8s %-14s %s" % (x["id"], x["side"], x["site"], v, x["what"]))
            if x["accounts_for"]:
                print("    %-14s accounts for: %s" % ("", ", ".join(x["accounts_for"])))
        print("    unaccounted inputs: %s   OPEN: %s   energy total: %s"
              % (e["unaccounted_inputs"] or "none", ", ".join(e["open_terms"]),
                 "REFUSED (OPEN terms)" if e["energy_total"] is None else e["energy_total"]))
    print("\n(5) Not totalled: every energy column carries OPEN terms (reading at A, retiring A's instance, E_rec).")
    print("    The board's channel reading, recorded beside M's H-ONE-POSITION and not graded: BEATS_LIGHT = %s"
          % d["board_channel_reading"]["BEATS_LIGHT"])


def selftest():
    n_ok = n_bad = n_ctl = 0
    structural = []

    def chk(label, got, want, ctl=False):
        nonlocal n_ok, n_bad, n_ctl
        ok = got == want
        n_ok += ok
        n_bad += not ok
        n_ctl += ctl
        print("  [%s]%s %-92s %r" % ("ok" if ok else "XX", " CTL" if ctl else "", label[:92], got))

    print("balance.py selftest")
    chk("M's words, items 29, 30 and 32, are found verbatim in the rulings file", m_words_present(),
        (True, True, True))
    nc = no_cloning()
    chk("no-cloning (quantum): over random pairs the overlap gap |<psi|phi>| - |<psi|phi>|^2 stays > 0 -- no unitary "
        "clones both", nc["least_overlap_gap"] > 0, True)
    chk("CONTROL: classical copying is not forbidden -- CNOT onto a blank copies both basis states",
        nc["cnot_copies_basis_states"], [True, True], ctl=True)
    chk("CONTROL: a one-word change to item 29's words is not found",
        (M_WORDS_29.replace("must equal", "should equal") in
         " ".join(open(RULINGS_FILE, encoding="utf-8").read().split())), False, ctl=True)
    cs = counts()
    chk("four counts, each positive, imported from measure.price_table",
        (len(cs), all(b > 0 for _, b in cs)), (4, True))
    chk("the species-sequence count equals measure.object_bits()'s (an imported value, compared)",
        abs(cs[0][1] - measure.object_bits()["species_sequence_bits"]) <= 1e-9 * cs[0][1], True)
    q = quantum_value_balance()
    chk("R-QUANTUM: B's least fidelity with the bits is 1 (to 1e-12)", abs(q["fid_min_with_bits"] - 1.0) < 1e-12, True)
    chk("R-QUANTUM: the four outcomes are equiprobable for every state (record alone holds no I)",
        q["p_dev_max_from_quarter"] < 1e-12, True)
    chk("CONTROL: bits withheld, B's fidelity is 1/2 for every state (B holds I/2), not 1: no balance without the bits",
        (q["fid_bits_withheld_dev_max_from_half"] < 1e-12, q["fid_mean_bits_withheld"] < 0.99), (True, True),
        ctl=True)
    chk("the board's readings this file rests on: CARRIES_SUBSTANCE False, IT_IS_A_MOVE_NOT_A_COPY True",
        (transit.CARRIES_SUBSTANCE, transit.IT_IS_A_MOVE_NOT_A_COPY), (False, True))
    o = object_conserved()
    chk("electrons = protons, recomputed from measure.atom_counts and massform.Z_OF; O carries Z = 8",
        (abs(o["electrons"] - sum(n * massform.Z_OF[e] for e, n in measure.atom_counts()[0].items())) < 1,
         massform.Z_OF["O"]), (True, 8))
    chk("mass number by M/u lies within 1.5% of the atom-weighted mean weight (H-BARYON-BY-MASS, a sanity bound)",
        abs(o["mass_number_approx"] - sum(n * stock.ATOMIC_MASS[e] for e, n in measure.atom_counts()[0].items()))
        / o["mass_number_approx"] < 0.015, True)
    structural.append("the conserved column closes site by site with A -> B transfer 0: built so (A's matter stays at "
                      "A; B's object is built from B's stock), so printed, not counted")
    for name, bits in cs:
        for r in ("R-CLASSICAL", "R-QUANTUM"):
            t = equation(bits, r)
            chk("%s | %s: every input is accounted for in an output" % (name[:24], r), unaccounted(t), [])
            chk("%s | %s: the energy total is REFUSED (OPEN terms present)" % (name[:24], r), energy_total(t), None)
    t = equation(cs[0][1], "R-QUANTUM")
    chk("CONTROL: the B-residue term dropped, IN-B-STOCK is still accounted (by OUT-B-OBJECT) -- the check is per input",
        unaccounted([x for x in t if x[0] != "OUT-B-RESIDUE"]), [], ctl=True)
    chk("CONTROL: the record and ebits outputs dropped, IN-EBITS goes unaccounted and is caught",
        unaccounted([x for x in t if x[0] not in ("OUT-EBITS", "OUT-B-OBJECT")]), ["IN-EBITS"], ctl=True)
    chk("CONTROL: every OPEN energy term filled with 0, the total is no longer refused",
        energy_total([x[:4] + ((0.0,) if (x[5] == "J" and x[4] is None) else (x[4],)) + x[5:] for x in t]) is None,
        False, ctl=True)
    chk("OPEN terms named: reading at A and assembly at B", open_terms(t), ["IN-A-READ", "IN-B-ASSEMBLE"])
    chk("R-CLASSICAL sends I bits; R-QUANTUM sends 2I (transit.CLASSICAL_BITS_PER_QUBIT = 2)",
        ([x[4] for x in equation(10.0, "R-CLASSICAL") if x[0] == "IN-CHANNEL"],
         [x[4] for x in equation(10.0, "R-QUANTUM") if x[0] == "IN-CHANNEL"], transit.CLASSICAL_BITS_PER_QUBIT),
        ([10.0], [20.0], 2))
    ch = [seat.channel_floor(1e6, T)["E_1d_one_pol_J"] for T in SCHEDULES_S]
    chk("the channel's energy falls as the schedule lengthens (no floor independent of T)", ch[1] < ch[0], True)
    s = stock_terms()
    chk("B's residue = CI feedstock - payload, positive; the gate at Proxima stays OPEN (P unmeasured)",
        (abs(s["ci_residue_kg"] - (s["ci_feedstock_kg"] - massform.PAYLOAD_KG)) < 1e-9, s["ci_residue_kg"] > 0,
         s["P_measured_in_proxima_system"]), (True, True, False))
    for x in structural:
        print("  [STRUCTURAL] " + x)
    print("\n%d/%d checks pass, %d of them controls; %d STRUCTURAL printed, not counted"
          % (n_ok, n_ok + n_bad, n_ctl, len(structural)))
    return n_bad == 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    elif "--json" in sys.argv:
        print(json.dumps(collect(), indent=1, default=str))
    else:
        report()
