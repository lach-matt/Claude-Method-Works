#!/usr/bin/env python3
"""register_counts.py — keep the Register's own entry counts current.

    python3 tools/register_counts.py                     # count, and check the printed figures
    python3 tools/register_counts.py --appending 4       # what the figures become after N entries
    python3 tools/register_counts.py --write OUT.md      # emit the Register with the figures corrected

Exit 0 when the printed figures agree with the Register, 1 when they drift.

The Register prints its own extent in two places — the front matter and the back matter — and
nothing recomputes them, so they are maintained by hand and go stale silently. They already have:
the front matter carries the mature record as "165 to 1791, 1,470 entries" where the back matter
carries 165-1792, and under 1,470 the front matter's own three parts sum to 1,634 against its own
printed total of 1,635.

AN ENTRY IS A HEADING, NOT A NUMBER. Seven headings carry several numbers each — docket 30's seven,
`### 203, 215, 218, ...` and its like — and the printed total of 1,635 is 1,628 single-number
headings plus those 7. Counting numbers instead gives 1,660 and disagrees with everything the
volume prints, so the heading is the unit and this program uses it.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

HEAD = re.compile(r"^### (\d{1,4})((?:\s*,\s*\d{1,4})*)\s*$")
GENESIS_END, SUPERSEDED_END = 94, 164

# The two sentences that carry the figures. Each is matched, not reconstructed, so a rewrite
# changes only the numerals and leaves the prose exactly as the volume has it.
FRONT_TOTAL = re.compile(r"(\*\*)(\d[\d,]*) entries, 1 to (\d+)(\.?\*\*)")
FRONT_MATURE = re.compile(r"(and 165 to )(\d+)(, )(\d[\d,]*)( entries, are the mature record)")
BACK = re.compile(r"(\(genesis 1–94, superseded 95–164, mature record 165–)(\d+)(\))")


def count(text):
    """Every heading, split into the three blocks the volume names."""
    heads = []
    for line in text.split("\n"):
        m = HEAD.match(line)
        if m:
            nums = [int(m.group(1))] + [int(x) for x in re.findall(r"\d+", m.group(2) or "")]
            heads.append(nums)
    genesis = [h for h in heads if h[0] <= GENESIS_END]
    superseded = [h for h in heads if GENESIS_END < h[0] <= SUPERSEDED_END]
    mature = [h for h in heads if h[0] > SUPERSEDED_END]
    grouped = [h for h in heads if len(h) > 1]
    return {
        "headings": len(heads),
        "genesis": len(genesis),
        "superseded": len(superseded),
        "mature": len(mature),
        "grouped": len(grouped),
        "numbers": sum(len(h) for h in heads),
        "highest": max(n for h in heads for n in h),
    }


def printed(text):
    """The figures the volume states about itself."""
    out = {}
    m = FRONT_TOTAL.search(text)
    if m:
        out["front_total"] = int(m.group(2).replace(",", ""))
        out["front_highest"] = int(m.group(3))
    m = FRONT_MATURE.search(text)
    if m:
        out["front_mature_highest"] = int(m.group(2))
        out["front_mature"] = int(m.group(4).replace(",", ""))
    m = BACK.search(text)
    if m:
        out["back_mature_highest"] = int(m.group(2))
    n = len(re.findall(r"\*\*\d[\d,]* entries, 1 to \d+", text))
    out["sites"] = n
    return out


def group(n):
    return f"{n:,}"


def like(sample: str, n: int) -> str:
    """Format n the way this site already formats its numerals.

    The volume is not consistent between sites and is not being tidied: the total prints
    `1635 entries` with no separator while the mature figure prints `1,470 entries` with one.
    A count tool that normalises them edits prose it was not asked to touch, so each site keeps
    its own convention and only the digits move."""
    return f"{n:,}" if "," in sample else str(n)


def main(argv=None):
    here = pathlib.Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--register",
                    default=str(here / "method/members/The_Method_1_6___The_Register-2.md"))
    ap.add_argument("--appending", type=int, default=0, metavar="N",
                    help="report the figures after N further mature entries are seated")
    ap.add_argument("--write", metavar="OUT.md",
                    help="write the Register with the figures corrected (never in place)")
    a = ap.parse_args(argv)

    text = pathlib.Path(a.register).read_text(encoding="utf-8")
    c, p = count(text), printed(text)

    print(f"counted in {pathlib.Path(a.register).name}")
    print(f"  headings                 {group(c['headings'])}"
          f"   ({group(c['headings'] - c['grouped'])} single + {c['grouped']} grouped)")
    print(f"  numbers those headings carry  {group(c['numbers'])}"
          f"   (not the unit — see the module docstring)")
    print(f"  genesis      1-{GENESIS_END:<4}        {group(c['genesis'])}")
    print(f"  superseded  {GENESIS_END+1}-{SUPERSEDED_END}        {group(c['superseded'])}")
    print(f"  mature       165-{c['highest']}      {group(c['mature'])}")
    print(f"  sum of the three         {group(c['genesis'] + c['superseded'] + c['mature'])}")
    print(f"  highest entry number     {c['highest']}")

    print("\nprinted by the volume about itself")
    print(f"  front matter, total      {group(p.get('front_total', 0))} entries, "
          f"1 to {p.get('front_highest')}")
    print(f"  front matter, mature     165 to {p.get('front_mature_highest')}, "
          f"{group(p.get('front_mature', 0))} entries")
    print(f"  back matter, mature      165-{p.get('back_mature_highest')}")
    print(f"  sites carrying the total {p.get('sites')}")

    drift = []
    if p.get("front_total") != c["headings"]:
        drift.append(f"total: printed {group(p.get('front_total', 0))}, counted "
                     f"{group(c['headings'])}")
    if p.get("front_highest") != c["highest"]:
        drift.append(f"highest: printed {p.get('front_highest')}, counted {c['highest']}")
    if p.get("front_mature") != c["mature"]:
        drift.append(f"mature count: printed {group(p.get('front_mature', 0))}, counted "
                     f"{group(c['mature'])}")
    if p.get("front_mature_highest") != c["highest"]:
        drift.append(f"mature range end, front matter: printed {p.get('front_mature_highest')}, "
                     f"counted {c['highest']}")
    if p.get("back_mature_highest") != c["highest"]:
        drift.append(f"mature range end, back matter: printed {p.get('back_mature_highest')}, "
                     f"counted {c['highest']}")
    own = p.get("front_total"), (c["genesis"] + c["superseded"] + p.get("front_mature", 0))
    if own[0] != own[1]:
        drift.append(f"the front matter does not sum to itself: 94 + 70 + "
                     f"{group(p.get('front_mature', 0))} = {group(own[1])} against its own "
                     f"{group(own[0])}")

    print()
    if drift:
        print(f"DRIFT — {len(drift)} figure(s) do not agree with the Register:")
        for d in drift:
            print(f"  {d}")
    else:
        print("COUNTS CURRENT — every printed figure agrees with the Register.")

    if a.appending:
        n = a.appending
        hi = c["highest"] + n
        print(f"\nafter seating {n} further mature entries (through {hi}):")
        print(f"  front matter, total      {group(c['headings'] + n)} entries, 1 to {hi}")
        print(f"  front matter, mature     165 to {hi}, {group(c['mature'] + n)} entries")
        print(f"  back matter, mature      165-{hi}")
        print(f"  check  94 + 70 + {group(c['mature'] + n)} = "
              f"{group(c['genesis'] + c['superseded'] + c['mature'] + n)}")

    if a.write:
        hi = c["highest"]
        new = FRONT_TOTAL.sub(
            lambda m: f"{m.group(1)}{like(m.group(2), c['headings'])} entries, "
                      f"1 to {hi}{m.group(4)}", text, count=1)
        new = FRONT_MATURE.sub(
            lambda m: f"{m.group(1)}{hi}{m.group(3)}"
                      f"{like(m.group(4), c['mature'])}{m.group(5)}", new, count=1)
        new = BACK.sub(lambda m: f"{m.group(1)}{hi}{m.group(3)}", new, count=1)
        # the back matter repeats the total in its own sentence, in its own style
        new = re.sub(r"(\*\*)(\d[\d,]*)( entries, 1 to )(\d+)(\*\*)",
                     lambda m: f"{m.group(1)}{like(m.group(2), c['headings'])}"
                               f"{m.group(3)}{hi}{m.group(5)}", new)
        out = pathlib.Path(a.write)
        if out.resolve() == pathlib.Path(a.register).resolve():
            sys.exit("refusing to write over the Register member; name a different file")
        out.write_text(new, encoding="utf-8")
        before, after = text.encode("utf-8"), new.encode("utf-8")
        ch = sum(1 for x, y in zip(text.split("\n"), new.split("\n")) if x != y)
        print(f"\nwrote {out}")
        print(f"  {ch} line(s) changed; {len(before):,} B -> {len(after):,} B "
              f"({len(after) - len(before):+d})")

    return 1 if drift else 0


if __name__ == "__main__":
    sys.exit(main())
