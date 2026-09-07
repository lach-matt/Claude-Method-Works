#!/usr/bin/env python3
"""withdrawncite.py — registers the main volume withdraws and then cites as authority. Phase 1, item
E-042, and the complement of `r2-warn`'s census.

WHAT r2-warn ALREADY DOES. It censuses the entries that CARRY a `WARNING:` marker and reads each
against its citing lines -- 39 entries, 59 citer lines at this build. An entry with no marker is
outside its set by construction.

WHAT THIS DOES. The other direction: the main volume sometimes withdraws an entry IN PROSE. Every
line of the volume that both uses a withdrawal word and names a register is collected, and each
register so named is then checked twice -- does the volume cite it again as authority somewhere
else, and does its Register entry carry a `WARNING:`?

THE RESULT IS A CLASS OF ONE, AND IT IS EXACTLY E-042's.

  register 497 -- "the counting/coupling split they were read as showing is WITHDRAWN with register
  497" (main L3883) -- is cited as authority thirty-seven lines later: "the exact triangle costs
  cells, it costs E, and it costs seed. Register 497." (L3920), and again at L3951. The entry itself
  carries NO WARNING.

So the volume withdraws an entry and then rests a conclusion on it, in one section, and nothing in
the Register tells a reader either thing. Recorded, not repaired: which of the two readings survives
is subject matter.

stdlib only.  --selftest asserts the census and its one row.
"""
import argparse, collections, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.join(os.path.dirname(HERE), "members")


def load():
    M = open(os.path.join(MEM, "The_Method_1_6-2.md"), encoding="utf-8").read().split("\n")
    R = open(os.path.join(MEM, "The_Method_1_6___The_Register-2.md"), encoding="utf-8").read()
    parts = re.split(r"\n### ([0-9, ]+)\n", R)
    ents = {}
    for i in range(1, len(parts), 2):
        for n in re.findall(r"\d+", parts[i]):
            ents[int(n)] = parts[i + 1]
    return M, ents


def census():
    M, ents = load()
    withdrawn = collections.defaultdict(list)
    cited = collections.defaultdict(list)
    for i, l in enumerate(M, 1):
        if re.search(r"withdraw", l, re.I):
            for n in re.findall(r"[Rr]egister (\d+)", l):
                withdrawn[int(n)].append(i)
        for n in re.findall(r"[Rr]egisters? (\d+)", l):
            cited[int(n)].append(i)
    rows = []
    for n, ws in sorted(withdrawn.items()):
        other = [i for i in cited.get(n, []) if i not in ws]
        rows.append(dict(reg=n, withdrawn_at=ws, cited_at=other,
                         warning="WARNING" in ents.get(n, ""), seated=n in ents))
    return rows


def report():
    rows = census()
    print("Registers the main volume withdraws in prose, and what it does with them afterwards\n")
    print(f"  registers named on a withdrawing line: {len(rows)}")
    print(f"  {'register':>9}{'withdrawn at':>16}{'also cited at':>22}{'WARNING?':>11}{'seated?':>9}")
    for r in rows:
        print(f"  {r['reg']:>9}{str(r['withdrawn_at']):>16}"
              f"{(str(r['cited_at']) if r['cited_at'] else '—'):>22}"
              f"{str(r['warning']):>11}{str(r['seated']):>9}")
    bad = [r for r in rows if r["cited_at"] and not r["warning"]]
    print(f"\n  withdrawn AND re-cited as authority: {sum(1 for r in rows if r['cited_at'])}")
    print(f"  of those, with no WARNING in the entry: {len(bad)}")
    for r in bad:
        print(f"\n  Register {r['reg']}: the volume withdraws it at L{r['withdrawn_at'][0]} and rests")
        print(f"  a conclusion on it at L{', L'.join(str(i) for i in r['cited_at'])}, and the entry")
        print("  says neither thing. RECORDED, NOT REPAIRED — which reading survives is subject matter.")
    print("\n  This is the complement of r2-warn, which censuses the entries that DO carry a marker")
    print("  and cannot see one that does not.")


def selftest():
    ok = fail = 0
    def eq(name, got, want):
        nonlocal ok, fail
        if got == want: ok += 1; print(f"  OK   {name}: {got}")
        else: fail += 1; print(f"  FAIL {name}: got {got}, want {want}")
    rows = census()
    eq("registers named on a withdrawing line", len(rows), 3)
    both = [r for r in rows if r["cited_at"]]
    eq("withdrawn and also cited: a class of one", len(both), 1)
    eq("and it is register 497", both[0]["reg"], 497)
    eq("withdrawn at main L3883", both[0]["withdrawn_at"], [3883])
    eq("cited as authority at L3920 and L3951", both[0]["cited_at"], [3920, 3951])
    eq("entry 497 carries no WARNING", both[0]["warning"], False)
    eq("entry 497 is seated", both[0]["seated"], True)
    eq("no other withdrawn register is re-cited",
       [r["reg"] for r in rows if r["cited_at"] and r["reg"] != 497], [])
    print(f"\nOK: {ok}  FAIL: {fail}")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    sys.exit(selftest() if a.selftest else (report() or 0))
