#!/usr/bin/env python3
"""pass_audit.py -- item 440: every row of the register against the corrected criterion for a pass.

M, 440: "A station is green at an end only when every row it rests on there is proved, or derived from first principles
and established  mathematics. - this is the criteria for each pass... And anything derived must be proved separately
with computation."  With 156 (M-DERIVED-AND-PROVED: every lemma both derived and proved, computed or machine-checked).
Labels: computed, deduced, M's.  Worked in the conversation; not verified; not seated.

  P0 (read) M's words, verbatim in the rulings file (156, 440).
  P1 (computed) Every instrument a row cites is found on disk and carries a selftest.  Thirteen were not run by the
     theorem's own selftest (warptheorem T1's lemma list stopped at item 362): arrival_large, b4d_large, bearing26,
     core_face, encode_labels, encode_read, exactcopy, focusing_parts, junction_own, quantum_onset, rearrange,
     settle_arrival, z3b_large -- all thirteen pass (run here at 440); added to T1 at 441, M approving, so none is left
     outside it.
  P2 (deduced) Each row not PROVED is classed by what proves it.
     C -- its claim is computed or machine-checked by the instruments it cites (the computation is the separate proof
          M asks for); its premises are named (M's rulings, READ sources, other rows).
     D -- part of its derivation is an argument in prose that no instrument computes or machine-checks.
     A -- it rests on a step assumed, not derived (O1b and O1c: the core delivering every part to the bounce, M's 422).
     X -- a definition of M's: neither proved nor derived; the corrected criterion no longer names it.
  P3 (deduced) The rows that do not pass now: D -- B7 (the formation's chain of rulings and one READ source) and B5b (the
     wall's tension share TS, deduced, no wall profile computed); A -- O1b and O1c; X -- R0, R1, R2, R6, RECON, B6'
     (put to M: are M's definitions first principles?); and SOURCEs and SOURCE, deferred.  Every other row is C.
     [Item 441: B5b's wall computed (b5b_wall.py W0-W7, approach approved at 441); B5b is C since.]
     [Item 442: B7 derived by the bulk's geometry (b7_geometry.py G0-G6, 442 (3)); B7 is C since.]
  P4 (deduced) Which stations the failing rows sit in, end by end, read from the map's own station lists; a station
     passes at an end only when every row it lists there is PROVED or C.
  P5 (deduced; item 441) M: "1 - no" (M's rulings are not first principles) and "2 - no. Each definition must be
     proved".  So a row passes only when its claim is computed, it names no ruling of M's among its premises, and it
     rests on no definition not yet proved.  RULED below is each row's premises among M's rulings, read from its
     where-field (verifier and work-item numbers set aside); FRAMEWORK is the definition B6' (our universe a plane of
     tension sigma with its offset in a five-dimensional bulk), on which every row set in the bulk or on the plane
     rests.  Under 441 three rows pass: I2, R3 and Z3a -- the capacity bound, exactness at the instant, and the null
     condition of our own matter -- each physics alone and computed.  Every other row waits on a definition proved
     (B6' first, which gates all the rest) or a ruling derived.

python3 pass_audit.py [--selftest | --run | --mutants]
"""
import contextlib, glob, html, importlib.util, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MAP = os.path.join(D68, "chainmap.html")
MUT = set()
WORDS = ((156, "All lemmas must be BOTH derived and proved"),
         (440, "anything derived must be proved separately with computation"),
         (440, "or derived from first principles and established mathematics"))
NOT_IN_T1 = ("arrival_large", "b4d_large", "bearing26", "core_face", "encode_labels", "encode_read", "exactcopy",
             "focusing_parts", "junction_own", "quantum_onset", "rearrange", "settle_arrival", "z3b_large")
# P2: the class of every row that is not PROVED (deduced row by row from its where-field and its instruments)
CLASS = {
    "G1": ("C", "E(N) computed: rows_small G1s, ledger E3s, exactE; axioms G1 from 101, 132, 131/133"),
    "H2": ("C", "the faces U = 0 computed (c1_oneway K2), the count on the 3-sphere (H1, c7_oneway V11); 270 (a) M's"),
    "H2tu": ("C", "rows_small H2tu-s computed; C3 at the large end"),
    "H2txs": ("C", "copy_p2 C1: position 2's bit area computed; 240 M's"),
    "H2tx": ("C", "copy_p2 C1, m1p2x_large Y8 computed; 240 M's"),
    "O1a": ("C", "the one-way object constructed and computed (c1_oneway, verified 304); one way M's (270, 276, 277)"),
    "O1b": ("C", "4D stretch and onset computed (focusing_parts, quantum_onset, core_face); the core computed on the "
                 "exact warped black string to the quantum region (core_large K1-K7, 478; was A, H-CORE-DELIVERS)"),
    "O1c": ("C", "4D stretch complete by exact forms (focusing_parts F1-F3); every causal geodesic reaches the region "
                 "in finite affine length and leaves it on position 2's side (core_large K5-K6, 478; was A)"),
    "O3s": ("C", "o3_hold O3e, stability S6 computed; Schlue READ; 334, 336 M's"),
    "O3": ("C", "o3_large Q1-Q4, stability S6 computed; FW and Schlue READ"),
    "Z1t": ("C", "rows_large Z1t computed"), "Z2r": ("C", "rows_large Z2r computed"),
    "Z3a": ("C", "b1_matter C1-C3, pointwise P1-P4 computed"),
    "Z3bs": ("C", "pair_math P1-P4 computed; readings Q1 the reading of 273 against 183, by M's words"),
    "Z3b": ("C", "z3b_large Z0-Z6 computed; readings Q1"),
    "Z3c": ("C", "nature_rows Z1-Z3 computed"),
    "B2t": ("C", "rows_large B2t, m1_large M1-M3 computed; FW READ"),
    "B3s": ("C", "b4d_small D10 reads every cell's row; settle_arrival A2, A6 computed"),
    "B3": ("C", "b4d_large K9 reads every cell's row; settle_arrival A4-A6 computed"),
    "B4ds": ("C", "b4d_small D2-D16 computed; M-PLANCK-ENDS M's; settle_arrival A2"),
    "B4d": ("C", "b4d_large K0-K12, settle_arrival A1-A6 computed; Wang-Choptuik READ"),
    "B5a": ("C", "b5a_oneway, b5a_residue computed, verified 339"),
    "B5cs": ("C", "e_positive E7 computed"), "B5c": ("C", "m1_large M8, tau_share T4 computed"),
    "B5pu": ("C", "b5p_cypher, pointwise P5 computed"), "B5px": ("C", "theorem_p2 TC, pointwise P6 computed"),
    "B5b": ("C", "b5b_wall W0-W7 computed (441): an exact smooth wall, its null energy a square at every point, the "
                 "matter it carries in D = 5, the crossing share to the thin limit; pointwise P1-P6 computed"),
    # [item 441: B5b was D -- "the wall's tension share TS deduced, no wall profile computed" -- until b5b_wall]
    "B7": ("C", "b7_geometry G0-G6 computed (442 (3)): the vacuum before the opening, strictly stationary, no closed "
                "trapped surface (Mars-Senovilla, READ), the planes coincident"),
    # [item 442: B7 was D -- "b7_formation: a chain of M's rulings (100, 140, 122 (4), 101 (1), 86 (3)) and one READ
    #  source, argued in prose, not machine-checked" -- until b7_geometry]
    "I1": ("C", "i2_capacity I2a: the throat's area entropy N bits computed; 137 (1) M's"),
    "E1us": ("C", "close_small K5, K9 computed; M-ENERGY-STAYS M's"),
    "E1u": ("C", "close_large L3, L5 computed; M-ENERGY-STAYS M's"),
    "E2us": ("C", "c_junction J1, close_small K9 computed; 110, 111 (a), 240 M's"),
    "E2u": ("C", "close_large L4, L5 computed; 110, 111 (a), 240 M's"),
    "E1xs": ("C", "close_small K9 computed; M-ENERGY-STAYS, 240, 111 (b), 230 M's"),
    "E1x": ("C", "close_large L3, junction_own G10 computed; M-ENERGY-STAYS, 390, 427 M's"),
    "E2xs": ("C", "c_junction J1, close_small K9 computed; 110, 111 (a), 240 M's"),
    "E2x": ("C", "close_large L4, L5 computed; 110, 111 (a), 240 M's"),
    "E3": ("C", "ledger E3, E3s machine-checked (z3); 155 M's"),
    "E4r": ("C", "rows_large E4r computed"),
    "R4": ("C", "r4_length computed; 155 M's"), "R5": ("C", "r5_build, copy_p2 computed; 155, 239, 240 M's"),
    "ENCODE": ("C", "encode_labels C1-C5 computed; 438 M's"),
    "M1": ("C", "m1_large M0-M10 computed; FW, AFPY READ"), "M1P2x": ("C", "m1p2x_large Y1-Y9 computed"),
    "FARs": ("C", "far_small F0-F9 computed, verified 355"), "FAR": ("C", "far_large L0-L9 computed, verified 355"),
    "WRITEs": ("C", "write_cypher W5, encode_read E5 computed"), "WRITE": ("C", "write_large X1-X3, encode_read E5"),
    "ARRIVALs": ("C", "arrival_small V0-V14 (verified 348), settle_arrival A2 computed"),
    "ARRIVAL": ("C", "arrival_large A1-A3, settle_arrival A4-A6 computed"),
    "CLOSEs": ("C", "close_small K1-K9 computed; M-ENERGY-STAYS M's"),
    "CLOSE": ("C", "close_large L1-L5 computed; M-ENERGY-STAYS M's"),
    "R0": ("X", "M's definition (70, 101 (8), 115 (c), 130 (2))"), "R1": ("X", "M's definition (145, 146)"),
    "R2": ("X", "M's definition (148, 240, 285)"), "R6": ("X", "M's definition (284, 285)"),
    "RECON": ("X", "M's definition (437)"),
    "B6'": ("X", "M's definition (201), its consistency computed (sigma_defines T1-T4, nature_rows B1-B3)"),
}
PASSING = ("PROVED", "C")
# P5 (item 441): each row's premises among M's rulings (substantive; verifier and work-item numbers set aside)
RULED = {
    "G1": (101, 131, 132, 133), "H2": (270,), "H2txs": (240,), "H2tx": (240, 390, 427),
    "O1a": (270, 273, 276, 277, 282), "O1bs": (259, 282), "O1cs": (282,), "O1b": (273, 422, 426),
    "O1c": (273, 414, 422, 426), "O3s": (158, 334, 336), "O3": (158, 160, 334, 336),
    "Z3bs": (177, 183, 273, 318), "Z3b": (177, 183, 273, 318, 422), "Z3c": (200, 201), "B1": (201, 320),
    "B3s": (162, 273, 336, 353, 386), "B4ds": (162, 273, 336, 353, 386), "B3": (162, 179, 273, 353, 386),
    "B4d": (162, 179, 273, 353, 386), "B4a": (282,), "B5a": (127, 275, 276, 282, 322), "B5cs": (139, 284, 285),
    "B5c": (139, 275, 276), "B5pu": (202,), "B5px": (202, 229, 284), "B6": (200,), "B8": (201, 328),
    "B7": (86, 100, 101, 122, 140, 282), "I1": (137,), "E1us": (336,), "E1u": (336,), "E2us": (110, 111, 240),
    "E2u": (110, 111, 240), "E1xs": (111, 230, 240, 336), "E1x": (111, 230, 240, 336, 390, 427),
    "E2xs": (110, 111, 240), "E2x": (110, 111, 240), "E3": (110, 111, 155, 239, 240), "R4": (155,),
    "R5": (155, 239, 240), "ENCODE": (131, 136, 146, 147, 148, 437, 438), "M1s": (282,), "M1": (273,),
    "M1P2xs": (275, 282), "M1P2x": (390, 427), "FARs": (139, 166, 226, 275, 318), "FAR": (139, 166, 226),
    "WRITEs": (163, 334, 336), "WRITE": (334, 336), "ARRIVALs": (109, 136, 162, 163, 240, 285, 340, 386),
    "ARRIVAL": (162, 198, 386, 432, 437), "CLOSEs": (336,), "CLOSE": (139, 336),
}
OFF_FRAMEWORK = ("I2", "R3", "Z3a")                   # physics of our own universe, not set in the bulk or the plane
DEFINITIONS = ("R0", "R1", "R2", "R6", "RECON", "B6'")


def strict(cls):
    """P5: the rows that pass under 441, and for every other row what it waits on"""
    out = {}
    for k, (c, why) in cls.items():
        wait = []
        if c not in PASSING:
            wait.append(c)
        if RULED.get(k):
            wait.append("rulings " + ", ".join(str(n) for n in RULED[k]))
        if k not in OFF_FRAMEWORK and k not in DEFINITIONS and "framework" not in MUT:
            wait.append("B6' (the framework) unproved")
        out[k] = wait
    return out


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def register():
    return _load(os.path.join(D68, "warptheorem.py"), "pa_wt").LEMMAS_NOW


def t1_list():
    src = open(os.path.join(D68, "warptheorem.py"), encoding="utf-8").read()
    body = src[src.index("def lemma_selftests"):src.index("def t2(")]
    return {f[:-3] for f in re.findall(r'"([a-z0-9_]+\.py)"', body)}


def cited_not_in_t1(rows):
    """instruments a row cites (by stem) that T1's lemma list does not run; common words that are also file stems,
    and the record's superseded arrival_cypher, set aside"""
    paths = glob.glob(os.path.join(HERE, "*.py")) + glob.glob(os.path.join(D68, "bulk", "*.py"))
    stems = {os.path.basename(p)[:-3] for p in paths}
    words_too = {"bulk", "crossing", "horizon", "opening", "plane", "static", "values", "causal", "escape", "umbilic",
                 "stability", "arrival_cypher"}
    t1 = t1_list() | {"exactE", "passage5d", "coin", "localbulk", "stability"}       # T1's own
    found = set()
    for r in rows:
        for st in stems - t1 - words_too:
            if re.search(r"(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])" % re.escape(st), r[3]):
                found.add(st)
    return sorted(found)


def classify(rows):
    out = {}
    for c, name, status, where in rows:
        key = name.split()[0]
        if status == "PROVED":
            out[key] = ("PROVED", "")
        elif status == "OPEN":
            out[key] = ("OPEN", "deferred by M (M-SOURCE-LAST)" if key.startswith("SOURCE") else "")
        else:
            cls = CLASS.get(key, ("?", "not classified"))
            if "promote" in MUT and cls[0] in ("D", "A", "X"):          # [478: no D or A row remains]
                cls = ("C", cls[1])
            out[key] = cls
    return out


def stations():
    """the map's stations: id -> {end: [row names]} from its station lists ('end' spans; shared rows both ends)"""
    s = open(MAP, encoding="utf-8").read()
    arts = re.findall(r'<article class="station" id="([^"]+)">(.*?)</article>', s, re.S)
    out = {}
    for sid, body in arts:
        ends = {"small": [], "large": []}
        for li in re.findall(r'<li class="lm[^"]*">(.*?)</li>', body, re.S):
            m = re.search(r"<b>([^<]+)</b>", li)
            if not m:
                continue
            name = html.unescape(m.group(1)).strip()
            e = re.search(r'<span class="end">([^<]+)</span>', li)
            end = e.group(1) if e else ""
            if "small" in end:
                ends["small"].append(name)
            elif "large" in end:
                ends["large"].append(name)
            else:
                ends["small"].append(name); ends["large"].append(name)
        out[sid] = ends
    return out


def station_verdicts(cls):
    v = {}
    for sid, ends in stations().items():
        v[sid] = {}
        for end, names in ends.items():
            bad = [n for n in names if n in cls and cls[n][0] not in PASSING]
            v[sid][end] = bad
    return v


def run_missing(names):
    res = {}
    for st in names:
        try:
            path = os.path.join(HERE, st + ".py")
            path = path if os.path.exists(path) else os.path.join(D68, "bulk", st + ".py")
            mod = _load(path, "pa_" + st)
            with contextlib.redirect_stdout(io.StringIO()):
                res[st] = bool(mod.selftest())
        except Exception as e:                                        # noqa: BLE001
            res[st] = "error: %s" % e
    return res


def report(run=False):
    rows = register()
    print("P0 M's words inside 156 and 440:", words())
    nt = cited_not_in_t1(rows)
    print("P1 cited instruments not run by the theorem's selftest (%d): %s" % (len(nt), ", ".join(nt)))
    if run:
        for k, v in run_missing(nt).items():
            print("   %-16s selftest %s" % (k, v))
    cls = classify(rows)
    by = {}
    for k, (c, why) in cls.items():
        by.setdefault(c, []).append(k)
    print("P2 classes:", {c: len(v) for c, v in sorted(by.items())})
    onm = [k for k in by.get("C", []) if "M's" in cls[k][1] or "M-" in cls[k][1]]
    print("   of the C rows, %d name M's rulings among their premises: %s" % (len(onm), ", ".join(onm)))
    for c in ("D", "A", "X", "OPEN"):
        for k in by.get(c, []):
            print("   %-5s %-7s %s" % (c, k, cls[k][1]))
    st = strict(cls)
    passing = sorted(k for k, w in st.items() if not w)
    print("P5 under 441, rows that pass (%d): %s; every other row waits on a ruling derived or a definition proved"
          % (len(passing), ", ".join(passing)))
    print("P4 stations not passing at an end under the corrected criterion (440's reading):")
    for sid, ends in station_verdicts(cls).items():
        for end, bad in ends.items():
            if bad:
                print("   %-12s %-6s %s" % (sid, end, ", ".join(bad)))


def selftest(quiet=False):
    ok = []

    def say(s):
        if not quiet:
            print(s, flush=True)
    w = words(); ok.append(w); say("P0 M's words verbatim inside 156 and 440: %s" % w)
    rows = register()
    nt = cited_not_in_t1(rows)
    p1 = nt == []                                                    # [item 441: T1 runs all thirteen]
    ok.append(p1); say("P1 every cited instrument is in T1's list now (the thirteen added at 441): %s" % p1)
    cls = classify(rows)
    unclassed = [k for k, v in cls.items() if v[0] == "?"]
    fail = sorted(k for k, v in cls.items() if v[0] not in PASSING)
    p2 = not unclassed and fail == sorted(["R0", "R1", "R2", "R6", "RECON", "B6'",
                                           "SOURCEs", "SOURCE"])         # [B5b out at 441, B7 at 442, O1b and O1c at 478]
    ok.append(p2); say("P2-P3 every row classed; not passing: %s: %s" % (", ".join(fail), p2))
    v = station_verdicts(cls)
    p4 = any(bad for ends in v.values() for bad in ends.values()) and all(
        set(bad) <= set(fail) for ends in v.values() for bad in ends.values())
    ok.append(p4); say("P4 the failing rows located in the map's stations: %s" % p4)
    st = strict(cls)
    p5 = sorted(k for k, w in st.items() if not w) == ["I2", "R3", "Z3a"]
    ok.append(p5); say("P5 under 441 three rows pass -- I2, R3, Z3a: %s" % p5)
    return all(ok)


def mutants():
    names = ["promote", "framework"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-10s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report(run=bool(a and a[0] == "--run"))
