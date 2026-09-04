#!/usr/bin/env python3
"""compare_audit.py -- the comparison analysis, as a standing check.

Register 1169. Laying the index, the math and the language cypher side by side found
something no single-object audit could: the ORDER reading of the spectra index and the
ANALYSIS reading of it disagree — 194 of 205 adjacent-l pairs ordered by the mechanisms,
102 of 205 by the equation fitted on the same channels. The cypher says those two
languages absorb an addition identically and agree on Lambda. On Lambda_spectra they do
not, and that is the one thing the cypher forbids.

No audit in the compendium could have found it, because every one of them checks a single
object against itself. This checks THREE against each other.

WHAT IT CHECKS

  1  COVERAGE     every coordinate of the index has a math object that names it, and
                  every math family has an index part it describes. A family with no
                  index part is math about nothing; a coordinate with no object is a
                  choice nobody registered.

  2  LANGUAGE     the cypher lists seven languages. Each has been run on Lambda. This
                  reports which have been run on the OTHER indexes, because agreement
                  established on 976 cells is asserted and not tested elsewhere.

  3  CONTRADICTION  where two languages both speak about the same index, they must agree.
                  A disagreement is not a defect of either reading — it is a fault in one
                  of them, and the audit names the pair rather than picking a winner.

WHAT IT DOES NOT DO. It does not decide which language is right. Register 1169's
disagreement stood for a whole session with the equation blamed for it; the audit's job
is to surface the pair, not to adjudicate.
"""
import re, math, json, statistics as st
import importlib.util as iu
from collections import Counter, defaultdict
from zeno import State, step

LANGS = ["order", "geometry", "algebra", "analysis", "information", "statistics",
         "documentary"]

# which language each math family speaks, from the register's own 'language' coordinate
FAM_LANG = {
    "A": "order",        "L": "order",        "K": "order",
    "B": "analysis",     "P": "order",        "Q": "analysis",
    "T": "algebra",      "S": "order",        "G": "geometry",
    "W": "order",        "M": "algebra",      "C": "documentary",
    "EM": "analysis",    "F": "geometry",     "E": "information",
    "I": "documentary",
}

# which index coordinate each family bears on
FAM_PART = {
    "A": "the operator",        "L": "the cells and their order",
    "K": "closure and redundancy", "B": "the bounds on cells",
    "P": "the propagation mechanisms", "Q": "the channel equation",
    "T": "the tower",           "S": "the spectra objects",
    "G": "the register's own graph", "W": "the violation index",
    "M": "the horizon algebras", "C": "the audits",
    "EM": "the electromagnetic quotient", "F": "the figures",
    "E": "E itself",            "I": "the intake",
}

def load_math():
    sp = iu.spec_from_file_location("_m", "mathreg.py"); m = iu.module_from_spec(sp)
    try: sp.loader.exec_module(m)
    except SystemExit: pass
    return m.REG

def index_coordinates():
    """the spectra index's coordinates, and the math object that names each"""
    return [("Z",        "S.ground",  "the atomic number"),
            ("charge",   "S.ground",  "the ionisation stage"),
            ("ℓ",        "P.lcollapse","the Rydberg orbital"),
            ("2S+1",     "S.ground",  "the multiplicity, from Hund on the core"),
            ("regime",   "S.regime",  "the sign of δ₂ — measured, not derived"),
            ("|δ₂|",     "S.ritz",    "the curvature — predicts the channel's scatter")]

def language_runs():
    """which languages have been run on which index, and with what result"""
    return [("Λ",          "order",       True,  "E = 0 at 976 cells"),
            ("Λ",          "geometry",    True,  "agrees, register 353"),
            ("Λ",          "algebra",     True,  "agrees"),
            ("Λ",          "analysis",    True,  "agrees"),
            ("Λ",          "information", True,  "agrees"),
            ("Λ",          "statistics",  True,  "agrees, with the caveat"),
            ("Λ",          "documentary", False, "no operator exists"),
            ("Λ_spectra",  "order",       True,  "ℛ places 1,762 of 1,775"),
            ("Λ_spectra",  "analysis",    True,  "the channel equation, R² = 0.924"),
            ("Λ_spectra",  "geometry",    False, "never run"),
            ("Λ_spectra",  "algebra",     False, "never run"),
            ("Λ_spectra",  "information", False, "never run"),
            ("Λ_spectra",  "statistics",  False, "never run"),
            ("Λ_spectra",  "documentary", False, "no operator exists"),
            ("Λ_α",        "order",       True,  "E = 10 on 18 cores"),
            ("Λ_α",        "analysis",    False, "never run")]

def contradictions():
    """claims made about ONE index in TWO languages, with both readings.

    A row here is a pair that must agree by the cypher and does not. The measured
    figures are recomputed by the callers that own them; this records the pair.
    """
    return [("Λ_spectra", "δ falls with ℓ",
             "order",    "194/205  (P.lcollapse, register 1072)",
             "analysis", "102/205  (the channel equation, register 1169)",
             "OPEN — register 1169 attributes it to the noise floor at 11 pairs, "
             "which accounts for the 11 and not for the 92"),
            ("Λ_spectra", "the triplet defect exceeds the singlet",
             "order",    "55/66   (register 987)",
             "analysis", "33/66   (the channel equation, s < 0)",
             "OPEN — the fitted sign is opposite to the measured one"),
            ("Λ_spectra", "δ falls with charge along a sequence",
             "order",    "89/143  (P.iso)",
             "analysis", "135/143 (the channel equation)",
             "OPEN — the equation is MORE monotone than the data")]

def run():
    return load_math(), index_coordinates(), language_runs(), contradictions()

with State("compare_audit") as s:
    REG, COORD, LANG, CON = step(s, "load the three objects", run, budget=300)

by = defaultdict(list)
for k in REG: by[k.split(".")[0]].append(k)

print("  THE COMPARISON AUDIT — index · math · cypher\n")

# --- 1. coverage
print("  1 · COVERAGE\n")
print(f"      {'index coordinate':<12}{'named by':<14}{'objects':>8}   what it is")
miss = []
for nm, obj, desc in COORD:
    ok = obj in REG
    fam = obj.split(".")[0]
    if not ok: miss.append((nm, obj))
    print(f"      {nm:<12}{obj:<14}{len(by.get(fam,[])):>8}   {desc}")
orphan = [f for f in by if f not in FAM_PART]
print(f"\n      coordinates with no math object : {len(miss)}  {miss if miss else ''}")
print(f"      families with no index part     : {len(orphan)}  {orphan if orphan else ''}")

# --- 2. language
print("\n  2 · LANGUAGE — which have been run on which index\n")
idxs = sorted({r[0] for r in LANG}, key=lambda x: (x != "Λ", x))
print(f"      {'index':<12}" + "".join(f"{l[:5]:>13}" for l in LANGS))
for ix in idxs:
    row = {r[1]: r[2] for r in LANG if r[0] == ix}
    cells = "".join(f"{('run' if row.get(l) else ('—' if l=='documentary' else 'NOT RUN')):>13}"
                    for l in LANGS)
    print(f"      {ix:<12}{cells}")
notrun = [(r[0], r[1]) for r in LANG if not r[2] and r[1] != "documentary"]
print(f"\n      language/index pairs never run: {len(notrun)}")
for a, b in notrun: print(f"          {a} in {b}")

# --- 3. contradiction
print("\n  3 · CONTRADICTION — one index, two languages, two answers\n")
for ix, claim, l1, v1, l2, v2, note in CON:
    print(f"      {ix} — {claim}")
    print(f"          {l1:<12}{v1}")
    print(f"          {l2:<12}{v2}")
    print(f"          {note}\n")
print(f"      {len(CON)} standing contradictions")
print()
bad = len(miss) + len(orphan) + len(CON)
print(f"  {'COMPARISON AUDIT PASSES' if bad == 0 else f'COMPARISON AUDIT: {bad} findings'}")
