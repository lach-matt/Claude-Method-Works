#!/usr/bin/env python3
"""m1_bulk.py -- items 229-231: M1, the plane's reading of the corridor's mouth, after M's answers on the bulk, on 203's
equality, on the open mouth, and after D- was computed.  M, 230: "the everything everywhere all at once bulk. This bulk
does all the work ... the bulk contects matter from position 1 to a position 2 that does not contain that exact matter
configuration"; "the energy being read/defined at position 1 can be absorbed by position 2 off it is not already
contained within position 2."  M, 231: to 210 "Yes, a statement"; to 211 "Do the computations for D-. I want to say yes
to D+, but we have no choice but to confirm by computing D-".  Worked in the conversation (computed by import, deduced;
not verified by a separate session); 2026-10-11.  Seated on item 231 under 206 after the conversation's critic lenses.

  M0 (read) M's words for items 230 and 231, verbatim in the rulings file.
  M1 (deduced from the clauses' supports) As it stood after item 230, every clause of M1 was carried by a computation,
     M's statement, or a demand M's words set aside -- except (d), no added matter on our plane, which needed 210's
     guess (the rim's junction is what the open mouth looks like) and 211's reading (the open mouth keeps the corridor
     on its D+ side).  M1 OPEN on (d) alone.  (Z) at the rim needs no guess: two_sided T1 proves the appearance from
     one smooth bulk (212's statement, reaffirmed by 230) and 214 states each sees its own reflection.
  M2 (computed, by import of d_minus.py, run here) D- has no body joined to the throat: none of the 40 marginal members
     is a D- body, a flat joint at the throat has D-'s tangential null energy negative at every depth, the least steep
     admissible D- path grows without bound going in, and the other tilt is never admissible (DM5, the critic's).  So D+ is the only orientation in which the open mouth has
     a body -- the computation M asked for before confirming D+ (231), and it confirms it.  211's support is now
     COMPUTED, not the board's reading.
  M3 (deduced) With item 231 -- 210 M's statement, 211 confirmed by M2 -- every clause is carried: M1 DERIVED, no
     blocker.  DERIVED in warptheorem.py's sense: from M's more basic statements and computed results.
  M4 (read) the record's own wording classes each support as it is used here: 210 as M's guess until 231, 211 as the
     board's reading put to M, 212's H-Z-REFLECTION as M's guess (not needed); 231 holds both answers.
  M5 (computed, from warptheorem.py's rows) the chain, counting an input green when its own status is green (the rule
     warptheorem.py states: a lemma is green only when every input it rests on is): 22 green with M1 OPEN, 32 with M1
     DERIVED; the ten rows that waited on M1 alone are B2t, E4r, G1, G3, H2tu, O1b, O1c, O2, Z1t, Z2r.
  M6 (computed; the cypher, roster 1173, run and audited) the configurations as cells over the clauses' readiness: two
     cells, and only item 231's configuration holds the target (every clause carried).  Clause (d) is the index's key --
     the one coordinate that varies -- so by 211's audit the languages' verdicts here are void as evidence: the cypher
     adds nothing the support table does not, and the table decides.

What this does not show.
  - M2's limit at the throat is deduced from the threshold law beyond the bank's first column (d_minus DM3), on the
    flat-limit bank, for static thin sheets.
  - (e) is carried inside the verified layer (m1_cypher M1 (e), stability O2).  Under the throat eq. (17)'s deep static
    bulk keeps b4_static S2's singular surface (open_mouth.py's note (v)); in M's configuration the bulk doing the work
    is the everything bulk (212, 230), so that static bulk is the board's model, not M's -- the board's reading, as for
    the kink (230 (a)), to be overruled by M at any point.
  - 203's equality is the ledger's (230 (b)): E read at position 1, absorbed at position 2 if not already contained;
    the static sheet's own Killing energy is not equated with E.
  - The logic lens (in the conversation): the kink and 203's equality are carried by the board's readings of M's own
    230 answers ((a), (b)), as item 179 read M's words for the plane-carried stages -- readings of what M said, which
    149 lets the board make, where 211's was a reading of the physics put to M as a question.  The distinction is the
    board's: if M overrules either reading, M1 returns to OPEN on that clause.

Reads warptheorem.py's rows (as data), the rulings file, tools/cypher.py, index_audit.py and d_minus.py.  Stdlib (+
sympy through d_minus's import of corridor_shape).  python3 m1_bulk.py [--selftest | --mutants]
"""
import ast
import contextlib
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
WT = os.path.join(D68, "warptheorem.py")
MUT = {}
_C = {}
GREEN = {"PROVED", "DERIVED", "AXIOM"}
M230 = ("the everything everywhere all at once bulk. This bulk does all the work. It the statistical possibility of all "
        "matter.")
M231_210 = 'M chose: "Yes, a statement"'
M231_211 = "Do the computations for D-. I want to say yes to D+, but we have no choice but to confirm by computing D-"
WAITING = ["B2t", "E4r", "G1", "G3", "H2tu", "O1b", "O1c", "O2", "Z1t", "Z2r"]


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


# Each support of M1 is one of: COMPUTED (an instrument's verified result), STATEMENT (M's words carried as M's),
# GUESS (M's words carried as M's guess, not a ruling -- the record's own wording, checked below), READING (the board's,
# put to M and unanswered), SET_ASIDE (a demand of the board's configuration that M's words remove, as item 179 found
# for the plane-carried stages).
D_210 = "210 H-RIM-OPEN-MOUTH"
D_211 = "211 H-OPEN-MOUTH-DPLUS"
D_DM = "d_minus.py M2: D- has no body joined to the throat, so the open mouth keeping a body is D+ (231's condition)"


def clauses(stage, dm_ok=True, s210=True):
    """M1's clauses and their supports: stage 230 is the record as it stood after item 230; stage 231 after M's answers
    and the D- computation (dm_ok: d_minus.py's checks pass; s210: 231's answer to 210 is in the rulings file)"""
    if stage == 230:
        d_sup = [("GUESS", D_210), ("READING", D_211)]
    else:
        d_sup = [("STATEMENT" if s210 else "GUESS", D_210), ("COMPUTED" if dm_ok else "READING", D_DM if dm_ok else D_211)]
    return [
        ("a", "a vacuum bulk on each side (eq. (17)'s static bulk)", [("COMPUTED", "m1_cypher.py M1 (a); b4_static.py")]),
        ("b", "the corridor exclusive to the bulk, meeting the planes only along its rim",
         [("COMPUTED", "m1_cypher.py M1 (b); rim_profile.py P4"), ("STATEMENT", "179")]),
        ("c", "our plane reads eq. (17) at r0 = 2m", [("COMPUTED", "m1_cypher.py M1 (c), by construction")]),
        ("d", "no added matter on our plane: the rim's junction is the open mouth, the plane's own fold",
         [("COMPUTED", "open_mouth.py O3 (a gravitating sheet's fold carries a Nambu-Goto line)")] + d_sup),
        ("e", "regular: B's closure inside the verified layer, the horizon extremal and smooth",
         [("COMPUTED", "m1_cypher.py M1 (e); stability.py O2")]),
        ("f", "position 2 admissible: positive, null energy net per ray",
         [("COMPUTED", "theorem_p2.py TC"), ("STATEMENT", "226"), ("STATEMENT", "229")]),
        ("Z at the rim", "(Z) at the rim with no partner: the joint's negative line is the one-sided view's appearance",
         [("COMPUTED", "two_sided.py T1 (one bulk smooth across the sheet: the two-sided stress vanishes)"),
          ("STATEMENT", "212 M-BULK-EVERYWHERE"), ("STATEMENT", "214"), ("STATEMENT", "230"),
          ("GUESS", "212 H-Z-REFLECTION")]),
        ("kink", "a bulk in which the warp's kink follows our plane into the corridor (item 212's first)",
         [("SET_ASIDE", "230 (a): the connection is the everything bulk's")]),
        ("203", "203's equality: the corridor's energy equals the README's E (item 212's second)",
         [("STATEMENT", "230: absorbed at position 2 if not already contained"), ("STATEMENT", "213"),
          ("COMPUTED", "warptheorem.py E3, resting on no input (E1x and E2x rest on CLOSE and are not used)")]),
        ("bridge", "Wall C's bridge between the universes", [("SET_ASIDE", "215, 230: cells of the bulk index, connected by it")]),
        ("static", "item 213's static obstruction (no static sheet joins a side with the object to one without)",
         [("SET_ASIDE", "215: binds glued bulks only")]),
    ]


# which GUESS / READING supports a clause cannot do without (the owners' own words): (d)'s junction is "what the open
# mouth looks like, not added matter" on 210, and the side kept is D+ on 211; (Z) at the rim needs no guess (M1 above)
def needs():
    n = {"d": {("GUESS", D_210), ("READING", D_211)}}
    if MUT.get("z_needs_guess"):
        n["Z at the rim"] = {("GUESS", "212 H-Z-REFLECTION")}
    return n


def verdict(cl):
    """M1's status from its clauses' supports: DERIVED when no needed support is a GUESS or a READING; READING when a
    READING remains needed; OPEN when a GUESS does.  A COMPUTED or STATEMENT support is never a blocker"""
    worst, blockers, nd = "DERIVED", [], needs()
    for key, text, sup in cl:
        for kind, src in sup:
            if kind in ("GUESS", "READING") and (kind, src) in nd.get(key, ()):
                blockers.append((key, kind, src))
                if kind == "GUESS":
                    worst = "OPEN"
                elif worst == "DERIVED":
                    worst = "READING"
    return worst, blockers


def d_minus_result():
    """d_minus.py's own checks, run here (DM0-DM3, DM5): M2 holds only if every one passes"""
    if MUT.get("d_minus_body"):
        return False, ["DM1 (mutant: a D- body assumed)"]
    if "dm" not in _C:
        dm = _load(os.path.join(HERE, "d_minus.py"), "m1b_dm")
        _C["dm"] = dm.checks(dm.compute())
    r = _C["dm"]
    return all(ok for _, ok in r), [n.split()[0] for n, ok in r if not ok]


def rulings_text():
    return " ".join(open(RULINGS, encoding="utf-8").read().split())


def answered_210():
    want = 'M chose: "No"' if MUT.get("misquote_231") else M231_210
    return want in rulings_text()


def configurations(dm_ok):
    """M1 after item 230, with each of 231's two moves alone, and with both"""
    s210 = answered_210()
    cfg = {"after item 230": clauses(230)}
    c = clauses(230)
    c[3] = (c[3][0], c[3][1], [c[3][2][0], ("STATEMENT" if s210 else "GUESS", D_210), ("READING", D_211)])
    cfg["210 as M's statement only"] = c
    c = clauses(230)
    c[3] = (c[3][0], c[3][1], [c[3][2][0], ("GUESS", D_210), ("COMPUTED" if dm_ok else "READING", D_DM if dm_ok else D_211)])
    cfg["D- computed only"] = c
    cfg["item 231 (both)"] = clauses(231, dm_ok, s210)
    return {name: verdict(cl) for name, cl in cfg.items()}


RECORD_WORDING = {D_210: ("rulings", "carried as M's guess, not a ruling: H-RIM-OPEN-MOUTH"),
                  "212 H-Z-REFLECTION": ("rulings", "Carried as M's guess, put"),
                  D_211: ("theorem", "the board's reading H-OPEN-MOUTH-DPLUS, put to M")}


def record_checks():
    rul = rulings_text()
    thm = " ".join(open(WT, encoding="utf-8").read().split())
    wording = {k: v in (rul if where == "rulings" else thm) for k, (where, v) in RECORD_WORDING.items()}
    raw = open(RULINGS, encoding="utf-8").read()
    present = {i: ("%s. **" % i) in raw for i in ("179", "210", "211", "212", "213", "214", "215", "226", "229", "230",
                                                    "231")}
    return dict(wording=wording, present=present, m230=M230 in rul, m231=(M231_210 in rul, M231_211 in rul))


def chain_effect():
    """the chain read from warptheorem.py's rows: a lemma green when PROVED or DERIVED and every input it rests on has
    a green status of its own; also with M1 held OPEN (the chain before item 231)"""
    mods = {n.targets[0].id: n.value for n in ast.parse(open(WT, encoding="utf-8").read()).body
            if isinstance(n, ast.Assign) and hasattr(n.targets[0], "id")}
    L, R = ast.literal_eval(mods["LEMMAS"]), ast.literal_eval(mods["RESTS_ON"])
    lem = [(n.split()[0], s) for c, n, s, w in L if c != "N"]
    inp = {n.split()[0]: s for c, n, s, w in L if c == "N"}
    gin = set() if MUT.get("inputs_not_counted") else {k for k, s in inp.items() if s in GREEN}
    green = lambda g: sorted(k for k, s in lem if s in GREEN and all(i in g for i in R.get(k, "").split()))
    return dict(now=green(gin), m1_open=green(gin - {"M1"}), m1_status=inp["M1"], n=len(lem),
                waiting_on_m1_only=sorted(k for k, s in lem if R.get(k) == "M1"))


def cypher_m1(cy, ia, cfg):
    """the configurations as cells over the clauses' readiness (1 = carried without a needed guess or reading): target
    every clause carried"""
    keys = [k for k, _, _ in clauses(231)]
    rows = {name: tuple(0 if k in {b[0] for b in bl} else 1 for k in keys) for name, (st, bl) in cfg.items()}
    cells = sorted(set(rows.values()))
    ix = cy.Index("m1_bulk", keys, [list(c) for c in cells], value_order={k: [0, 1] for k in keys})
    runs = {r: cy.run(ix, r, {"statistics_order": 2, "algebra_budget": 10 ** 6}) for r in ("1173",)}
    target = tuple(1 for _ in keys)
    return dict(rows=rows, held=sorted(n for n, r in rows.items() if r == target), cells=len(cells), runs=runs,
                audit=ia.audit_index(keys, cells))


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "m1b_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "m1b_ia")
    dm_ok, dm_failed = d_minus_result()
    cfg = configurations(dm_ok)
    return dict(dm=(dm_ok, dm_failed), cfg=cfg, before=verdict(clauses(230)), seated=verdict(clauses(231, dm_ok,
                answered_210())), record=record_checks(), chain=chain_effect(), cy=cypher_m1(cy, ia, cfg))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rc = o["record"]
    add("M0 M's words for items 230 and 231 verbatim in the rulings file (230's bulk; 231's two answers)",
        rc["m230"] and all(rc["m231"]) and answered_210())
    st, bl = o["before"]
    add("M1 after item 230: M1 OPEN on clause (d) alone -- 210's guess and 211's reading; (Z) at the rim needs no guess",
        st == "OPEN" and sorted(bl) == sorted([("d", "GUESS", D_210), ("d", "READING", D_211)]))
    add("M2 d_minus.py's checks pass (run here): D- has no body joined to the throat, so the open mouth keeping a body "
        "is D+ -- 211's support COMPUTED", o["dm"][0] and not o["dm"][1])
    st, bl = o["seated"]
    cfg = o["cfg"]
    add("M3 with item 231 every clause is carried: M1 DERIVED, no blocker; either move alone leaves it blocked (210 "
        "alone: READING on 211; D- alone: OPEN on 210's guess)", st == "DERIVED" and bl == []
        and cfg["210 as M's statement only"][0] == "READING" and cfg["D- computed only"][0] == "OPEN"
        and cfg["item 231 (both)"] == ("DERIVED", []))
    add("M4 the record's wording classes each support as used (210 M's guess until 231, 211 the board's reading put to "
        "M, 212's H-Z-REFLECTION M's guess); items 179, 210-215, 226, 229-231 present",
        all(rc["wording"].values()) and all(rc["present"].values()))
    ch = o["chain"]
    add("M5 the chain (inputs counted green by their own status): M1 %s in warptheorem.py; 22 green with M1 OPEN, 32 "
        "with M1 DERIVED; the ten rows that waited on M1 alone: %s" % (ch["m1_status"], ", ".join(WAITING)),
        ch["m1_status"] == "DERIVED" and len(ch["m1_open"]) == 22 and len(ch["now"]) == 32 and ch["n"] == 45
        and ch["waiting_on_m1_only"] == WAITING and sorted(set(ch["now"]) - set(ch["m1_open"])) == WAITING)
    y = o["cy"]
    add("M6 cypher (1173, run): two cells, only item 231's configuration holds the target (every clause carried); the "
        "audit finds clause (d) the index's key, so its verdicts are void as evidence (211) -- the table decides",
        y["held"] == ["item 231 (both)"] and y["cells"] == 2 and y["audit"]["keys"] == ["d"]
        and len(y["runs"]["1173"]["verdicts"]) > 0)
    return res


MUTANTS = {"z_needs_guess": "(Z) at the rim read as needing 212's guess",
           "d_minus_body": "D- read as having a body (the computation failing)",
           "misquote_231": "231's answer to 210 misquoted (not found)",
           "inputs_not_counted": "the chain's tally ignoring inputs' own statuses"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-19s %-50s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


def report(o):
    print("m1_bulk.py -- M1 after items 229-231\n")
    print("clauses and their supports (item 231):")
    for k, t, sup in clauses(231, o["dm"][0], answered_210()):
        print("  (%s) %s\n       %s" % (k, t, "; ".join("%s: %s" % s for s in sup)))
    print("\nd_minus.py's checks: %s" % ("all pass" if o["dm"][0] else "failed %s" % o["dm"][1]))
    print("the record's wording: %s; items present: %s; 230 verbatim: %s; 231's answers verbatim: %s" % (
        o["record"]["wording"], all(o["record"]["present"].values()), o["record"]["m230"], o["record"]["m231"]))
    print("\nM1's status by configuration (blockers):")
    for n, (st, bl) in o["cfg"].items():
        print("  %-28s %-8s %s" % (n, st, bl))
    c = o["chain"]
    print("\nthe chain: M1 %s; green %d (with M1 held OPEN %d); rows waiting on M1 alone: %s" % (
        c["m1_status"], len(c["now"]), len(c["m1_open"]), c["waiting_on_m1_only"]))
    y = o["cy"]
    print("cypher: %d cells; target (every clause carried) held by %s; audit %s" % (y["cells"], y["held"], y["audit"]))
    for rn, res in y["runs"].items():
        print("  roster %s: %s" % (rn, "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in res["verdicts"])))


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
