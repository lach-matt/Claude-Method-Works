#!/usr/bin/env python3
"""gate97.py -- INSTRUMENT B.  Clause 3 decided by coverage, not by sample size.

Scores PREDICTION-B-EXPOSED.md (512ae671d2fa0a8f, filed 15:38:25Z).

B-1  free elimination: rows where entrant and runner-up share n+l are ORDERING-IMMUNE
     by F55.2's theorem (equal-n+l reversal is a within-shell / tie-break event).
B-2  bound B = max measured c=1e6 differential = 0.21400 Ha, applied uniformly.
     Parameter-free: it is a measured maximum, not a fit.
B-3  exposed rows with margin > B are PROVED safe.  Residue = the rest, minus walked.

Reads the sealed chain read-only.  Writes nothing into it.
"""
import json, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(HERE, "..", "rt", "nlchain.jsonl")

B = 0.21400                      # s56 measured maximum differential, Z=91
DERIV_LO, DERIV_HI = 2, 108      # the derivation is 107 rows.  Z>108 is OUTPUT.

# the 12 rows already walked at c=1e6: 11 from s55 + Z=57 from s56
WALKED = {57, 89, 90, 91, 58, 21, 19, 24, 29, 39, 46, 47}

def nl(ch):
    """n+l and n from a channel label like '4s'."""
    n = int(ch[0]) if len(ch) == 2 else int(ch[:-1])
    l = "spdfghik".index(ch[-1])
    return n + l, n

def load(path=CHAIN, corrupt=None):
    rows = []
    for line in open(path):
        r = json.loads(line)
        if not (DERIV_LO <= r["Z"] <= DERIV_HI):
            continue
        if r.get("mode") != "chain":
            continue
        rows.append(r)
    if corrupt:
        rows = corrupt(rows)
    return rows

def analyse(rows):
    exposed, immune = [], []
    for r in rows:
        order = r["order"]
        ent = order[0][0]
        run = order[1][0]
        g_e, n_e = nl(ent)
        g_r, n_r = nl(run)
        rec = dict(Z=r["Z"], ent=ent, run=run, g_e=g_e, g_r=g_r,
                   margin=round(order[0][1] - order[1][1], 6) * -1
                   if False else abs(order[0][1] - order[1][1]))
        (immune if g_e == g_r else exposed).append(rec)
    return exposed, immune

def report(rows, quiet=False):
    exposed, immune = analyse(rows)
    n_exp = len(exposed)
    proved = [e for e in exposed if e["margin"] > B]
    under = [e for e in exposed if e["margin"] <= B]
    residue = [e for e in under if e["Z"] not in WALKED]
    if not quiet:
        print(f"  rows in derivation window : {len(rows)}")
        print(f"  IMMUNE  (equal n+l)       : {len(immune)}")
        print(f"  EXPOSED (cross n+l)       : {n_exp}   <-- N_exp")
        print()
        print(f"  {'Z':>4} {'ent':>5} {'run':>5} {'g_e':>4} {'g_r':>4} {'margin':>10}   verdict")
        for e in exposed:
            v = "PROVED SAFE" if e["margin"] > B else (
                "walked" if e["Z"] in WALKED else "RESIDUE")
            print(f"  {e['Z']:>4} {e['ent']:>5} {e['run']:>5} {e['g_e']:>4} "
                  f"{e['g_r']:>4} {e['margin']:>10.5f}   {v}")
        print()
        print(f"  B (uniform, measured max) : {B:.5f} Ha")
        print(f"  PROVED SAFE by margin > B : {len(proved)}")
        print(f"  exposed with margin <= B  : {len(under)}")
        print(f"  of those already walked   : {len(under) - len(residue)}")
        print(f"  RESIDUE                   : {len(residue)}   {[e['Z'] for e in residue]}")
    return n_exp, exposed, proved, residue

def score(rows):
    n_exp, exposed, proved, residue = report(rows)
    ez = sorted(e["Z"] for e in exposed)
    PRED = [2, 3, 4, 11, 12, 19, 20, 37, 38, 55, 56, 87, 88]
    cl = []
    cl.append(("B-1a  N_exp == 13", n_exp == 13, f"N_exp={n_exp}"))
    cl.append(("B-1b  exposed set is the predicted 13", ez == PRED, f"{ez}"))
    cl.append(("B-1c  no d/f-block row exposed",
               all(e["ent"][-1] not in "df" for e in exposed),
               ",".join(f"{e['Z']}:{e['ent']}" for e in exposed if e["ent"][-1] in "df") or "none"))
    cl.append(("B-1c' La(57) and Ac(89) IMMUNE",
               57 not in ez and 89 not in ez, f"57 in exp={57 in ez}, 89 in exp={89 in ez}"))
    cl.append(("B-3a  uniform bound does NOT close clause 3", len(residue) > 0,
               f"residue={len(residue)}"))
    cl.append(("B-3b  proved-safe count in {2,3}", len(proved) in (2, 3),
               f"proved={len(proved)}"))
    cl.append(("B-3c  residue in [8,11]", 8 <= len(residue) <= 11, f"residue={len(residue)}"))
    print()
    ok = 0
    for name, passed, detail in cl:
        print(f"  {'PASS' if passed else 'FALSIFIED':>9}  {name:<42} {detail}")
        ok += passed
    print(f"\n  GATE97: {ok}/{len(cl)} clauses hold as filed.")
    return ok, len(cl), n_exp, exposed, proved, residue

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "canfail":
        print("=== CAN-FAIL 1: force every runner-up into the entrant's own group ===")
        def c1(rows):
            for r in rows:
                r["order"] = [r["order"][0], [r["order"][0][0], r["order"][1][1]]]
            return r0 if False else rows
        n, *_ = report(load(corrupt=c1), quiet=True)
        print(f"  N_exp = {n}   (expect 0; gate must FALSIFY B-1a)  "
              f"{'BITES' if n != 13 else 'DOES NOT BITE -- gate is blind'}")
        print()
        print("=== CAN-FAIL 2: inflate every margin above B ===")
        def c2(rows):
            for r in rows:
                o = r["order"]
                r["order"] = [o[0], [o[1][0], o[0][1] - 99.0]] + o[2:]
            return rows
        _, _, pr, res = report(load(corrupt=c2), quiet=True)
        print(f"  residue = {len(res)}, proved = {len(pr)}   (expect residue 0)  "
              f"{'BITES' if len(res) == 0 else 'DOES NOT BITE'}")
        print()
        print("=== CAN-FAIL 3: collapse every margin to zero ===")
        def c3(rows):
            for r in rows:
                o = r["order"]
                r["order"] = [o[0], [o[1][0], o[0][1]]] + o[2:]
            return rows
        _, _, pr, res = report(load(corrupt=c3), quiet=True)
        print(f"  proved = {len(pr)}   (expect 0)  "
              f"{'BITES' if len(pr) == 0 else 'DOES NOT BITE'}")
        sys.exit(0)
    ok, tot, *_ = score(load())
    sys.exit(0)
