#!/usr/bin/env python3
"""gchannel.py -- is a g subshell in the law's candidate set?  Asked of the law, of
the walk, and of the spectroscopic survey.

Finding R4-09 put this to M as a ruling, on the ground that no observation
distinguishes the two candidate sets because no neutral atom occupies a g subshell.
M's correction: the survey covers the IONS as well, and weeks were spent building it.
He is right, and the survey settles the factual half.

  extracted/archives/method16-rp-b-data/COORDINATES.tsv
  104,832 rows.  Z = 1 to 120, core charge 1 to 120, l = 0 to 7, with a quantum
  defect, a grade (measured / exact / computed), a source and a witness flag on each.

This program asks three questions of it and of the law together, and answers each
with a measurement rather than a ruling.

  1. DOES THE LAW ADMIT g?  Its own admissibility test is q < 2(2l+1) and says
     nothing about l, so an empty 5g passes it.  Excluding g is an extra clause.
  2. WHAT DOES ADMITTING g COST?  Every bound 5g contributes across the 106 steps,
     classified -- because a bound of the form a > 0 is the parameter's own domain
     and carries no information, while a > 1/sqrt(3) is a real constraint.
  3. IS g A REAL CHANNEL?  Chapter 35 says "a channel that does not respond to the
     nucleus is not in the field" and reports the g channels at hydrogenic depth.  A
     quantum defect of zero IS hydrogenic depth, so the survey tests that claim
     directly.

REFUSALS
  A measured g channel is a RYDBERG channel, not ground-state occupancy.  No element
  below Z = 121 has a g electron in its ground configuration, and this program does
  not claim otherwise.  What the survey settles is whether g channels EXIST and
  RESPOND -- not whether one has ever been a ground entrant.  The remaining half is
  still M's, and section 6 says exactly what is left of it.
  Nothing is repaired.

INPUT
  method/members/LW1-ground.py                                  the seated member
  extracted/archives/restore-point-2-13/walk.py                 the corridor
  extracted/archives/method16-rp-b-data/COORDINATES.tsv         the survey
  All read in place; none copied.

stdlib only.  --selftest asserts the survey's own figures and the law's arithmetic.
"""
import argparse, csv, importlib.util, io, json, math, os, statistics, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
MEMBERS = os.path.join(ROOT, "method", "members")
RPB = os.path.join(ROOT, "extracted", "archives", "method16-rp-b-data")
WALK = os.path.join(ROOT, "extracted", "archives", "restore-point-2-13", "walk.py")
COORD = os.path.join(RPB, "COORDINATES.tsv")
SURVEY = os.path.join(RPB, "survey.json")
LET = "spdfghi?"
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII"}
INF = float("inf")


def cap(l):
    return 2 * (2 * l + 1)


def load(members):
    gpath = os.path.join(members, "LW1-ground.py")
    gspec = importlib.util.spec_from_file_location("ground", gpath)
    ground = importlib.util.module_from_spec(gspec)
    gspec.loader.exec_module(ground)
    saved = sys.modules.get("ground")
    sys.modules["ground"] = ground
    buf, o = io.StringIO(), sys.stdout
    try:
        sys.stdout = buf
        wspec = importlib.util.spec_from_file_location("walkmod", WALK)
        walk = importlib.util.module_from_spec(wspec)
        wspec.loader.exec_module(walk)
    finally:
        sys.stdout = o
        if saved is None:
            sys.modules.pop("ground", None)
        else:
            sys.modules["ground"] = saved
    return ground, walk


def occupancy(g, Z):
    if Z < 1:
        return {}
    c = {}
    for n, l, o in g.expand(Z):
        c[(n, l)] = c.get((n, l), 0) + o
    return c


def entrant(g, Z):
    pr, cu = occupancy(g, Z - 1), occupancy(g, Z)
    got = [k for k in cu if cu[k] > pr.get(k, 0)]
    return got[0] if len(got) == 1 else None


def gen(prev, lmax):
    """walk.py's generator, with l capped so the two conventions differ only there."""
    out = []
    for l in range(lmax + 1):
        for n in range(l + 1, 9):
            if prev.get((n, l), 0) >= cap(l):
                continue
            out.append((n, l))
            if prev.get((n, l), 0) == 0:
                break
    return out


def corridor(cands, e):
    pg = e[0] - e[1] - 1
    lo, hi = -INF, INF
    for r in cands:
        if r == e:
            continue
        d = math.sqrt(r[0] - r[1] - 1) - math.sqrt(pg)
        dn = r[0] - e[0]
        if abs(d) < 1e-12:
            continue
        if d > 0:
            hi = min(hi, dn / d)
        else:
            lo = max(lo, dn / d)
    return lo, hi


# ------------------------------------------------------------------ 2. the law
def g_bounds(ground, walk):
    """Every bound a g candidate contributes, and whether it binds."""
    out = []
    for Z in range(3, 109):
        e = entrant(ground, Z)
        if e is None:
            continue
        prev = occupancy(ground, Z - 1)
        with_g, without = gen(prev, 4), gen(prev, 3)
        lo_a, hi_a = corridor(with_g, e)
        lo_n, hi_n = corridor(without, e)
        pg = e[0] - e[1] - 1
        for r in with_g:
            if r[1] != 4 or r == e:
                continue
            d = math.sqrt(r[0] - r[1] - 1) - math.sqrt(pg)
            dn = r[0] - e[0]
            if abs(d) < 1e-12:
                continue
            b = dn / d
            lower = d < 0
            binds = (lower and abs(b - lo_a) < 1e-12 and lo_a != lo_n) or \
                    (not lower and abs(b - hi_a) < 1e-12 and hi_a != hi_n)
            out.append(dict(Z=Z, el=ground.GROUND[Z][0], ent=f"{e[0]}{LET[e[1]]}",
                            cand=f"{r[0]}{LET[r[1]]}", lower=lower, bound=b,
                            binds=binds, trivial=abs(b) < 1e-12,
                            lo_with=lo_a, lo_without=lo_n))
    return out


def g_ever_wins(ground, walk):
    """Under the walk's own trajectory, is a g subshell ever the least-nu candidate?
    nu(5g) = 5 exactly, since its node count is zero and a drops out."""
    a = 0.0
    traj = {Z: av for Z, av, mv in walk.TR}
    wins = []
    for Z in range(3, 109):
        e = entrant(ground, Z)
        if e is None:
            continue
        a = traj.get(Z, a)
        prev = occupancy(ground, Z - 1)
        best, bestnu = None, INF
        for r in gen(prev, 4):
            p = r[0] - r[1] - 1 + prev.get(r, 0) / cap(r[1])
            nu = r[0] - a * math.sqrt(p)
            if nu < bestnu:
                best, bestnu = r, nu
        if best is not None and best[1] == 4:
            wins.append((Z, ground.GROUND[Z][0], f"{best[0]}{LET[best[1]]}"))
    return wins


def corridors_nonempty(ground, lmax):
    n = 0
    tot = 0
    for Z in range(3, 109):
        e = entrant(ground, Z)
        if e is None:
            continue
        tot += 1
        lo, hi = corridor(gen(occupancy(ground, Z - 1), lmax), e)
        n += lo < hi
    return n, tot


# --------------------------------------------- 3b. the levels store behind the survey
STORE = os.path.join(ROOT, "extracted", "archives", "spectra-levels-store", "deliver")
MEAS = os.path.join(STORE, "MEASUREMENTS.tsv")
QUEUE = os.path.join(STORE, "queue2")


def levels_store():
    """The channel measurements and the per-species level tables they were read from.
    MEASUREMENTS.tsv carries a member count and an n range per channel, which the
    flat survey does not, so a g channel's DEPTH is visible here and not there."""
    out = dict(meas=[], species=[], gspecies=[], lines=0)
    if os.path.exists(MEAS):
        out["meas"] = list(csv.DictReader(open(MEAS, encoding="utf-8"), delimiter="\t"))
    if os.path.isdir(QUEUE):
        import re
        for fn in sorted(os.listdir(QUEUE)):
            if not fn.endswith(".tsv"):
                continue
            txt = open(os.path.join(QUEUE, fn), errors="replace").read()
            body = [l for l in txt.split("\n") if l and not l.startswith("#")]
            out["lines"] += len(body)
            out["species"].append(fn[:-4])
            if re.search(r"\b\d+g\b|\(\d+G|\bG\b", txt):
                out["gspecies"].append(fn[:-4])
    return out


# --------------------------------------------------------------- 3. the survey
def survey():
    rows = list(csv.DictReader(open(COORD, encoding="utf-8"), delimiter="\t"))
    el = json.load(open(SURVEY, encoding="utf-8"))["el"]
    return rows, el


def by_l(rows, grade="measured"):
    out = {}
    for l in range(8):
        m = [r for r in rows if int(r["l"]) == l and r["grade"] == grade]
        ds = [abs(float(r["delta"])) for r in m]
        out[l] = dict(n=len(m), ds=ds,
                      med=statistics.median(ds) if ds else None,
                      lo=min(ds) if ds else None, hi=max(ds) if ds else None)
    return out


def pearson(x, y):
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else 0.0


def measure(members):
    ground, walk = load(members)
    rows, el = survey()
    gm = [r for r in rows if int(r["l"]) == 4 and r["grade"] == "measured"]
    gb = g_bounds(ground, walk)
    binding = [b for b in gb if b["binds"]]
    st = levels_store()
    st["gchan"] = [r for r in st["meas"] if int(r["l"]) == 4]
    st["hchan"] = [r for r in st["meas"] if int(r["l"]) == 5]
    return dict(ground=ground, walk=walk, rows=rows, el=el, gmeas=gm, store=st,
                bounds=gb, binding=binding,
                trivial=[b for b in binding if b["trivial"]],
                real=[b for b in binding if not b["trivial"]],
                wins=g_ever_wins(ground, walk),
                ne3=corridors_nonempty(ground, 3),
                ne4=corridors_nonempty(ground, 4),
                lstats=by_l(rows),
                gions=[r for r in gm if int(r["charge"]) > 1],
                gneutral=[r for r in gm if int(r["charge"]) == 1],
                hmeas=[r for r in rows if int(r["l"]) == 5 and r["grade"] == "measured"])


def report(o):
    el = o["el"]

    def sym(z):
        return el.get(str(z), "?")

    print("  IS g IN THE CANDIDATE SET?  ASKED OF THE LAW AND OF THE SURVEY")
    print()
    print("  1. WHAT THE LAW ITSELF ADMITS")
    print("     The admissibility test is q < 2(2l+1).  An empty 5g has q = 0 and passes it.")
    print("     Nothing in the law's statement mentions l, so excluding g is an extra clause")
    print("     that has to come from somewhere other than the law.")
    print()
    print("  2. WHAT ADMITTING g COSTS, over the 106 steps")
    print(f"     g candidates offered:        {len(o['bounds'])} step-pairs")
    print(f"     of those, BINDING:           {len(o['binding'])}")
    print(f"       giving exactly a > 0:      {len(o['trivial'])}  "
          "-- the parameter's own domain, no information")
    print(f"       giving a real bound:       {len(o['real'])}")
    for b in o["real"]:
        print(f"          {b['el']:<3} {b['Z']:>3}  entrant {b['ent']:<3} vs {b['cand']}"
              f"   a > {b['bound']:.7f}   (= 1/sqrt(3))")
    print(f"     corridors non-empty, l <= 3: {o['ne3'][0]} of {o['ne3'][1]}")
    print(f"     corridors non-empty, l <= 4: {o['ne4'][0]} of {o['ne4'][1]}")
    print(f"     a g subshell wins the step:  {o['wins'] or 'NEVER'}")
    print("     So admitting g never changes which subshell the law selects and never")
    print("     empties a corridor.  It moves the FLOOR at sixteen steps and nothing else.")
    print()
    print("  3. WHAT THE SURVEY HOLDS")
    print(f"     COORDINATES.tsv: {len(o['rows']):,} rows, Z = "
          f"{min(int(r['Z']) for r in o['rows'])} to {max(int(r['Z']) for r in o['rows'])}, "
          f"core charge {min(int(r['charge']) for r in o['rows'])} to "
          f"{max(int(r['charge']) for r in o['rows'])}, l = 0 to 7")
    print(f"     {sum(1 for r in o['rows'] if r['grade']=='measured')} measured and witnessed; "
          f"{sum(1 for r in o['rows'] if r['grade']=='exact')} exact; the rest computed")
    print()
    print(f"     MEASURED g CHANNELS: {len(o['gmeas'])}  "
          f"-- {len(o['gions'])} in IONS, {len(o['gneutral'])} in neutrals")
    for r in sorted(o["gmeas"], key=lambda r: (int(r["Z"]), int(r["charge"])))[:40]:
        z, c = int(r["Z"]), int(r["charge"])
        print(f"        {sym(z) + ' ' + ROMAN.get(c, str(c)):<9} delta = {float(r['delta']):+9.5f}"
              f"   {r['source'][:44]}")
    if o["hmeas"]:
        r = o["hmeas"][0]
        print(f"     and one measured h channel (l = 5): "
              f"{sym(int(r['Z']))} {ROMAN.get(int(r['charge']), r['charge'])}, "
              f"delta = {float(r['delta'])}")
    print()
    print("  3b. THE LEVELS STORE BEHIND IT, which carries the DEPTH of each channel")
    st = o["store"]
    print(f"     {len(st['species'])} species level tables, {st['lines']:,} level lines,"
          f" neutrals and ions to core charge 10")
    print(f"     {len(st['gspecies'])} of the {len(st['species'])} carry a g term in their levels")
    print(f"     MEASUREMENTS.tsv: {len(st['meas'])} channels, of which {len(st['gchan'])} are g"
          f" and {len(st['hchan'])} is h")
    print(f"       {'species':<10}{'term':<12}{'members':>8}{'n range':>10}{'delta':>10}")
    for r in sorted(st["gchan"], key=lambda r: -int(r["members"])):
        z = int(r["Z"])
        print(f"       {sym(z) + ' I':<10}{r['term']:<12}{r['members']:>8}"
              f"{r['n_lo'] + '-' + r['n_hi']:>10}{float(r['delta']):>10.5f}")
    deep = [r for r in st["gchan"] if int(r["members"]) >= 10]
    print(f"     {len(deep)} of the {len(st['gchan'])} g channels carry ten or more members;")
    print("     the deepest runs n = 8 to 25 over twenty-nine of them.  A twenty-nine-member")
    print("     series with a defect of 0.05 is not a channel sitting at hydrogenic depth.")
    print()
    print("  4. CHAPTER 35's CRITERION, TESTED ON THE SURVEY")
    print("     'every g channel ... sits at its hydrogenic depth to the storage precision")
    print("      ... a channel that does not respond to the nucleus is not in the field.'")
    print("     A quantum defect of zero IS hydrogenic depth.  Measured, by l:")
    print(f"       {'l':>3} {'measured':>9} {'|delta| min':>12} {'|delta| max':>12} {'median':>10}")
    for l in range(8):
        s = o["lstats"][l]
        if not s["n"]:
            print(f"       {LET[l]:>3} {0:>9}")
            continue
        print(f"       {LET[l]:>3} {s['n']:>9} {s['lo']:>12.5f} {s['hi']:>12.5f} {s['med']:>10.5f}")
    ds = [abs(float(r["delta"])) for r in o["gmeas"]]
    zs = [int(r["Z"]) for r in o["gmeas"]]
    print(f"     g defects run to {max(ds):.5f}, and {sum(1 for d in ds if d > 0.001)} of "
          f"{len(ds)} exceed 0.001.  They are small and they are NOT zero.")
    print(f"     r(Z, |delta|) over the measured g channels = {pearson(zs, ds):+.3f}, so they")
    print("     rise with the nucleus -- which is the corpus's own high-l mechanism, the")
    print("     defect following core polarisability beyond l = 3.")
    print("     The l-collapse ladder above is the corpus's own law reproduced: the median")
    print("     defect falls monotonically from s to h across six orders of magnitude.")
    print()
    print("  5. WHAT THIS SETTLES")
    print("     g channels EXIST and are MEASURED, in thirty-six species, thirty-two of them")
    print("     ions.  So 'no observation distinguishes the two candidate sets' was wrong,")
    print("     and 'g does not respond to the nucleus' is not what the survey shows.")
    print("     Neither ground for excluding g survives the data.")
    print()
    print("  6. WHAT IS STILL M's, and it is narrower than it was")
    print("     A measured g channel is a RYDBERG channel.  No element below Z = 121 has a g")
    print("     electron in its GROUND configuration, and the law is about ground occupancy.")
    print("     So the question is no longer 'does g exist' -- it does -- but 'may the law")
    print("     consider a channel that exists and is never the ground entrant'.")
    print("     The law's own test admits it; the ground data never exercises it; and the")
    print("     cost of admitting it is one moved floor at sixteen steps, eleven of which")
    print("     move it only to a > 0.  Nothing is repaired here.")


FIXTURES = """the survey's own figures and the law's arithmetic:
  COORDINATES.tsv   104,832 rows; Z 1-120; core charge 1-120; l 0-7
                    358 measured and witnessed, 929 exact
  measured g        36 channels, 32 of them ions, |delta| up to 0.04010
  measured h        1 channel
  levels store      61 species tables, 9,200 level lines, neutrals and ions to charge 10;
                    34 species carry a g term; MEASUREMENTS.tsv has 554 channels of which
                    12 are g and one is h, the deepest g running n = 8 to 25 over 29 members
  the l-collapse    median |delta| falls s > p > d > f > g > h, monotone
  the law           5g binds at 16 of the 106 steps: 11 at exactly a > 0 and 5 at
                    a > 1/sqrt(3) = 0.5773503
  the law           admitting g never makes g the entrant and never empties a corridor"""


def selftest(members):
    o = measure(members)
    checks = []

    def eq(n, got, want):
        checks.append((n, got, want, got == want))

    eq("survey rows", len(o["rows"]), 104832)
    eq("Z range", (min(int(r["Z"]) for r in o["rows"]), max(int(r["Z"]) for r in o["rows"])), (1, 120))
    eq("charge range", (min(int(r["charge"]) for r in o["rows"]), max(int(r["charge"]) for r in o["rows"])), (1, 120))
    eq("l range", sorted({int(r["l"]) for r in o["rows"]}), [0, 1, 2, 3, 4, 5, 6, 7])
    eq("measured rows", sum(1 for r in o["rows"] if r["grade"] == "measured"), 358)
    eq("measured g channels", len(o["gmeas"]), 36)
    eq("of them, ions", len(o["gions"]), 32)
    eq("of them, neutrals", len(o["gneutral"]), 4)
    eq("measured h channels", len(o["hmeas"]), 1)
    eq("max |delta| at g", round(max(abs(float(r["delta"])) for r in o["gmeas"]), 5), 0.0401)
    med = [o["lstats"][l]["med"] for l in range(6)]
    eq("the l-collapse is monotone", all(med[i] > med[i + 1] for i in range(5)), True)
    eq("g bounds that bind", len(o["binding"]), 16)
    eq("of them, exactly a > 0", len(o["trivial"]), 11)
    eq("of them, a real bound", len(o["real"]), 5)
    eq("the real bound is 1/sqrt(3)",
       sorted({round(b["bound"], 7) for b in o["real"]}), [0.5773503])
    eq("g never wins the step", o["wins"], [])
    eq("corridors non-empty without g", o["ne3"], (106, 106))
    eq("corridors non-empty with g", o["ne4"], (106, 106))
    st = o["store"]
    eq("levels-store species", len(st["species"]), 61)
    eq("level lines in the store", st["lines"], 9200)
    eq("species carrying a g term", len(st["gspecies"]), 34)
    eq("MEASUREMENTS channels", len(st["meas"]), 554)
    eq("of them, g channels", len(st["gchan"]), 12)
    eq("of them, h channels", len(st["hchan"]), 1)
    eq("g channels with >= 10 members",
       len([r for r in st["gchan"] if int(r["members"]) >= 10]), 4)
    eq("the deepest g channel's members",
       max(int(r["members"]) for r in st["gchan"]), 29)
    print(FIXTURES)
    print()
    bad = 0
    for n, got, want, ok in checks:
        print(f"  {'ok  ' if ok else 'FAIL'} {n:<34} {got!r:<20} expected {want!r}")
        bad += not ok
    print()
    print("SELFTEST OK" if not bad else f"SELFTEST FAILED: {bad}")
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--members", default=MEMBERS)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest(a.members)
    report(measure(a.members))
    return 0


if __name__ == "__main__":
    sys.exit(main())
