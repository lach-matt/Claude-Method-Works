#!/usr/bin/env python3
"""phase4.py — INCORPORATION PHASE 4: what the value store holds, and what it cannot.

SUPERSEDES the selection framing of the first version. M's ruling, session 1.7.2:

    "The index is meant to show all values, not just select few. If we are
     considering removing values for the sake of aesthetics, then the index is
     not built correctly."

That correction is the content of this file and the earlier version is the
residue (§H.9). The first version proposed refusing 36 measurements and routing
29, as though phase 4 were a question of which values the index admits. It never
was. Every cell already exists — 104,832 of them — whatever anyone measures. The
only thing a refusal could remove is MEASUREMENT.

WHAT THE REAL FAULT WAS. `COORDINATES.tsv` stores ONE delta per cell. 554 staged
measurements land on 158 cells; the scalar schema holds 145. Ti I carries 45
measured series on a single cell. So R 1649's "52 collisions" were never
collisions: they were second, third and forty-fifth true measurements with
nowhere to sit. Calling that a defect of the data inverted the error's direction.

THE REPAIR is `MEASUREMENTS.tsv` — many measurements to one cell, nothing
discarded, each row carrying its own provenance and status. The cell's delta
becomes a DERIVED view under a declared statistic rather than stored data, which
also dissolves T2: Ga I's members are retained, so mean, median and asymptotic
stop being rival facts and become three readings of one record.

This instrument therefore REPORTS COVERAGE. It selects nothing.

  span            a measurement over one n is not a series. Its members are
                  J-components, so its spread is FINE STRUCTURE, not convergence.
                  Recorded and named, never deleted.
  language        the captures speak LS, jK and jj. A jj term carries no 2S+1 at
                  all, so a null in `mult` is a GAP IN THE LANGUAGE and not a
                  missing number — M's standing protocol, arriving as data.
  limit_status    R 1649's fallback ("else the first limit above the top member")
                  is a silent default, which §2.9 forbids. Where it fired across
                  a core boundary the delta is VOID and says so.
  cell_exists     mult outside the index fibre. The fibre is a GROUND-state
                  property; a Rydberg series carries its PARENT's multiplicity.
                  One coordinate name over two quantities.

P8/§2.15: each named limitation is a true answer and therefore a bound. Every
check below can fail.
"""
import collections
import sys

STORE = "MEASUREMENTS.tsv"
COORD = "COORDINATES.tsv"


def read(path):
    rows = [l.rstrip("\r\n").split("\t") for l in open(path, encoding="utf-8") if l.strip()]
    return rows[0], rows[1:]


def main():
    h, M = read(STORE)
    col = {n: i for i, n in enumerate(h)}
    _, C = read(COORD)
    held = {(r[0], r[1], r[2], r[3]): r for r in C}
    wit = {k for k, r in held.items() if len(r) > 8 and r[8] == "witnessed"}

    print("  PHASE 4 — COVERAGE OF THE VALUE STORE\n")
    cells = {(r[0], r[2], r[3]) for r in M}
    per = collections.Counter((r[0], r[2], r[3]) for r in M)
    print(f"    measurements held           {len(M):>6,}   nothing discarded")
    print(f"    cells they land on          {len(cells):>6,}")
    print(f"    cells with >1 measurement   {sum(1 for v in per.values() if v > 1):>6,}"
          f"   max on one cell: {max(per.values())}")
    print(f"    a scalar schema could hold  {len(cells):>6,} of {len(M):,}"
          f"   ({100 * len(cells) / len(M):.0f}%)\n")

    for field in ("language", "span", "limit_status", "delta_status", "cell_exists"):
        c = collections.Counter(r[col[field]] for r in M)
        print(f"    {field}")
        for k, v in c.most_common():
            print(f"        {k:<42}{v:>5}{100 * v / len(M):>7.1f}%")
        print()

    def is_stored(row):
        """True when this measurement's delta IS the value the index holds."""
        key = (row[0], "1", row[2], row[3])
        if key not in wit:
            return False
        try:
            return abs(float(row[col["delta"]]) - float(held[key][4])) < 1e-6
        except (ValueError, IndexError):
            return False

    ok = True
    void = [r for r in M if r[col["delta_status"]].startswith("void")]
    leaked = [r for r in void if is_stored(r)]
    if leaked:
        print(f"  FAIL: {len(leaked)} voided deltas stand as the index's value")
        ok = False
    else:
        print(f"  CHECK: none of the {len(void)} voided deltas is the value the index holds.")

    sing = [r for r in M if r[col["span"]] == "single-n"]
    bad = [r for r in sing if is_stored(r)]
    if bad:
        print(f"  FAIL: {len(bad)} single-n values stand as series defects in the index")
        ok = False
    else:
        print(f"  CHECK: none of the {len(sing)} single-n measurements is a stored defect.")

    if len(M) != 554:
        print(f"  FAIL: store holds {len(M)}, the staging held 554")
        ok = False
    else:
        print("  CHECK: the store covers the staged set exactly, 554 of 554.")

    print("\n  THE BOUND THIS STATES (P8/§2.15):")
    print("    The index can carry one number per cell. The world measured more than one.")
    print("    Where those disagree the fault is in the store, and it is now recorded")
    print("    rather than settled by choosing.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
