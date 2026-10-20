#!/usr/bin/env python3
"""phase2.py -- item 442, phase 2: what computation proves after the prior art, and which rows pass.  M, 442: "Prove
all readings in the warp theorem using previous arts and works in the field, and after that, then use computation to
prove the rest."  prior_art.py gave each of the 61 readings its verdict; this instrument gives each the status of its
remainder, and recomputes 441's pass audit with the readings proved.  Labels: computed (the audit), deduced (each
status is the board's reading of the instruments named, put to M), M's.  Worked in the conversation; not verified; not
seated.

  Q0 (read) M's words: 442's direction.
  Q1 (deduced) Each reading's remainder:
     NONE      -- established by the prior art, or definitional: nothing left to compute.
     COMPUTED  -- the remainder is computed by the instruments named (each on disk with a selftest).
     BOUNDED   -- proved inside a stated bound, the contrary part excluded (437 inside the reconstructible region, 427
                  for sigma > 0); a row resting on it passes once shown to stay inside.
     TO-COMPUTE -- owed: a computation not yet made (R6 and 284, the room's work).
     REDERIVE  -- a statement about nature the literature does not hold as stated, or a contrary part: its rows are
                  re-derived without it (M-REDERIVE-WITHOUT, 442 (2)).
     BEYOND    -- outside established physics: 273's bounce (prior_art flag (a)).
  Q2 (computed) The audit under 442: a row passes when its own claim is computed (pass_audit's class C or PROVED),
     B6' is proved (b6p_prove.py), and every reading it names is NONE or COMPUTED; the P rulings that are process or
     scope (259, 318, 322, 414) drop, the three confirmations carry their readings, and 422 waits on the core.
  Q3 (computed) The passing rows, and for every other row what it waits on.
  Q4 (computed) Instruments named here but outside T1's list, put to M as at 441.

python3 phase2.py [--selftest | --mutants]
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
WORDS = ("Prove all readings in the warp theorem using previous arts and works in the field",)
DROPPED_P = (259, 318, 322, 414)                   # process and scope; 328, 334, 353 carry readings; 422 waits

# Q1: reading -> (status, instruments, note)
REMAINS = {
    "201": ("COMPUTED", ["b6p_prove.py"], "B6' proved to M's standard (442)"),
    "101": ("NONE", [], "established"), "133": ("NONE", [], "established"), "158": ("NONE", [], "established"),
    "229": ("NONE", [], "established"), "336": ("NONE", [], "established"), "386": ("NONE", [], "established"),
    "353": ("NONE", [], "established"),
    "R0": ("COMPUTED", ["settle_arrival.py", "encode_labels.py"], "the shell of E(N) forms the face; N computable"),
    "R1": ("COMPUTED", ["encode_labels.py"], "the labels decode exactly"),
    "R2": ("COMPUTED", ["p2_matter.py", "copy_p2.py"], "the copy's structures under the destinations' laws"),
    "R6": ("COMPUTED", ["room_work.py"], "realizable: the displacement inside E in vacuum, gas and liquid; "
                                         "a finding: inside solid matter it can exceed E"),
    "437": ("BOUNDED", ["bearing26.py"], "RECON inside the reconstructible region"),
    "110": ("COMPUTED", ["ledger.py"], "the ledger across the passage (its own premise 155 is REDERIVE)"),
    "111": ("COMPUTED", ["ledger.py"], "E3"), "230": ("COMPUTED", ["ledger.py"], "E3"),
    "239": ("COMPUTED", ["ledger.py"], "E3"),
    "127": ("COMPUTED", ["static.py"], "coincident planes act as one plane of summed tension (S2)"),
    "275": ("COMPUTED", ["static.py"], "as 127"),
    "131": ("COMPUTED", ["axioms.py", "encode_labels.py"], "the throat by N under the fixed code (the shortest "
                                                           "form uncomputable, prior art)"),
    "132": ("COMPUTED", ["axioms.py", "i2_capacity.py"], "the README's N against the area"),
    "136": ("COMPUTED", ["encode_labels.py"], "one fixed exact encoding"),
    "137": ("COMPUTED", ["i2_capacity.py"], "N bits against the throat's area (I2a)"),
    "139": ("REDERIVE", ["pointwise.py", "b5b_wall.py"], "(2), the positivity, computed; (1), the negative plane, "
                                                         "contrary (SMS): rows re-derived on the destination's own "
                                                         "sigma > 0"),
    "146": ("COMPUTED", ["encode_labels.py"], "as R1"), "147": ("COMPUTED", ["encode_labels.py"], "by construction"),
    "148": ("COMPUTED", ["p2_matter.py", "copy_p2.py"], "as R2"),
    "160": ("COMPUTED", ["settle_arrival.py"], "the face from the shell at the opening"),
    "198": ("COMPUTED", ["settle_arrival.py"], "as 160"), "340": ("COMPUTED", ["settle_arrival.py"], "as 160"),
    "162": ("COMPUTED", ["settle_arrival.py", "b4d_large.py"], "the size fixed by the shell, the face static after"),
    "163": ("NONE", [], "definitional"),
    "166": ("COMPUTED", ["static.py"], "coincident planes: both at once"),
    "179": ("COMPUTED", ["settle_arrival.py"], "the warped Vaidya's horizon in the bulk (A4)"),
    "282": ("COMPUTED", ["c1_oneway.py", "c4_oneway.py", "c5_oneway.py", "c7_oneway.py"],
            "(1), C1, C4, C5 and C7 re-posed one-way"),
    "282b": ("COMPUTED", ["b7_geometry.py"], "(2), B7's join through the bulk with no trapped surface before the "
                                             "opening (442 (3)); the event horizon's head start a finding"),
    "200": ("COMPUTED", ["b6_once.py"], "counted once"),
    "226": ("COMPUTED", ["theorem_p2.py", "p2_combined.py"], "the destinations' own values"),
    "427": ("BOUNDED", ["junction_own.py"], "every sigma > 0 (negative tension contrary, SMS)"),
    "240": ("COMPUTED", ["copy_p2.py"], "as R2"), "285": ("COMPUTED", ["copy_p2.py"], "as R2"),
    "284": ("COMPUTED", ["room_work.py"], "as R6"),
    "270": ("COMPUTED", ["h_oneway.py", "i_oneway.py", "c1_oneway.py"], "the one-way object"),
    "276": ("COMPUTED", ["h_oneway.py"], "as 270"), "277": ("COMPUTED", ["i_oneway.py"], "as 270"),
    "273": ("COMPUTED", ["bounce_qm.py", "bounce_close.py", "bounce_proof.py", "qb_baez.py", "transition_aos.py",
                         "transition5.py", "transition5q.py", "transition5r.py"],
            "[483] computed from the quantum dynamics: loop quantum gravity's effective (holonomy-corrected) interior, "
            "in 4D (transition_aos) and carried to the 5D core with its scales fixed by 415 (transition5q): one "
            "transition surface, no inner horizon, the white hole's mass the black hole's, curvature bounded, probability "
            "1, time 2 r_h/c; transition5 the form it realizes.  A candidate quantum theory: no established theory "
            "reaches x >= 1.  Was BEYOND (442-482); transition_qt5's route withdrawn at 480 (an inner horizon).  [485] "
            "transition5r: the dynamics is its polymer quantum theory's hbar -> 0 limit; the structure independent of "
            "the holonomy representation and the coefficients; the equal mass rests on one onset curvature (415).  "
            "[536-537] Defined in quantum physics (bounce_qm): the interior's Wheeler-DeWitt equation in the bulk's "
            "clock, unitarity forcing the reflection into the white hole; the rows rest on it, transition5q, the "
            "candidate theory's geometry, supporting it; the equal mass on 183, 273 (a) and (c) and 386 "
            "(bounce_close C3).  [538] An input row, QB, COMPUTED-THEORIZED, with its complete proof "
            "(BOUNCE-PROOF.md, bounce_proof P1-P6); the place x = 1 not a premise (P6).  [539] Its Planckian "
            "curvature under varying values of Baez's constants (qb_baez): the same numbers in every universe "
            "scanned, the size moving only through ell"),
    "390": ("COMPUTED", ["junction_own.py"], "position 2's face closes when empty"),
    "426": ("COMPUTED", ["encode_read.py"], "the least write by the size"),
    "432": ("COMPUTED", ["settle_arrival.py"], "the shell carries E at the opening (its N part unused)"),
    "438": ("COMPUTED", ["encode_labels.py"], "by construction"),
    "86": ("REDERIVE", [], "B7 alone; dropped by B7's geometry"),
    "100": ("REDERIVE", [], "B7 alone; dropped by B7's geometry (the weaker form established)"),
    "122": ("REDERIVE", [], "B7 alone; dropped by B7's geometry (contrary in 5D)"),
    "140": ("REDERIVE", [], "B7 alone; dropped by B7's geometry"),
    "109": ("REDERIVE", [], "ARRIVALs: the face's end with its content, re-derived without it"),
    "155": ("REDERIVE", [], "E3, R4, R5: the ledger's excess re-derived without the expansion"),
    "177": ("REDERIVE", [], "Z3b, Z3bs: re-derived on the averaged null condition (proved)"),
    "183": ("REDERIVE", [], "as 177"),
    "202": ("REDERIVE", [], "B5pu, B5px: re-derived on 229's ordinary matter instead"),
    "320": ("COMPUTED", ["rederive.py", "b1_matter.py"], "its information disjunct by Reeh-Schlieder: every bulk carries "
                                                         "the graviton's vacuum, entangled between any two regions "
                                                         "(RS_ENT; rederive X4, 465)"),
    "328": ("COMPUTED", ["relativity.py"], "observed for gravity; computed for every front"),
    "334": ("COMPUTED", ["o3_large.py", "write_large.py", "o3_hold.py"], "the hold as the face standing"),
}
STATUSES = ("NONE", "COMPUTED", "BOUNDED", "TO-COMPUTE", "REDERIVE", "BEYOND")
PROVED_DEFS = {"B6'": "b6p_prove.py"}
ROW_PART = {"B4a": {282: "282b"}, "B7": {282: "282b"}}       # the rows that use 282 (2), B7's join
DROPPED_FOR = {"B7": (86, 100, 122, 140)}                     # b7_geometry G6: B7 derived without them
# a row on a BOUNDED reading passes when it is shown to stay inside the bound
INSIDE_BOUND = {("ENCODE", 437): "the encoding is integers only, the same under any constants (encode_labels C3)",
                ("E1x", 427): "junction_own computes every sigma2, so every sigma2 > 0",
                ("H2tx", 427): "as E1x", ("M1P2x", 427): "as E1x",
                # 443 (1), approved: the wording bounded to the reconstructible region and to sigma > 0
                ("RECON", 437): "RECON's name bounded to the reconstructible region (443 (1))",
                ("ARRIVAL", 437): "ARRIVAL's name bounds its rebuild to the region (443 (1)); its 437 is item 437 (3), "
                                  "the re-wording, not RECON's 437 (4) -- a conflation in refound's table, recorded"}
DEF_READING = {"R0": "R0", "R1": "R1", "R2": "R2", "R6": "R6", "RECON": "437", "B6'": "201"}
# [item 489] R1 OPEN and twelve rows with it (the 488 verification's F1, F3, F5); [item 491] F1's and F3's premise
# withdrawn (432 (2), 163, 418, 336/386): R1 back as M's definition (r1_exact), FACE2s, FACE2 and the eight on them
# proved (face2_release); SOURCEs and SOURCE stay OPEN on F5; [item 534] SOURCEs and SOURCE COMPUTED-THEORIZED, which
# closes them (M: 'label them as computed')
OPEN_489 = set()
# item 465, OBSTACLES rank 4: rows re-derived without a REDERIVE reading (rederive.py X1-X9, its selftest the check);
# the reading keeps its status, the row no longer rests on it
REDERIVED = {("R4", 155): "X1 (155 (2), a definition)", ("R5", 155): "X1 (155 (3), established)",
             ("E3", 155): "X2 (the release at position 2's face's closing)", ("ARRIVALs", 109): "X3 (136 (1), 136 G, 162)",
             ("B5pu", 202): "X5 (one universe: our matter, pointwise P4-P5)", ("B5px", 202): "X6 (229's destination)",
             ("B5c", 139): "X9 (Sigma+ > 0 at 229's destination)", ("B5cs", 139): "X9",
             ("FAR", 139): "X7 (every decaying side)", ("FARs", 139): "X7", ("CLOSE", 139): "X8 (junction_own G8-G9)",
             # [Item 478] Z3b's content stated in five dimensions needs neither reading: the bulk's R_kk = 0, the README's
             # G_vv >= 0, the tension null on null rays (z3b_large Z1-Z3), the turned rays' negative inside the region
             # (Z5; pair_math P1-P3 at the small end); the plane's four-dimensional negative, O((ell/r0)^2), is the
             # projected Weyl term, geometry not matter -- the part 177 and 183 had read as an appearance
             ("Z3b", 177): "z3b_large Z1-Z3, Z5", ("Z3b", 183): "z3b_large Z1-Z3, Z5",
             ("Z3bs", 177): "pair_math P1-P3", ("Z3bs", 183): "pair_math P1-P3"}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def words():
    s = re.sub(r"\s+", " ", open(RULINGS, encoding="utf-8").read())
    return all(w in s for w in WORDS)


def remains():
    r = dict(REMAINS)
    if "beyond_computed" in MUT:                                       # [483] the mutant now restores 273 as BEYOND
        r["273"] = ("BEYOND", [], "")
    if "drop" in MUT:
        r.pop("155")
    return r


def audit():
    pa = _load(os.path.join(HERE, "pass_audit.py"), "p2_pa")
    cls = pa.classify(pa.register())
    rem = remains()
    ok_status = ("NONE", "COMPUTED")
    out = {}
    for row, (c, _) in cls.items():
        wait = []
        if row in DEF_READING:
            st = rem[DEF_READING[row]][0]
            inside = (row, int(DEF_READING[row])) in INSIDE_BOUND if DEF_READING[row].isdigit() else False
            if st == "BOUNDED" and inside and "outside" not in MUT:
                st = "NONE"
            if st not in ok_status:
                wait.append("%s %s" % (DEF_READING[row], st))
            out[row] = wait
            continue
        if c not in pa.PASSING:
            wait.append("its own claim (%s)" % c)
        for n in pa.RULED.get(row, ()):
            if n in DROPPED_P or n in DROPPED_FOR.get(row, ()):
                continue
            if n == 422:                                                 # [Item 478] computed: core_large.py K1-K7
                if "core_owed" in MUT:
                    wait.append("422 the core (TO-COMPUTE)")
                continue
            if (row, n) in REDERIVED and "no_rederive" not in MUT:
                continue
            key = ROW_PART.get(row, {}).get(n, str(n))
            st = rem[key][0]
            if st == "BOUNDED" and (row, n) in INSIDE_BOUND and "outside" not in MUT:
                continue
            if st not in ok_status:
                wait.append("%s %s" % (key, st))
        if row not in pa.OFF_FRAMEWORK and rem["201"][0] not in ok_status:
            wait.append("B6' unproved")
        out[row] = wait
    return out


def outside_t1():
    pa = _load(os.path.join(HERE, "pass_audit.py"), "p2_pa2")
    t1 = set(pa.t1_list())
    named = {f for v in REMAINS.values() for f in v[1]}
    return sorted(f for f in named if f[:-3] not in t1)                # t1_list gives stems


def report():
    print("Q0 M's words:", words())
    rem = remains()
    cnt = collections.Counter(v[0] for v in rem.values())
    print("Q1 61 readings' remainders:", ", ".join("%s %d" % (s, cnt[s]) for s in STATUSES))
    for s in ("TO-COMPUTE", "BOUNDED", "REDERIVE", "BEYOND"):
        print("  %s: %s" % (s, ", ".join(k for k, v in rem.items() if v[0] == s)))
    a = audit()
    passing = sorted(k for k, w in a.items() if not w)
    print("Q2-Q3 under 442, %d rows pass: %s" % (len(passing), ", ".join(passing)))
    for k, w in sorted(a.items()):
        if w:
            print("   %-8s waits on %s" % (k, "; ".join(w)))
    print("Q4 instruments named here outside T1:", ", ".join(outside_t1()))


def selftest(quiet=False):
    say = (lambda *a: None) if quiet else print
    ok = []
    r = words(); ok.append(r); say("Q0 words: %s" % r)
    pa_rd = _load(os.path.join(HERE, "prior_art.py"), "p2_prior").READINGS
    rem = remains()
    r = set(pa_rd) == set(rem) - {"282b"}; ok.append(r)
    say("Q1 every reading of prior_art has a remainder (282 split in two): %s" % r)
    r = all(v[0] in STATUSES for v in rem.values()) and all(v[1] for v in rem.values() if v[0] == "COMPUTED")
    ok.append(r); say("Q1 every status valid; every COMPUTED names its instruments: %s" % r)
    exists = all(os.path.exists(os.path.join(HERE, f)) or os.path.exists(os.path.join(D68, "bulk", f))
                 for v in rem.values() for f in v[1])
    ok.append(exists); say("Q1 every named instrument on disk: %s" % exists)
    rd = {k: v for k, v in rem.items() if k in pa_rd}
    r = all(pa_rd[k][3] != "EST" or v[0] in ("NONE", "COMPUTED") for k, v in rd.items()) and \
        all(v[0] in ("REDERIVE", "BOUNDED") for k, v in rd.items() if pa_rd[k][3] == "CONTRA")
    ok.append(r); say("Q1 consistent with the verdicts (EST needs nothing; CONTRA bounded or re-derived): %s" % r)
    r = rem.get("273", ("",))[0] == "COMPUTED" and "transition5q.py" in rem["273"][1]
    ok.append(r); say("Q1 273 computed from the 5D quantum dynamics (483; BEYOND before): %s" % r)
    a = audit()
    passing = sorted(k for k, w in a.items() if not w)
    r = set(["I2", "R3", "Z3a", "B5b", "B6'", "CLOSEs", "E1us", "E1u", "ENCODE", "E1x", "M1s", "O1bs", "B7", "B4a"]) <= \
        set(passing) and {"O1a", "O1b", "O1c", "M1", "Z3b", "Z3bs", "B4d", "B4ds"} <= set(passing) \
        and {"ARRIVAL", "RECON"} <= set(passing) and set(a) - set(passing) == OPEN_489
    ok.append(r); say("Q3 %d rows pass; the 441 three, B5b, B6', CLOSEs, E1u(s) and eight of the ten on 273 (483) among them; "
                      "none waits (534: SOURCEs and SOURCE COMPUTED-THEORIZED; 491: FACE2s, FACE2, the eight on "
                      "them and R1 back): %s" % (len(passing), r))
    say("%d/%d" % (sum(ok), len(ok)))
    return all(ok)


def mutants():
    caught = 0
    for m in ("beyond_computed", "drop", "outside"):
        MUT.clear(); MUT.add(m)
        try:
            bad = not selftest(quiet=True)
        except Exception:                                                    # noqa: BLE001
            bad = True
        caught += bad
        print("mutant %-16s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/3 caught" % caught)
    return caught == 3


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
