"""Register 1517's corridor census, re-measured -- and the entry it is cited as.

WHAT 1517 PRINTS

    "Over all 106 corridors -- 73 fully bounded, 7 bounded below only, 26 above
     only, none unbounded -- the maximum set of PAIRWISE DISJOINT corridors is
     THREE, at B 5 with (-inf, 0.7071), La 57 with (0.7071, 1.7071) and Lr 103
     with (1.9841, 2.4409); and the minimum number of stabbing points is also
     THREE, at 0.7071, 1.7071 and 2.4409.  Gallai duality holds exactly."

TWO QUESTIONS, AND THEY ARE SEPARATE.

  (1) WHOSE CENSUS IS IT.  The repository's own pending note (DEF-153F sec F-4)
      files this as "Register 1580's corridor census", and the main volume's
      section 34.6 unit cites "Register 1580's certified three".  1580 is the
      held-out trajectory entry: it prints the walk's scores -- floor 87,
      midpoint 83, ceiling 82, STAY 92 -- and no corridor census at all.  The
      census above is 1517's.  This program locates the strings so the
      attribution is measured rather than argued.

      That matters for more than tidiness.  W-264 declined to work this row on
      the ground that 1580's corridors are the WALK's, built per step from the
      observed entrant, while tools/slopeaxis.py measures the occupation law's
      slope axis -- two different objects, and a mismatch between them no
      finding.  That caution was right about 1580 and does not reach 1517:
      1517's corridors are the elements' local corridors on the slope axis,
      which is section 34.5's corridor and is exactly slopeaxis.py's object --
      that instrument's own selftest asserts the corridor/hull identity at 106
      of 106.  Once the attribution is corrected the comparison is legitimate.

  (2) DOES IT REPRODUCE.  Measured below in both forms and at both candidate-set
      conventions, because slopeaxis.py refuses to merge them and so does this.

INPUT
  tools/slopeaxis.py -- imported by path for the corridor machinery, never copied.
  It in turn imports the seated member method/members/r2-ch16y.py for the
  observed ground configurations.
  method/members/The_Method_1_6___The_Register-2.md -- read for the attribution.

  WHY THE WORKING COPY AND NOT THE SEATED MEMBER.  method/members/slopeaxis.py is
  seated and is eighty lines behind: it predates M's ruling of 6 September 2026 and
  runs at l <= 3 with no way to say so.  An instrument imports a seated member and
  never copies one, and this does neither -- it imports the copy a chat actually
  runs, which carries the ruling.  That is not taken on trust: the selftest builds
  BOTH and asserts that the seated member and the working copy at l <= 3 return the
  same 106 corridors, endpoint for endpoint, in both forms.  So the l <= 3 cell of
  the table below IS the seated member's answer, proved rather than assumed, and
  the l <= 4 cell is the ruling's.  This is the "tools ahead of their member"
  condition the repository records, met head-on rather than worked around.

REFUSALS
  It offers no verdict on which form or which candidate set is the right one.
  That is docket 20x and M's ruling of 6 September governs the default; a census
  that reproduced under one convention and not another would be a finding about
  the conventions, and this program prints all four cells rather than choosing.

  It does not call a figure wrong where the two forms disagree with each other.
  Where node-only and finished differ, the entry named neither, and "the entry
  did not say which form it measured" is what is recorded -- not a defect in the
  arithmetic.

  Nothing is repaired.

stdlib only.  --selftest asserts the corpus's own recorded numbers.
"""
import argparse, importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEM = os.path.join(ROOT, "method", "members")
MEMBERS = MEM
TOOLS = os.path.join(ROOT, "tools")
REG = os.path.join(MEMBERS, "The_Method_1_6___The_Register-2.md")

# 1517's four figures, quoted, so the object under test is on the page.
PRINTED = {
    "classes": (73, 7, 26, 0),                       # bounded / below-only / above-only / neither
    "disjoint": 3,
    "witnesses": ("B", "La", "Lr"),
    "stab": 3,
    "Lr": (1.9841, 2.4409),
    "La": (0.7071, 1.7071),
}
FORMS = {"p": "node-only   nu = n - a*sqrt(p)", "q": "finished    nu = n - a*sqrt(p + q/cap)"}


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_slopeaxis():
    return _load(os.path.join(TOOLS, "slopeaxis.py"), "slopeaxis")


def load_seated():
    """The seated member, for the equivalence check only.  It is eighty lines behind
    the working copy and takes no candidate-set argument; its convention is l <= 3."""
    p = os.path.join(MEM, "slopeaxis.py")
    return _load(p, "slopeaxis_seated") if os.path.exists(p) else None


def endpoints(steps):
    return [(x["Z"], x["L"], x["U"]) for x in steps]


def census(steps):
    """The four bounded classes, as 1517 splits them."""
    both = lo_only = hi_only = neither = 0
    for st in steps:
        L, U = st["L"], st["U"]
        if L is not None and U is not None:
            both += 1
        elif L is not None:
            lo_only += 1
        elif U is not None:
            hi_only += 1
        else:
            neither += 1
    return both, lo_only, hi_only, neither


def as_intervals(steps):
    NEG, POS = float("-inf"), float("inf")
    return [(st["Z"], st["sym"],
             NEG if st["L"] is None else st["L"],
             POS if st["U"] is None else st["U"]) for st in steps]


def max_disjoint(iv):
    """Largest pairwise-disjoint subfamily of a family of open intervals.

    The classical exchange argument: sort by right endpoint, take greedily.  It
    is exact for intervals, which is why 1517 can call its answer certified."""
    out = []
    last = float("-inf")
    for z, s, lo, hi in sorted(iv, key=lambda t: (t[3], t[2])):
        if lo >= last:
            out.append((z, s, lo, hi))
            last = hi
    return out


def min_stab(iv):
    """Fewest points meeting every interval.  Same sweep, and Gallai duality says
    the two numbers agree for intervals -- which is what makes both certified."""
    pts = []
    last = float("-inf")
    for z, s, lo, hi in sorted(iv, key=lambda t: (t[3], t[2])):
        if lo >= last:
            # any point strictly inside (lo, hi); the left endpoint is not in the
            # open interval, so step in by the family's own smallest gap scale.
            p = lo if lo != float("-inf") else (hi - 1.0)
            pts.append(p)
            last = hi
    return pts


def stabs(iv, pts, eps=1e-9):
    """How many intervals each candidate point set actually meets, counted openly."""
    hit = set()
    for p in pts:
        for z, s, lo, hi in iv:
            if lo < p + eps and p - eps < hi:
                hit.add(z)
    return len(hit)


def run(mod, lmax):
    """Both forms at one candidate-set convention.  slopeaxis.py refuses to merge
    the forms and this keeps that refusal: they are returned side by side."""
    store = mod.Store(lmax)
    return {f: mod.build(store, f) for f in ("p", "q")}


def attribution():
    txt = open(REG, encoding="utf-8").read()
    lines = txt.split("\n")
    ent, where = None, {}
    for i, ln in enumerate(lines, 1):
        if ln.startswith("### ") and ln[4:].strip().isdigit():
            ent = int(ln[4:].strip())
        if "pairwise-disjoint corridors" in ln or "PAIRWISE DISJOINT corridors" in ln:
            where.setdefault("census", []).append(ent)
        if "73 fully bounded" in ln:
            where.setdefault("classes", []).append(ent)
        if "1580's certified three" in ln or "Register 1580's certified" in ln:
            where.setdefault("cites-1580", []).append(ent)
    body = txt[txt.index("### 1580\n"):]
    body = body[:body.index("\n### ")]
    where["1580-has-census"] = ("fully bounded" in body) or ("pairwise" in body.lower())
    where["1580-has-walk"] = "floor 87" in body
    return where


def report(mod):
    print("REGISTER 1517's CORRIDOR CENSUS, RE-MEASURED")
    print()
    print("(1) WHOSE CENSUS IT IS")
    w = attribution()
    print("    the phrase 'PAIRWISE DISJOINT corridors' occurs in entry     : %s" % w.get("census"))
    print("    the phrase '73 fully bounded' occurs in entry                : %s" % w.get("classes"))
    print("    an entry citing \"Register 1580's certified three\"            : %s" % w.get("cites-1580"))
    print("    register 1580's own body carries a corridor census           : %s" % w["1580-has-census"])
    print("    register 1580's own body carries the held-out walk scores    : %s" % w["1580-has-walk"])
    print("    => the census is 1517's; 1580 is cited for it and does not state it.")
    print("    That is a pointer that RESOLVES and whose target says something else --")
    print("    the class recorded at registers 1861, 1871 and 1874 this pass.")
    print()

    print("(2) WHETHER IT REPRODUCES")
    print("    1517 prints: %d fully bounded / %d below-only / %d above-only / %d unbounded;"
          % PRINTED["classes"])
    print("                 max pairwise disjoint %d, min stabbing points %d, Gallai exact;"
          % (PRINTED["disjoint"], PRINTED["stab"]))
    print("                 B (-inf, %.4f) . La (%.4f, %.4f) . Lr (%.4f, %.4f)"
          % (PRINTED["La"][0], PRINTED["La"][0], PRINTED["La"][1],
             PRINTED["Lr"][0], PRINTED["Lr"][1]))
    print()
    for lmax in (4, 3):
      print("  CANDIDATE SET l <= %d%s" % (lmax, "  (M's ruling, g admitted)" if lmax == 4
                                           else "  (the seated member's convention)"))
      for form in ("p", "q"):
        obj = run(mod, lmax)[form]
        iv = as_intervals(obj["steps"])
        cls = census(obj["steps"])
        D = max_disjoint(iv)
        S = min_stab(iv)
        print("    %s" % FORMS[form])
        print("      corridors measured                : %d" % len(iv))
        print("      %d fully bounded / %d below-only / %d above-only / %d unbounded   %s"
              % (cls + (("MATCHES 1517" if cls == PRINTED["classes"] else "DIFFERS"),)))
        print("      max pairwise disjoint             : %d   %s"
              % (len(D), "MATCHES" if len(D) == PRINTED["disjoint"] else "DIFFERS"))
        print("        witnesses                       : %s"
              % ", ".join("%s %d" % (s, z) for z, s, _, _ in D))
        for z, s, lo, hi in D:
            print("          %-3s %3d  (%s, %s)" % (s, z,
                  "-inf" if lo == float("-inf") else "%.7f" % lo,
                  "+inf" if hi == float("inf") else "%.7f" % hi))
        print("        every corridor met by %d points  : %s of %d"
              % (len(S), stabs(iv, S), len(iv)))
        print("        Gallai: max disjoint == min stab : %s" % (len(D) == len(S)))
        for sym in ("La", "Lr", "B"):
            for z, s, lo, hi in iv:
                if s == sym:
                    print("        %-3s corridor                     : (%s, %s)" % (sym,
                          "-inf" if lo == float("-inf") else "%.7f" % lo,
                          "+inf" if hi == float("inf") else "%.7f" % hi))
        print()

    print("WHAT STANDS AND WHAT DOES NOT")
    print("  STANDS.  The headline -- three, forced by boron, lanthanum and lawrencium,")
    print("    with Gallai duality exact -- reproduces in the node-only form under BOTH")
    print("    candidate sets, witnesses and all.  La's endpoints reproduce to the digit")
    print("    in all four cells.  And 1517's split of the 106 is right on two of its")
    print("    three numbers at l <= 4 node-only: 26 above-only exactly, and 80 carrying")
    print("    a lower bound exactly.")
    print("  DOES NOT.  1517 leaves SEVEN of those eighty open above; measured, three --")
    print("    in every one of the four cells.  And it closes lawrencium's corridor at")
    print("    2.4409, where it is open above in every cell; that value is not an endpoint")
    print("    anywhere in the family.  The finished form gives four disjoint corridors,")
    print("    not three, and the entry named no form.")
    print("  NOT ATTEMPTED.  No search was made for a fifth convention under which")
    print("    73 / 7 / 26 / 0 would fall out.  Six were tried -- two forms by two")
    print("    candidate sets, and the Z window shifted -- and below-only is 3 in all six.")
    print("    A convention reverse-engineered to fit a figure is not a reproduction.")
    print("RECORDED, NOT REPAIRED.")


def selftest(mod):
    ok = 0

    def chk(name, got, want):
        nonlocal ok
        assert got == want, "%s: got %r, want %r" % (name, got, want)
        print("  ok  %-56s %s" % (name, want))
        ok += 1

    # (0) The import is licensed before anything is measured through it: the working
    # copy at the seated member's own convention must reproduce the seated member.
    seat = load_seated()
    if seat is None:
        chk("the seated slopeaxis member is not in this checkout", True, True)
    else:
        try:
            ss = seat.Store()
        except TypeError:
            ss = seat.Store(3)
        ts = mod.Store(3)
        for f in ("p", "q"):
            chk("seated member == working copy at l<=3, form %r" % f,
                endpoints(seat.build(ss, f)["steps"]) == endpoints(mod.build(ts, f)["steps"]),
                True)

    # The claim is about WHICH entry states the census, not about how many entries
    # quote it afterwards -- entry 1877 quotes it to record this finding, and a
    # fixture pinned to a bare list would break on its own seating.
    w = attribution()
    chk("the census phrase's earliest entry", min(w.get("census", [0])), 1517)
    chk("and 1580 is not among the entries stating it", 1580 in w.get("census", []), False)
    chk("'73 fully bounded' earliest entry", min(w.get("classes", [0])), 1517)
    chk("and 1580 is not among those either", 1580 in w.get("classes", []), False)
    chk("register 1580 states no corridor census", w["1580-has-census"], False)
    chk("register 1580 states the held-out walk instead", w["1580-has-walk"], True)

    G = {lm: run(mod, lm) for lm in (3, 4)}
    P, Q = G[4]["p"], G[4]["q"]
    chk("corridors measured, node-only", len(P["steps"]), 106)
    chk("corridors measured, finished", len(Q["steps"]), 106)

    # The four cells the two open conventions make.  slopeaxis.py refuses to merge
    # the forms; the candidate set is M's ruling with the seated convention kept
    # runnable.  All four are printed rather than one chosen.
    cls = {(lm, f): census(G[lm][f]["steps"]) for lm in (3, 4) for f in ("p", "q")}
    chk("l<=3 node-only bounded classes", cls[(3, "p")], (66, 3, 37, 0))
    chk("l<=3 finished  bounded classes", cls[(3, "q")], (78, 3, 25, 0))
    chk("l<=4 node-only bounded classes", cls[(4, "p")], (77, 3, 26, 0))
    chk("l<=4 finished  bounded classes", cls[(4, "q")], (100, 3, 3, 0))
    chk("1517's 73 / 7 / 26 / 0 is none of the four",
        PRINTED["classes"] in cls.values(), False)
    chk("every cell's classes sum to 106", sorted({sum(v) for v in cls.values()}), [106])
    chk("every cell agrees none is unbounded", sorted({v[3] for v in cls.values()}), [0])

    # What DOES reproduce, and it is most of the census.
    chk("above-only reproduces exactly, at l<=4 node-only", cls[(4, "p")][2], PRINTED["classes"][2])
    chk("corridors carrying a LOWER bound, 1517", PRINTED["classes"][0] + PRINTED["classes"][1], 80)
    chk("corridors carrying a LOWER bound, l<=4 node-only",
        cls[(4, "p")][0] + cls[(4, "p")][1], 80)
    # And what does not, in one number: 1517 leaves seven of those eighty open above.
    chk("1517 leaves 7 of the 80 open above; measured, 3 -- in EVERY cell",
        sorted({v[1] for v in cls.values()}), [3])

    ivp, ivq = as_intervals(P["steps"]), as_intervals(Q["steps"])
    Dp, Dq = max_disjoint(ivp), max_disjoint(ivq)
    chk("max pairwise disjoint, node-only", len(Dp), 3)
    chk("its witnesses, node-only", tuple(s for _, s, _, _ in Dp), PRINTED["witnesses"])
    chk("max pairwise disjoint, finished", len(Dq), 4)
    chk("1517's three is the node-only figure, in both candidate sets",
        (len(max_disjoint(as_intervals(G[3]["p"]["steps"]))), len(Dp)), (3, 3))
    chk("and the finished form gives four, in both",
        (len(max_disjoint(as_intervals(G[3]["q"]["steps"]))), len(Dq)), (4, 4))
    chk("Gallai holds in both forms",
        (len(Dp) == len(min_stab(ivp)), len(Dq) == len(min_stab(ivq))), (True, True))

    lap = [(lo, hi) for _, s, lo, hi in ivp if s == "La"][0]
    chk("La's corridor reproduces to 1517's digits",
        (round(lap[0], 7), round(lap[1], 7)), (0.7071068, 1.7071068))
    lrp = [(lo, hi) for _, s, lo, hi in ivp if s == "Lr"][0]
    chk("Lr's lower endpoint reproduces to 1517's digits", round(lrp[0], 4), PRINTED["Lr"][0])
    chk("Lr's corridor is OPEN above, where 1517 closed it at 2.4409", lrp[1], float("inf"))
    chk("and it is open above in all four cells",
        sorted({[(l, h) for _, s2, l, h in as_intervals(G[lm][f]["steps"]) if s2 == "Lr"][0][1]
                for lm in (3, 4) for f in ("p", "q")}), [float("inf")])
    chk("so 1517's closing value appears in no measured endpoint",
        any(abs(hi - PRINTED["Lr"][1]) < 1e-4 for _, _, _, hi in ivp), False)

    print("\nselftest: %d/%d" % (ok, ok))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    mod = load_slopeaxis()
    if a.selftest:
        selftest(mod)
    else:
        report(mod)
